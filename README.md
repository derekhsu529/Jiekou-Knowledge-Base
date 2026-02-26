# Jiekou.ai 知识库爬虫

将 [jiekou.ai](https://jiekou.ai) 网站内容转换为 Markdown 知识库，用于智能问答助手。

## 功能特点

- 自动发现 URL（从 sitemap.xml 和 llms.txt）
- 使用 Jina Reader 将网页转换为 Markdown
- 断点续爬支持
- 智能问答测试（同义词扩展 + 全文搜索）

## 目录结构

```
Jiekou/
├── crawler/                    # 爬虫代码
│   ├── main.py                 # 主入口
│   ├── sitemap_parser.py       # URL 发现
│   ├── converter.py            # Jina Reader 转换
│   ├── file_manager.py         # 文件管理
│   └── progress_tracker.py     # 进度跟踪
├── knowledge_base/             # Markdown 知识库
│   ├── models/                 # 模型详情 (81个)
│   ├── docs/                   # API 文档 (204个)
│   └── pages/                  # 主站页面 (75个)
├── data/                       # 运行数据
│   └── urls.json               # 发现的 URL
├── test_qa.py                  # 问答测试脚本
└── requirements.txt
```

## 快速开始

### 安装

```bash
cd Jiekou
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 运行爬虫

```bash
# 完整爬取
python3 run.py

# 断点续爬
python3 run.py --resume

# 仅重试失败的
python3 run.py --retry-only
```

### 测试问答

```bash
# 设置 API Key
export PPIO_API_KEY="your-api-key"

# 运行测试
python3 test_qa.py
```

## 知识库统计

- 总文件数：360 个
- 模型文档：81 个
- API 文档：204 个
- 主站页面：75 个
- 总大小：约 1.8 MB

## 技术栈

- Python 3.x
- Jina Reader（网页转 Markdown）
- Anthropic Claude API（问答）
