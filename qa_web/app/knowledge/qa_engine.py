"""问答引擎 - Claude API 集成"""

from anthropic import Anthropic
from ..config import PPIO_API_KEY, ANTHROPIC_BASE_URL, AI_MODEL

# 系统提示词
SYSTEM_PROMPT = """你是接口AI (jiekou.ai) 的智能客服助手。

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
基于知识库内容回答，如无相关信息则诚实说明。"""


def _get_client() -> Anthropic:
    """获取 Anthropic 客户端"""
    return Anthropic(
        api_key=PPIO_API_KEY,
        base_url=ANTHROPIC_BASE_URL
    )


def generate_answer(question: str, context: str) -> str:
    """
    使用 Claude API 生成回答

    Args:
        question: 用户问题
        context: 知识库上下文

    Returns:
        AI 生成的回答
    """
    client = _get_client()

    response = client.messages.create(
        model=AI_MODEL,
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"知识库内容：\n{context}\n\n用户问题：{question}"
            }
        ]
    )

    return response.content[0].text
