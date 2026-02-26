#!/usr/bin/env python3
"""知识库问答测试 - 增强版搜索"""

import os
import json
import re
from pathlib import Path
from anthropic import Anthropic

BASE_DIR = Path(__file__).parent
KNOWLEDGE_BASE = BASE_DIR / "knowledge_base"

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


def expand_keywords(query: str) -> set:
    """扩展关键词，添加同义词"""
    query_lower = query.lower()
    keywords = set(query_lower.split())

    # 添加同义词
    expanded = set(keywords)
    for word in keywords:
        for key, synonyms in SYNONYMS.items():
            if word in key or key in word:
                expanded.update(synonyms)
            if word in synonyms:
                expanded.add(key)
                expanded.update(synonyms)

    return expanded


def search_in_content(content: str, keywords: set) -> int:
    """在文档内容中搜索关键词，返回匹配分数"""
    content_lower = content.lower()
    score = 0
    for kw in keywords:
        # 计算关键词出现次数（最多计 5 次）
        count = min(content_lower.count(kw), 5)
        score += count
    return score


def load_relevant_docs(query: str, max_docs: int = 8) -> str:
    """根据查询加载相关文档（增强版搜索）"""
    index_file = KNOWLEDGE_BASE / "_index.json"
    with open(index_file, encoding='utf-8') as f:
        index = json.load(f)

    # 扩展关键词
    keywords = expand_keywords(query)

    scored_docs = []
    for page in index["pages"]:
        title = page.get("title", "").lower()
        path = page.get("path", "").lower()

        # 标题和路径匹配（权重高）
        title_score = sum(3 for kw in keywords if kw in title)
        path_score = sum(2 for kw in keywords if kw in path)

        # 内容匹配（需要读取文件）
        doc_path = KNOWLEDGE_BASE / page["path"]
        content_score = 0
        if doc_path.exists():
            try:
                with open(doc_path, encoding='utf-8') as f:
                    content = f.read()
                    content_score = search_in_content(content, keywords)
            except:
                pass

        total_score = title_score + path_score + content_score
        if total_score > 0:
            scored_docs.append((total_score, page))

    # 按分数排序，取前 N 个
    scored_docs.sort(key=lambda x: x[0], reverse=True)
    top_docs = [doc for _, doc in scored_docs[:max_docs]]

    # 如果没有匹配，取一些默认文档
    if not top_docs:
        top_docs = index["pages"][:max_docs]

    # 加载文档内容
    contents = []
    for doc in top_docs:
        doc_path = KNOWLEDGE_BASE / doc["path"]
        if doc_path.exists():
            with open(doc_path, encoding='utf-8') as f:
                content = f.read()
                # 截取前 3000 字符
                contents.append(f"### {doc['title']}\nURL: {doc.get('url', '')}\n{content[:3000]}")

    return "\n\n---\n\n".join(contents)


def ask_question(question: str) -> str:
    """向知识库提问"""
    # 加载相关文档
    context = load_relevant_docs(question)

    # 调用 Claude API
    client = Anthropic(
        api_key=os.getenv("PPIO_API_KEY"),
        base_url="https://api.ppinfra.com/anthropic"
    )

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=2000,
        system="""你是接口AI (jiekou.ai) 的智能客服助手。

## 接口AI 核心信息
- **官网**：https://jiekou.ai
- **API 基础地址**：https://api.jiekou.ai/openai（兼容 OpenAI SDK 格式）
- **支持模型**：Claude、GPT、Gemini、Qwen、Llama 等 100+ 模型
- **文档**：https://docs.jiekou.ai

## 回答原则

### 1. 第三方工具集成问题（VSCode、Claude Code、Cursor 等）
当用户问"如何在 XXX 工具中使用接口AI的模型"时：
- 这类工具通常支持自定义 API 端点（Base URL）
- 配置方式：将 API Base URL 设置为 `https://api.jiekou.ai/openai`，填入接口AI的 API Key
- 模型名称使用接口AI提供的模型ID（如 `claude-opus-4-6`、`claude-sonnet-4-5-20250929`）

**VSCode Claude Code 配置示例：**
1. 设置环境变量或配置文件：
   - `ANTHROPIC_BASE_URL=https://api.jiekou.ai/anthropic`（Anthropic 格式）
   - 或 `OPENAI_BASE_URL=https://api.jiekou.ai/openai`（OpenAI 格式）
2. 设置 API Key 为接口AI的密钥
3. 模型名使用接口AI支持的名称

### 2. 模型相关问题
从知识库中查找模型的价格、参数、使用示例等信息。

### 3. API 调用问题
提供代码示例，强调使用接口AI的 base_url。

### 4. 其他问题
基于知识库内容回答，如无相关信息则诚实说明。""",
        messages=[
            {
                "role": "user",
                "content": f"""知识库内容：
{context}

用户问题：{question}"""
            }
        ]
    )

    return response.content[0].text


def main():
    print("=" * 50)
    print("接口AI 知识库问答测试（增强版）")
    print("输入 'q' 退出")
    print("=" * 50)

    while True:
        question = input("\n问题: ").strip()
        if question.lower() == 'q':
            break
        if not question:
            continue

        print("\n思考中...")
        try:
            answer = ask_question(question)
            print(f"\n回答: {answer}")
        except Exception as e:
            print(f"\n错误: {e}")


if __name__ == "__main__":
    main()
