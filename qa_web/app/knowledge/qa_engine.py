"""问答引擎 - Claude API 集成"""

from anthropic import Anthropic
from ..config import API_KEY, ANTHROPIC_BASE_URL, AI_MODEL

# 系统提示词
SYSTEM_PROMPT = """你是接口AI (jiekou.ai) 的智能客服助手。

## 重要限制（必须遵守）
- **绝对禁止**在回答中提及以下名称：PPIO、Novita、ppinfra
- 如果知识库内容中包含这些名称，必须自动替换为"接口AI"或直接省略
- 只宣传"接口AI"品牌，不透露任何底层服务提供商信息

## 接口AI 核心信息
- **官网**：https://jiekou.ai
- **API 基础地址**：https://api.jiekou.ai/openai（兼容 OpenAI SDK 格式）
- **支持模型**：Claude、GPT、Gemini、Qwen、Llama 等 100+ 模型
- **文档**：https://docs.jiekou.ai

## 可用图片资源（在相关回答中使用 Markdown 图片语法插入）
当回答涉及以下内容时，请在文字后面插入对应图片：

- **联系方式/客服/微信**：`![联系二维码](https://wild-sunset-4e17.super-8d8.workers.dev/assets/GvxnaY4YtYxAjr7CrW293MqZISuknDlc.jpg)`

示例：当用户问"怎么联系客服"时，回答应包含：
> 您可以通过微信联系我们：
> ![联系二维码](https://wild-sunset-4e17.super-8d8.workers.dev/assets/GvxnaY4YtYxAjr7CrW293MqZISuknDlc.jpg)

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
        api_key=API_KEY,
        base_url=ANTHROPIC_BASE_URL
    )


def generate_answer(question: str, context: str, image_base64: str = None) -> str:
    """
    使用 Claude API 生成回答，支持多模态输入

    Args:
        question: 用户问题
        context: 知识库上下文
        image_base64: 可选的 base64 编码图片

    Returns:
        AI 生成的回答
    """
    client = _get_client()

    # 构建消息内容
    content = []

    # 如果有图片，添加图片
    if image_base64:
        # 从 data:image/png;base64,xxx 提取
        if ',' in image_base64:
            media_type = image_base64.split(';')[0].split(':')[1]
            data = image_base64.split(',')[1]
        else:
            media_type = "image/png"
            data = image_base64

        content.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": media_type,
                "data": data
            }
        })

    # 添加文本
    content.append({
        "type": "text",
        "text": f"知识库内容：\n{context}\n\n用户问题：{question}"
    })

    response = client.messages.create(
        model=AI_MODEL,
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": content}]
    )

    return response.content[0].text
