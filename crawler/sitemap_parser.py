"""解析 sitemap.xml 和 llms.txt 发现所有 URL"""

import re
import requests
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional
from urllib.parse import urlparse
from .utils import get_logger, retry_with_backoff

logger = get_logger(__name__)


class SitemapParser:
    """从 sitemap 和 llms.txt 发现所有 URL"""

    SITEMAP_INDEX = "https://jiekou.ai/sitemap.xml"
    DOCS_LLMS_TXT = "https://docs.jiekou.ai/llms.txt"

    def __init__(self):
        self.urls: List[Dict] = []
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (compatible; JiekouCrawler/1.0)"
        })

    @retry_with_backoff(max_retries=3, base_delay=2.0)
    def _fetch(self, url: str) -> str:
        """获取 URL 内容"""
        response = self.session.get(url, timeout=30)
        response.raise_for_status()
        return response.text

    def parse_sitemap_index(self) -> List[str]:
        """解析 sitemap 索引，获取子 sitemap URL"""
        logger.info(f"解析 sitemap 索引: {self.SITEMAP_INDEX}")
        try:
            content = self._fetch(self.SITEMAP_INDEX)
            root = ET.fromstring(content)

            # 处理 XML 命名空间
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

            sitemap_urls = []
            # 尝试作为 sitemap index 解析
            for sitemap in root.findall(".//sm:sitemap/sm:loc", ns):
                sitemap_urls.append(sitemap.text)

            # 如果没找到子 sitemap，可能是直接的 urlset
            if not sitemap_urls:
                for url in root.findall(".//sm:url/sm:loc", ns):
                    self.urls.append({
                        "url": url.text,
                        "source": "sitemap",
                        "category": self._categorize_url(url.text)
                    })
                logger.info(f"从主 sitemap 直接解析到 {len(self.urls)} 个 URL")
            else:
                logger.info(f"发现 {len(sitemap_urls)} 个子 sitemap")

            return sitemap_urls

        except Exception as e:
            logger.error(f"解析 sitemap 索引失败: {e}")
            return []

    def parse_sitemap_xml(self, sitemap_url: str) -> List[Dict]:
        """解析单个 sitemap.xml 文件"""
        logger.info(f"解析 sitemap: {sitemap_url}")
        try:
            content = self._fetch(sitemap_url)
            root = ET.fromstring(content)

            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

            urls = []
            for url_elem in root.findall(".//sm:url", ns):
                loc = url_elem.find("sm:loc", ns)
                if loc is not None and loc.text:
                    url_info = {
                        "url": loc.text,
                        "source": "sitemap",
                        "category": self._categorize_url(loc.text)
                    }

                    # 获取可选元素
                    lastmod = url_elem.find("sm:lastmod", ns)
                    if lastmod is not None:
                        url_info["lastmod"] = lastmod.text

                    priority = url_elem.find("sm:priority", ns)
                    if priority is not None:
                        url_info["priority"] = priority.text

                    urls.append(url_info)

            logger.info(f"从 {sitemap_url} 解析到 {len(urls)} 个 URL")
            return urls

        except Exception as e:
            logger.error(f"解析 sitemap {sitemap_url} 失败: {e}")
            return []

    def parse_llms_txt(self) -> List[Dict]:
        """解析 docs.jiekou.ai/llms.txt 获取文档 URL"""
        logger.info(f"解析 llms.txt: {self.DOCS_LLMS_TXT}")
        try:
            content = self._fetch(self.DOCS_LLMS_TXT)

            urls = []
            # 匹配格式: - [Title](url): description
            # 或: - [Title](url)
            pattern = r'-\s*\[([^\]]+)\]\(([^)]+)\)(?::\s*(.+))?'

            for match in re.finditer(pattern, content):
                title = match.group(1).strip()
                url = match.group(2).strip()
                description = match.group(3).strip() if match.group(3) else ""

                # 处理相对 URL
                if not url.startswith("http"):
                    url = f"https://docs.jiekou.ai{url}"

                urls.append({
                    "url": url,
                    "title": title,
                    "description": description,
                    "source": "llms.txt",
                    "category": self._categorize_url(url)
                })

            logger.info(f"从 llms.txt 解析到 {len(urls)} 个 URL")
            return urls

        except Exception as e:
            logger.error(f"解析 llms.txt 失败: {e}")
            return []

    def _categorize_url(self, url: str) -> Dict:
        """对 URL 进行分类"""
        parsed = urlparse(url)
        path = parsed.path

        if "docs.jiekou.ai" in parsed.netloc:
            # 文档页面
            category = "docs"
            # 提取子分类
            parts = path.strip("/").split("/")
            if len(parts) >= 2 and parts[0] == "docs":
                subcategory = parts[1] if len(parts) > 1 else "general"
            else:
                subcategory = "general"
            return {"type": category, "subcategory": subcategory}

        elif "/models/model-detail/" in path:
            # 模型详情页
            model_name = path.split("/")[-1]
            return {"type": "models", "model_name": model_name}

        elif "/legal/" in path:
            return {"type": "pages", "subcategory": "legal"}

        else:
            # 主站其他页面
            return {"type": "pages", "subcategory": "main"}

    def discover_all(self) -> List[Dict]:
        """发现所有 URL"""
        logger.info("开始发现所有 URL...")

        all_urls = []
        seen_urls = set()

        # 1. 解析 sitemap 索引
        sitemap_urls = self.parse_sitemap_index()

        # 如果有子 sitemap，逐个解析
        for sitemap_url in sitemap_urls:
            urls = self.parse_sitemap_xml(sitemap_url)
            for url_info in urls:
                if url_info["url"] not in seen_urls:
                    seen_urls.add(url_info["url"])
                    all_urls.append(url_info)

        # 添加从主 sitemap 直接解析的 URL
        for url_info in self.urls:
            if url_info["url"] not in seen_urls:
                seen_urls.add(url_info["url"])
                all_urls.append(url_info)

        # 2. 解析 llms.txt
        doc_urls = self.parse_llms_txt()
        for url_info in doc_urls:
            if url_info["url"] not in seen_urls:
                seen_urls.add(url_info["url"])
                all_urls.append(url_info)

        logger.info(f"总共发现 {len(all_urls)} 个唯一 URL")

        # 按类型统计
        stats = {}
        for url_info in all_urls:
            url_type = url_info["category"]["type"]
            stats[url_type] = stats.get(url_type, 0) + 1

        logger.info(f"URL 分布: {stats}")

        return all_urls
