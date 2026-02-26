"""爬取进度跟踪，支持断点续爬"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set
from .utils import get_logger

logger = get_logger(__name__)


class ProgressTracker:
    """跟踪和持久化爬取进度"""

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.progress_file = self.data_dir / "progress.json"
        self.errors_file = self.data_dir / "errors.json"

        self.completed: Set[str] = set()
        self.failed: Dict[str, Dict] = {}
        self.stats = {
            "total": 0,
            "completed": 0,
            "failed": 0,
            "started_at": None,
            "last_updated": None
        }

        self._load()

    def _load(self):
        """从磁盘加载进度"""
        if self.progress_file.exists():
            try:
                data = json.loads(self.progress_file.read_text(encoding='utf-8'))
                self.completed = set(data.get("completed", []))
                self.stats = data.get("stats", self.stats)
                logger.info(f"加载进度: {len(self.completed)} 个已完成")
            except Exception as e:
                logger.warning(f"加载进度文件失败: {e}")

        if self.errors_file.exists():
            try:
                self.failed = json.loads(self.errors_file.read_text(encoding='utf-8'))
                logger.info(f"加载错误记录: {len(self.failed)} 个失败")
            except Exception as e:
                logger.warning(f"加载错误文件失败: {e}")

    def _save(self):
        """持久化进度到磁盘"""
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.stats["last_updated"] = datetime.now().isoformat()
        self.stats["completed"] = len(self.completed)
        self.stats["failed"] = len(self.failed)

        # 保存进度
        self.progress_file.write_text(
            json.dumps({
                "completed": list(self.completed),
                "stats": self.stats
            }, ensure_ascii=False, indent=2),
            encoding='utf-8'
        )

        # 保存错误记录
        self.errors_file.write_text(
            json.dumps(self.failed, ensure_ascii=False, indent=2),
            encoding='utf-8'
        )

    def is_completed(self, url: str) -> bool:
        """检查 URL 是否已成功爬取"""
        return url in self.completed

    def mark_completed(self, url: str):
        """标记 URL 为已完成"""
        self.completed.add(url)

        # 如果之前失败过，从失败列表移除
        if url in self.failed:
            del self.failed[url]

        # 每 10 个保存一次
        if len(self.completed) % 10 == 0:
            self._save()

    def mark_failed(self, url: str, error: str):
        """记录失败的 URL"""
        self.failed[url] = {
            "error": error,
            "attempts": self.failed.get(url, {}).get("attempts", 0) + 1,
            "last_attempt": datetime.now().isoformat()
        }
        self._save()

    def get_pending(self, all_urls: List[str]) -> List[str]:
        """获取未完成的 URL"""
        return [url for url in all_urls if url not in self.completed]

    def get_retryable(self, max_attempts: int = 3) -> List[str]:
        """获取可重试的失败 URL"""
        return [
            url for url, info in self.failed.items()
            if info["attempts"] < max_attempts
        ]

    def set_total(self, total: int):
        """设置总 URL 数"""
        self.stats["total"] = total

    def start_session(self):
        """开始新的爬取会话"""
        if not self.stats["started_at"]:
            self.stats["started_at"] = datetime.now().isoformat()

    def finish(self):
        """完成爬取，保存最终进度"""
        self._save()

    def get_summary(self) -> str:
        """获取进度摘要"""
        total = self.stats["total"]
        completed = len(self.completed)
        failed = len(self.failed)
        pending = total - completed

        return (
            f"进度: {completed}/{total} ({completed/total*100:.1f}%)\n"
            f"  - 已完成: {completed}\n"
            f"  - 待处理: {pending}\n"
            f"  - 失败: {failed}"
        )
