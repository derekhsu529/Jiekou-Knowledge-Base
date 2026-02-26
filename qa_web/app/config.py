"""配置模块"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# 项目路径
BASE_DIR = Path(__file__).parent.parent
PROJECT_ROOT = BASE_DIR.parent
KNOWLEDGE_BASE_DIR = PROJECT_ROOT / "knowledge_base"

# 数据库
DATABASE_PATH = BASE_DIR / "data" / "qa.db"

# AI API 配置
PPIO_API_KEY = os.getenv("PPIO_API_KEY", "")
ANTHROPIC_BASE_URL = os.getenv("ANTHROPIC_BASE_URL", "https://api.ppinfra.com/anthropic")
AI_MODEL = os.getenv("AI_MODEL", "claude-sonnet-4-5-20250929")

# 服务器配置
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8080"))
