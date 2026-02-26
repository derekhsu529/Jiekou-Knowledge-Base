---
title: "API 配置与技术接入"
url: "https://docs.jiekou.ai/docs/support/faq_api.md"
crawled_at: "2026-02-26T23:36:59.722687"
---

Published Time: Thu, 26 Feb 2026 15:36:59 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# API 配置与技术接入

## 1. API 基础 URL 应该填什么？

根据协议不同，主要有以下几种：

* OpenAI 兼容格式：[https://api.jiekou.ai/openai](https://api.jiekou.ai/openai) 或 [https://api.jiekou.ai/openai/v1/chat/completions](https://api.jiekou.ai/openai/v1/chat/completions)
* Anthropic 原生协议：[https://api.jiekou.ai/anthropic](https://api.jiekou.ai/anthropic) （用于 Claude Code 等工具）
* 生图/生视频专用：[https://api.jiekou.ai/v3/](https://api.jiekou.ai/v3/) （如 Gemini、Nano Banana 等）

注意：如遇到 404 错误，请检查 URL 末尾是否多写了 /v1，不同工具对路径拼接逻辑不同。

## 2. 调用时返回 401 "无效令牌" 怎么办？

1. 确认 API Key 已正确创建：[https://jiekou.ai/settings/key-management](https://jiekou.ai/settings/key-management)
2. 确认请求头中 Authorization 格式为：Bearer sk\_xxxxxx
3. 如使用 Claude Code，环境变量应设置为 ANTHROPIC\_AUTH\_TOKEN=sk\_xxxxx（不需要加 Bearer 前缀，工具会自动添加）

## 3. 调用返回 404 "page not found" 怎么排查？

常见原因：

* URL 错误：如使用了 /v3/glm-asr 却拼写错误
* 模型路由错误：如 Codex 模型需要使用 /v1/responses 而非 /v1/chat/completions
* 工具自动拼接问题：部分工具（如 cc-switch）会自动添加 /chat/completions，此时 Base URL 不应包含该路径

## 4. 如何在 Claude Code 中配置 Jiekou.AI？

环境变量配置如下：

Windows cmd：

```
set ANTHROPIC_BASE_URL=https://api.jiekou.ai/anthropic
set ANTHROPIC_AUTH_TOKEN=sk_您的API密钥
set ANTHROPIC_MODEL=claude-opus-4-1-20250805
set ANTHROPIC_SMALL_FAST_MODEL=claude-sonnet-4-20250514
```

Mac/Linux bash：

```
export ANTHROPIC_BASE_URL=https://api.jiekou.ai/anthropic
export ANTHROPIC_AUTH_TOKEN=sk_您的API密钥
export ANTHROPIC_MODEL=claude-opus-4-1-20250805
export ANTHROPIC_SMALL_FAST_MODEL=claude-sonnet-4-20250514
```

参考文档：[https://docs.jiekou.ai/docs/integration/claudecode](https://docs.jiekou.ai/docs/integration/claudecode)

## 5. Claude Code 提示强制登录/需要验证怎么解决？

最新版 Claude Code 可能强制要求登录。解决方案：

* 使用 Cline 插件替代（VSCode 插件市场搜索）
* 或配合 cc-switch 等转发工具使用

## 6. GPT-5.1 / Codex 模型如何调用？为什么返回 400 错误？

GPT-5.1 系列（包括 Codex）需要使用 OpenAI 的 Responses API，而非 Chat Completions：

```
curl "https://api.jiekou.ai/openai/v1/responses" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer " \ -d '{ "model": "gpt-5.1-codex", "input": [...], "max_output_tokens": 64000 }' ``` ## 7. Claude 4.5 返回 "thinking block" 相关错误怎么办？ 错误通常提示：Expected 'thinking' or 'redacted\_thinking', but found 'text'。这是因为 Claude 4.5 启用 Thinking 功能后，要求上下文必须包含特定的思考块格式。建议： * 清除对话历史重新开始 * 或禁用 Thinking 功能（如不需要） * 使用原生 Anthropic 协议而非 OpenAI 兼容协议（后者对 Thinking 支持可能不完整） ## 8. 调用 Claude API 返回 "输入过长" 错误？ Claude 模型对输入长度有限制（通常 max\_tokens 最大支持 64000）。请检查： * 输入文本长度 * Base64 图片的大小（过大图片建议先压缩） * 历史对话上下文累积长度 *** **联系支持** 如以上 FAQ 无法解决您的问题，请通过以下方式联系技术支持： * 企业微信/微信技术支持群（推荐，响应最快） * 提供信息格式： * 问题描述 + 截图 * 账号 ID (UUID) * Trace ID（如有，通常在错误信息中） * 请求参数（脱敏后）
