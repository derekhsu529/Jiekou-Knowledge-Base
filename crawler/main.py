"""主爬虫入口"""

import argparse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict

from .sitemap_parser import SitemapParser
from .converter import JinaConverter
from .file_manager import FileManager
from .progress_tracker import ProgressTracker
from .utils import get_logger

# 项目根目录
BASE_DIR = "/Users/xuxian/Documents/DerekHsu/03_Code/ServiceDesk/Jiekou"

logger = get_logger(__name__, log_file=f"{BASE_DIR}/logs/crawler.log")


class JiekouCrawler:
    """Jiekou.ai 知识库爬虫"""

    def __init__(self, base_dir: str, concurrent: int = 3, rate_limit: float = 0.3):
        """
        Args:
            base_dir: 项目根目录
            concurrent: 并发数
            rate_limit: 请求间隔（秒）
        """
        self.base_dir = base_dir
        self.concurrent = concurrent

        self.parser = SitemapParser()
        self.converter = JinaConverter(rate_limit=rate_limit)
        self.file_manager = FileManager(base_dir)
        self.progress = ProgressTracker(f"{base_dir}/data")

    def discover_urls(self) -> List[Dict]:
        """阶段 1: 发现所有 URL"""
        logger.info("=" * 50)
        logger.info("阶段 1: 发现 URL")
        logger.info("=" * 50)

        urls = self.parser.discover_all()
        self.file_manager.save_urls(urls)
        self.progress.set_total(len(urls))

        return urls

    def crawl_single(self, url_info: Dict) -> bool:
        """爬取单个 URL"""
        url = url_info["url"]

        if self.progress.is_completed(url):
            return True

        result = self.converter.convert(url)

        if result and result["success"]:
            filepath = self.file_manager.url_to_filepath(url_info)
            self.file_manager.save_markdown(filepath, result["markdown"], {
                "title": url_info.get("title") or result["title"],
                "url": url,
                "crawled_at": datetime.now().isoformat()
            })
            self.progress.mark_completed(url)
            logger.info(f"[OK] {filepath.name}")
            return True
        else:
            error = result.get("error", "Unknown error") if result else "No response"
            self.progress.mark_failed(url, error)
            logger.warning(f"[FAIL] {url}: {error}")
            return False

    def crawl_all(self, urls: List[Dict]):
        """阶段 2: 爬取所有 URL"""
        logger.info("=" * 50)
        logger.info("阶段 2: 爬取页面")
        logger.info("=" * 50)

        url_map = {u["url"]: u for u in urls}
        pending_urls = self.progress.get_pending(list(url_map.keys()))

        if not pending_urls:
            logger.info("没有待处理的 URL")
            return

        logger.info(f"待爬取: {len(pending_urls)} 个 URL (并发={self.concurrent})")
        self.progress.start_session()

        completed_count = 0
        total = len(pending_urls)

        with ThreadPoolExecutor(max_workers=self.concurrent) as executor:
            futures = {
                executor.submit(self.crawl_single, url_map[url]): url
                for url in pending_urls
            }

            for future in as_completed(futures):
                url = futures[future]
                try:
                    success = future.result()
                    completed_count += 1

                    # 每 20 个打印进度
                    if completed_count % 20 == 0:
                        logger.info(f"进度: {completed_count}/{total} ({completed_count/total*100:.1f}%)")

                except Exception as e:
                    logger.error(f"爬取异常 {url}: {e}")

    def retry_failed(self):
        """阶段 3: 重试失败的 URL"""
        retryable = self.progress.get_retryable(max_attempts=3)

        if not retryable:
            logger.info("没有需要重试的 URL")
            return

        logger.info("=" * 50)
        logger.info(f"阶段 3: 重试 {len(retryable)} 个失败的 URL")
        logger.info("=" * 50)

        # 加载 URL 信息
        urls = self.file_manager.load_urls()
        url_map = {u["url"]: u for u in urls}

        for url in retryable:
            if url in url_map:
                self.crawl_single(url_map[url])

    def build_index(self):
        """阶段 4: 构建索引"""
        logger.info("=" * 50)
        logger.info("阶段 4: 构建索引")
        logger.info("=" * 50)

        index = self.file_manager.build_index()
        return index

    def run(self, skip_discovery: bool = False, retry_only: bool = False):
        """运行完整爬取流程"""
        start_time = datetime.now()
        logger.info("=" * 50)
        logger.info("Jiekou.ai 知识库爬虫")
        logger.info(f"开始时间: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("=" * 50)

        if retry_only:
            self.retry_failed()
        else:
            # 阶段 1: 发现 URL
            if skip_discovery:
                urls = self.file_manager.load_urls()
                self.progress.set_total(len(urls))
            else:
                urls = self.discover_urls()

            # 阶段 2: 爬取
            self.crawl_all(urls)

            # 阶段 3: 重试
            self.retry_failed()

        # 阶段 4: 构建索引
        self.build_index()

        # 完成
        self.progress.finish()

        end_time = datetime.now()
        duration = end_time - start_time

        logger.info("=" * 50)
        logger.info("爬取完成!")
        logger.info(f"耗时: {duration}")
        logger.info(self.progress.get_summary())
        logger.info("=" * 50)


def main():
    parser = argparse.ArgumentParser(description="Jiekou.ai 知识库爬虫")
    parser.add_argument(
        "--resume", "-r",
        action="store_true",
        help="断点续爬（跳过 URL 发现）"
    )
    parser.add_argument(
        "--retry-only",
        action="store_true",
        help="仅重试失败的 URL"
    )
    parser.add_argument(
        "--concurrent", "-c",
        type=int,
        default=3,
        help="并发数 (默认: 3)"
    )
    parser.add_argument(
        "--rate-limit",
        type=float,
        default=0.3,
        help="请求间隔秒数 (默认: 0.3)"
    )

    args = parser.parse_args()

    crawler = JiekouCrawler(
        base_dir=BASE_DIR,
        concurrent=args.concurrent,
        rate_limit=args.rate_limit
    )

    crawler.run(
        skip_discovery=args.resume,
        retry_only=args.retry_only
    )


if __name__ == "__main__":
    main()
