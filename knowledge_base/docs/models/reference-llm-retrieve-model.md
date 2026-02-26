---
title: "获取指定模型信息"
url: "https://docs.jiekou.ai/docs/models/reference-llm-retrieve-model.md"
crawled_at: "2026-02-26T23:33:35.687623"
---

Published Time: Thu, 26 Feb 2026 05:01:49 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取指定模型信息

获取模型实例，提供有关模型的基本信息。此 Endpoint 与 OpenAI API 兼容。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 路径参数

 用于此请求的模型 ID。 

## 响应

 模型 ID，在 API Endpoints 中引用。 

 模型创建时的 Unix 时间戳（以秒为单位）。 

 对象类型，始终为 "model"。 

 每百万输入的 tokens 价格。 

 每百万输出 tokens 的价格。 

 模型的标题。 

 模型的描述。 

 模型的最大上下文大小。
