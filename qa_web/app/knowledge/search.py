"""知识库搜索模块 - 基于 test_qa.py 提取"""

import json
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass
from ..config import KNOWLEDGE_BASE_DIR

# 同义词/相关词映射表
SYNONYMS = {
    "视频": ["video", "i2v", "t2v", "v2v", "kling", "vidu", "wan", "sora", "veo", "hailuo", "minimax"],
    "图片": ["image", "img", "picture", "t2i", "i2i", "flux", "stable", "midjourney", "dall"],
    "音频": ["audio", "speech", "tts", "voice", "elevenlabs", "fish"],
    "文本": ["text", "llm", "chat", "gpt", "claude", "gemini", "qwen", "llama"],
    "价格": ["price", "pricing", "cost", "费用", "收费"],
    "调用": ["api", "sdk", "接口", "使用", "集成"],
    "vscode": ["vs code", "ide", "编辑器", "claude code", "插件"],
    "模型": ["model", "models"],
}

# 缓存知识库索引
_index_cache = None


@dataclass
class SearchResult:
    """搜索结果"""
    title: str
    path: str
    url: str
    score: int
    content_preview: str


def _load_index() -> Dict:
    """加载知识库索引（带缓存）"""
    global _index_cache
    if _index_cache is None:
        index_file = KNOWLEDGE_BASE_DIR / "_index.json"
        with open(index_file, encoding='utf-8') as f:
            _index_cache = json.load(f)
    return _index_cache


def _expand_keywords(query: str) -> set:
    """扩展关键词，添加同义词"""
    query_lower = query.lower()
    keywords = set(query_lower.split())

    expanded = set(keywords)
    for word in keywords:
        for key, synonyms in SYNONYMS.items():
            if word in key or key in word:
                expanded.update(synonyms)
            if word in synonyms:
                expanded.add(key)
                expanded.update(synonyms)

    return expanded


def _search_in_content(content: str, keywords: set) -> int:
    """在文档内容中搜索关键词，返回匹配分数"""
    content_lower = content.lower()
    score = 0
    for kw in keywords:
        count = min(content_lower.count(kw), 5)
        score += count
    return score


def search_knowledge_base(query: str, max_docs: int = 8) -> List[SearchResult]:
    """
    搜索知识库，返回最相关的文档列表

    Args:
        query: 用户查询
        max_docs: 返回的最大文档数

    Returns:
        SearchResult 列表
    """
    index = _load_index()
    keywords = _expand_keywords(query)

    scored_docs = []
    for page in index["pages"]:
        title = page.get("title", "").lower()
        path = page.get("path", "").lower()

        # 标题和路径匹配（权重高）
        title_score = sum(3 for kw in keywords if kw in title)
        path_score = sum(2 for kw in keywords if kw in path)

        # 内容匹配
        doc_path = KNOWLEDGE_BASE_DIR / page["path"]
        content_score = 0
        content_preview = ""

        if doc_path.exists():
            try:
                with open(doc_path, encoding='utf-8') as f:
                    content = f.read()
                    content_score = _search_in_content(content, keywords)
                    # 提取预览（跳过 frontmatter）
                    lines = content.split('\n')
                    start = 0
                    if lines[0].strip() == '---':
                        for i, line in enumerate(lines[1:], 1):
                            if line.strip() == '---':
                                start = i + 1
                                break
                    content_preview = '\n'.join(lines[start:start+10])[:500]
            except Exception:
                pass

        total_score = title_score + path_score + content_score
        if total_score > 0:
            scored_docs.append((total_score, page, content_preview))

    # 按分数排序
    scored_docs.sort(key=lambda x: x[0], reverse=True)
    top_docs = scored_docs[:max_docs]

    # 如果没有匹配，返回默认文档
    if not top_docs:
        for page in index["pages"][:max_docs]:
            doc_path = KNOWLEDGE_BASE_DIR / page["path"]
            content_preview = ""
            if doc_path.exists():
                with open(doc_path, encoding='utf-8') as f:
                    content_preview = f.read()[:500]
            top_docs.append((0, page, content_preview))

    results = []
    for score, doc, preview in top_docs:
        title = doc.get("title", "").strip()
        # 如果标题为空或是 Untitled，从内容中提取标题
        if not title or title.lower() == "untitled":
            title = _extract_title_from_content(doc["path"], preview)
        results.append(SearchResult(
            title=title,
            path=doc["path"],
            url=doc.get("url", ""),
            score=score,
            content_preview=preview
        ))
    return results


def _extract_title_from_content(path: str, preview: str) -> str:
    """从文档内容中提取标题"""
    lines = preview.split('\n')

    # 先尝试找 # 开头的标题行，或 === 下划线标题
    for i, line in enumerate(lines):
        stripped = line.strip()
        # # 开头的标题
        if stripped.startswith('#'):
            title = stripped.lstrip('#').strip()
            if title:
                return title
        # 检查下一行是否是 === 或 ---（Markdown setext 标题格式）
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if next_line and (next_line.startswith('===') or next_line.startswith('---')):
                if stripped and not stripped.startswith('```'):
                    return stripped

    # 如果没找到标题，取第一行非空文本
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('===') and not stripped.startswith('---') and not stripped.startswith('```'):
            return stripped[:60] + ('...' if len(stripped) > 60 else '')

    # 最后使用文件名
    filename = path.replace("\\", "/").split("/")[-1].rsplit(".", 1)[0]
    return filename.replace("_", " ").replace("-", " ").title()


def get_context_for_qa(results: List[SearchResult]) -> str:
    """将搜索结果转换为问答上下文"""
    contents = []
    for result in results:
        doc_path = KNOWLEDGE_BASE_DIR / result.path
        if doc_path.exists():
            with open(doc_path, encoding='utf-8') as f:
                content = f.read()
                contents.append(f"### {result.title}\nURL: {result.url}\n{content[:3000]}")

    return "\n\n---\n\n".join(contents)
