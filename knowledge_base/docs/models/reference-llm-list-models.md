---
title: "获取模型列表"
url: "https://docs.jiekou.ai/docs/models/reference-llm-list-models.md"
crawled_at: "2026-02-26T23:33:33.769077"
---

Published Time: Thu, 26 Feb 2026 11:22:37 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取模型列表

获取当前可用于 LLM API 的模型列表，并提供每个模型的基本信息。此 Endpoint 与 OpenAI API 兼容。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 响应

 包含以下属性的模型对象数组：   模型标识符，可在 API Endpoints 中引用。   模型创建时的 Unix 时间戳（以秒为单位）。   对象类型，始终为 "model"。   每百万输入 tokens 的价格。   每百万输出 tokens 的价格。   模型的标题。   模型的描述。   模型的最大上下文大小。
