"""数据库操作模块"""

import json
import aiosqlite
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from .config import DATABASE_PATH


async def init_db():
    """初始化数据库表"""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    async with aiosqlite.connect(DATABASE_PATH) as db:
        # 问答记录表
        await db.execute("""
            CREATE TABLE IF NOT EXISTS qa_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                matched_docs TEXT,
                response_time_ms INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 用户评价表
        await db.execute("""
            CREATE TABLE IF NOT EXISTS feedbacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                qa_id INTEGER NOT NULL,
                is_helpful BOOLEAN NOT NULL,
                feedback_text TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (qa_id) REFERENCES qa_records(id)
            )
        """)

        # 创建索引
        await db.execute("CREATE INDEX IF NOT EXISTS idx_qa_created_at ON qa_records(created_at)")
        await db.execute("CREATE INDEX IF NOT EXISTS idx_feedbacks_qa_id ON feedbacks(qa_id)")

        await db.commit()


async def save_qa_record(question: str, answer: str, matched_docs: List[Dict],
                         response_time_ms: int) -> int:
    """保存问答记录，返回记录 ID"""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute(
            """INSERT INTO qa_records (question, answer, matched_docs, response_time_ms)
               VALUES (?, ?, ?, ?)""",
            (question, answer, json.dumps(matched_docs, ensure_ascii=False), response_time_ms)
        )
        await db.commit()
        return cursor.lastrowid


async def save_feedback(qa_id: int, is_helpful: bool, feedback_text: Optional[str] = None) -> int:
    """保存用户评价，返回评价 ID"""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute(
            "INSERT INTO feedbacks (qa_id, is_helpful, feedback_text) VALUES (?, ?, ?)",
            (qa_id, is_helpful, feedback_text)
        )
        await db.commit()
        return cursor.lastrowid


async def delete_qa_record(qa_id: int) -> bool:
    """删除问答记录及其关联的评价"""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        # 先删除关联的评价
        await db.execute("DELETE FROM feedbacks WHERE qa_id = ?", (qa_id,))
        # 再删除问答记录
        cursor = await db.execute("DELETE FROM qa_records WHERE id = ?", (qa_id,))
        await db.commit()
        return cursor.rowcount > 0


async def get_qa_history(limit: int = 20, offset: int = 0) -> List[Dict]:
    """获取问答历史记录"""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute(
            """SELECT q.*,
                      (SELECT is_helpful FROM feedbacks WHERE qa_id = q.id ORDER BY id DESC LIMIT 1) as feedback,
                      (SELECT feedback_text FROM feedbacks WHERE qa_id = q.id ORDER BY id DESC LIMIT 1) as feedback_text
               FROM qa_records q
               ORDER BY q.created_at DESC
               LIMIT ? OFFSET ?""",
            (limit, offset)
        )
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]


async def get_stats_overview() -> Dict:
    """获取总体统计"""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        # 总问题数
        cursor = await db.execute("SELECT COUNT(*) FROM qa_records")
        total_questions = (await cursor.fetchone())[0]

        # 总评价数
        cursor = await db.execute("SELECT COUNT(*) FROM feedbacks")
        total_feedback = (await cursor.fetchone())[0]

        # 有用数
        cursor = await db.execute("SELECT COUNT(*) FROM feedbacks WHERE is_helpful = 1")
        helpful_count = (await cursor.fetchone())[0]

        # 没用数
        not_helpful_count = total_feedback - helpful_count

        # 有用率
        helpful_rate = (helpful_count / total_feedback * 100) if total_feedback > 0 else 0

        # 平均响应时间
        cursor = await db.execute("SELECT AVG(response_time_ms) FROM qa_records")
        avg_response_time = (await cursor.fetchone())[0] or 0

        return {
            "total_questions": total_questions,
            "total_feedback": total_feedback,
            "helpful_count": helpful_count,
            "not_helpful_count": not_helpful_count,
            "helpful_rate": round(helpful_rate, 1),
            "avg_response_time_ms": round(avg_response_time)
        }


async def get_daily_stats(days: int = 7) -> List[Dict]:
    """获取每日统计"""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        cursor = await db.execute("""
            SELECT
                DATE(q.created_at) as date,
                COUNT(q.id) as questions,
                SUM(CASE WHEN f.is_helpful = 1 THEN 1 ELSE 0 END) as helpful,
                SUM(CASE WHEN f.is_helpful = 0 THEN 1 ELSE 0 END) as not_helpful
            FROM qa_records q
            LEFT JOIN feedbacks f ON q.id = f.qa_id
            WHERE DATE(q.created_at) >= ?
            GROUP BY DATE(q.created_at)
            ORDER BY date DESC
        """, (start_date,))

        rows = await cursor.fetchall()
        return [{"date": row[0], "questions": row[1], "helpful": row[2] or 0, "not_helpful": row[3] or 0}
                for row in rows]


async def get_hot_questions(limit: int = 10) -> List[Dict]:
    """获取热门问题（简单实现：按问题出现次数）"""
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("""
            SELECT question, COUNT(*) as count, MAX(created_at) as last_asked
            FROM qa_records
            GROUP BY question
            ORDER BY count DESC, last_asked DESC
            LIMIT ?
        """, (limit,))

        rows = await cursor.fetchall()
        return [{"question": row[0], "count": row[1], "last_asked": row[2]} for row in rows]
