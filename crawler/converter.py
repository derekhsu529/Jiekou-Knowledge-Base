"""使用 Jina Reader 将网页转换为 Markdown"""

import time
import requests
from typing import Optional, Dict
from .utils import get_logger, retry_with_backoff

logger = get_logger(__name__)


class JinaConverter:
    """使用 Jina Reader 将网页转换为 Markdown"""

    JINA_BASE = "https://r.jina.ai/"

    def __init__(self, rate_limit: float = 0.3):
        """
        Args:
            rate_limit: 请求之间的最小间隔（秒）
        """
        self.rate_limit = rate_limit
        self.last_request_time = 0
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        })

    def _respect_rate_limit(self):
        """确保请求之间有足够间隔"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit:
            time.sleep(self.rate_limit - elapsed)
        self.last_request_time = time.time()

    @retry_with_backoff(max_retries=3, base_delay=2.0)
    def convert(self, url: str) -> Dict:
        """
        将 URL 转换为 Markdown

        Args:
            url: 要转换的网页 URL

        Returns:
            {
                "url": 原始 URL,
                "markdown": 转换后的 Markdown 内容,
                "title": 提取的标题,
                "success": 是否成功
            }
        """
        self._respect_rate_limit()

        jina_url = f"{self.JINA_BASE}{url}"

        try:
            response = self.session.get(jina_url, timeout=60)

            if response.status_code == 200:
                markdown = response.text
                title = self._extract_title(markdown)

                # 清理 Markdown 内容
                markdown = self._clean_markdown(markdown)

                return {
                    "url": url,
                    "markdown": markdown,
                    "title": title,
                    "success": True
                }
            else:
                logger.warning(f"转换失败 {url}: HTTP {response.status_code}")
                return {
                    "url": url,
                    "success": False,
                    "error": f"HTTP {response.status_code}"
                }

        except requests.exceptions.Timeout:
            logger.warning(f"转换超时 {url}")
            return {"url": url, "success": False, "error": "Timeout"}

        except Exception as e:
            logger.warning(f"转换异常 {url}: {e}")
            return {"url": url, "success": False, "error": str(e)}

    def _extract_title(self, markdown: str) -> str:
        """从 Markdown 中提取标题（第一个 H1）"""
        lines = markdown.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
        return "Untitled"

    def _clean_markdown(self, markdown: str) -> str:
        """清理 Markdown 内容"""
        lines = markdown.split('\n')
        cleaned_lines = []

        for line in lines:
            # 移除 Jina Reader 可能添加的元数据行
            if line.startswith('Title:') or line.startswith('URL Source:'):
                continue
            if line.startswith('Markdown Content:'):
                continue
            cleaned_lines.append(line)

        # 移除开头的空行
        while cleaned_lines and not cleaned_lines[0].strip():
            cleaned_lines.pop(0)

        return '\n'.join(cleaned_lines)
