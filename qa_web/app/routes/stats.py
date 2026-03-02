"""统计 API 路由"""

from typing import List
from fastapi import APIRouter, Query
from ..models import StatsOverview, DailyStat, HotQuestion
from ..database import get_stats_overview, get_daily_stats, get_hot_questions
from ..config import TAVILY_ENABLED, TAVILY_API_KEY, TAVILY_MAX_RESULTS

router = APIRouter()


@router.get("/overview", response_model=StatsOverview)
async def stats_overview():
    """获取总体统计"""
    stats = await get_stats_overview()
    return StatsOverview(**stats)


@router.get("/daily", response_model=List[DailyStat])
async def stats_daily(days: int = Query(7, ge=1, le=90)):
    """获取每日统计"""
    stats = await get_daily_stats(days=days)
    return [DailyStat(**s) for s in stats]


@router.get("/hot_questions", response_model=List[HotQuestion])
async def hot_questions(limit: int = Query(10, ge=1, le=100)):
    """获取热门问题"""
    questions = await get_hot_questions(limit=limit)
    return [HotQuestion(**q) for q in questions]


@router.get("/config")
async def get_config():
    """获取系统配置状态（用于调试）"""
    return {
        "tavily_enabled": TAVILY_ENABLED,
        "tavily_api_key_configured": bool(TAVILY_API_KEY),
        "tavily_api_key_length": len(TAVILY_API_KEY) if TAVILY_API_KEY else 0,
        "tavily_max_results": TAVILY_MAX_RESULTS
    }
