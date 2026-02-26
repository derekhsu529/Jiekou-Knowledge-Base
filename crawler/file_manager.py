"""文件组织和命名管理"""

import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List
from urllib.parse import urlparse, unquote
from .utils import get_logger

logger = get_logger(__name__)


class FileManager:
    """管理文件组织和命名"""

    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.knowledge_base = self.base_dir / "knowledge_base"
        self.data_dir = self.base_dir / "data"

    def url_to_filepath(self, url_info: Dict) -> Path:
        """
        将 URL 信息转换为本地文件路径

        URL 模式:
        - jiekou.ai/ -> knowledge_base/pages/index.md
        - jiekou.ai/pricing -> knowledge_base/pages/pricing.md
        - jiekou.ai/models/model-detail/gpt-4o -> knowledge_base/models/gpt-4o.md
        - docs.jiekou.ai/docs/model/llm.md -> knowledge_base/docs/model/llm.md
        """
        url = url_info["url"]
        parsed = urlparse(url)
        path = unquote(parsed.path)

        if "docs.jiekou.ai" in parsed.netloc:
            # 文档页面
            # /docs/cc/introduction.md -> docs/cc/introduction.md
            if path.startswith("/docs/"):
                rel_path = path[6:]  # 移除 /docs/
            else:
                rel_path = path.lstrip("/")

            # 移除 .md 扩展名（我们会重新添加）
            if rel_path.endswith(".md"):
                rel_path = rel_path[:-3]

            filename = self._sanitize_filename(rel_path)
            return self.knowledge_base / "docs" / f"{filename}.md"

        elif "/models/model-detail/" in path:
            # 模型详情页
            model_name = path.split("/")[-1]
            filename = self._sanitize_filename(model_name)
            return self.knowledge_base / "models" / f"{filename}.md"

        elif "/legal/" in path:
            # 法律页面
            page_name = path.split("/")[-1] or "terms"
            filename = self._sanitize_filename(page_name)
            return self.knowledge_base / "pages" / "legal" / f"{filename}.md"

        else:
            # 主站其他页面
            page_name = path.strip("/") or "index"
            filename = self._sanitize_filename(page_name)
            return self.knowledge_base / "pages" / f"{filename}.md"

    def _sanitize_filename(self, name: str) -> str:
        """清理文件名，确保文件系统兼容"""
        # 保留路径分隔符用于创建子目录
        parts = name.split("/")
        cleaned_parts = []

        for part in parts:
            if not part:
                continue
            # 替换非法字符
            part = re.sub(r'[<>:"|?*]', '-', part)
            # 替换多个空格为单个连字符
            part = re.sub(r'\s+', '-', part)
            # 移除开头和结尾的点和空格
            part = part.strip('. ')
            # 限制长度
            part = part[:100]
            if part:
                cleaned_parts.append(part)

        return "/".join(cleaned_parts) if cleaned_parts else "unnamed"

    def save_markdown(self, filepath: Path, content: str, metadata: Dict):
        """
        保存 Markdown 文件，添加 YAML frontmatter

        Args:
            filepath: 文件路径
            content: Markdown 内容
            metadata: 元数据（title, url, crawled_at 等）
        """
        # 确保目录存在
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # 构建 frontmatter
        title = metadata.get("title", "Untitled").replace('"', '\\"')
        url = metadata.get("url", "")
        crawled_at = metadata.get("crawled_at", datetime.now().isoformat())

        frontmatter = f'''---
title: "{title}"
url: "{url}"
crawled_at: "{crawled_at}"
---

'''

        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter + content)

        logger.debug(f"保存文件: {filepath}")

    def save_urls(self, urls: List[Dict]):
        """保存发现的 URL 列表"""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        urls_file = self.data_dir / "urls.json"

        with open(urls_file, 'w', encoding='utf-8') as f:
            json.dump(urls, f, ensure_ascii=False, indent=2)

        logger.info(f"保存 {len(urls)} 个 URL 到 {urls_file}")

    def load_urls(self) -> List[Dict]:
        """加载已保存的 URL 列表"""
        urls_file = self.data_dir / "urls.json"

        if not urls_file.exists():
            logger.warning(f"URL 文件不存在: {urls_file}")
            return []

        with open(urls_file, 'r', encoding='utf-8') as f:
            urls = json.load(f)

        logger.info(f"加载 {len(urls)} 个 URL")
        return urls

    def build_index(self) -> Dict:
        """构建知识库索引"""
        index = {
            "generated_at": datetime.now().isoformat(),
            "stats": {},
            "pages": []
        }

        stats = {"total": 0}

        # 遍历所有 Markdown 文件
        for md_file in self.knowledge_base.rglob("*.md"):
            stats["total"] += 1

            # 获取相对路径
            rel_path = md_file.relative_to(self.knowledge_base)
            category = rel_path.parts[0] if len(rel_path.parts) > 1 else "other"

            stats[category] = stats.get(category, 0) + 1

            # 读取 frontmatter
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 简单解析 frontmatter
                if content.startswith('---'):
                    end = content.find('---', 3)
                    if end > 0:
                        frontmatter = content[3:end]
                        title_match = re.search(r'title:\s*"([^"]*)"', frontmatter)
                        url_match = re.search(r'url:\s*"([^"]*)"', frontmatter)

                        index["pages"].append({
                            "title": title_match.group(1) if title_match else md_file.stem,
                            "path": str(rel_path),
                            "url": url_match.group(1) if url_match else "",
                            "category": category
                        })
            except Exception as e:
                logger.warning(f"解析文件失败 {md_file}: {e}")

        index["stats"] = stats

        # 保存索引
        index_file = self.knowledge_base / "_index.json"
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, ensure_ascii=False, indent=2)

        logger.info(f"构建索引完成: {stats}")
        return index
