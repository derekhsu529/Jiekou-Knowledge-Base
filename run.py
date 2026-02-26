#!/usr/bin/env python
"""简单运行脚本"""

import sys
from pathlib import Path

# 添加项目路径
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

from crawler.main import main

if __name__ == "__main__":
    main()
