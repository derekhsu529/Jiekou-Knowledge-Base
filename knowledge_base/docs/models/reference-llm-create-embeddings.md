---
title: "创建嵌入向量"
url: "https://docs.jiekou.ai/docs/models/reference-llm-create-embeddings.md"
crawled_at: "2026-02-26T23:33:29.932718"
---

Published Time: Thu, 26 Feb 2026 15:33:29 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 创建嵌入向量

创建一个表示输入文本的嵌入向量。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 要嵌入的输入文本，编码为字符串或 token 数组。要在单个请求中嵌入多个输入，请传递字符串数组或 token 数组。输入不得超过模型的最大输入 token（text-embedding-ada-002 为 8192 个 tokens），不能是空字符串，且任何数组的维度必须小于或等于 2048。 

 要使用的模型 ID。枚举值: * `baai/bge-m3` 

 返回嵌入向量的格式。可以是 float 或 base64。 

## Response

 固定为 list 

 模型生成的嵌入向量列表。   嵌入向量的索引。   嵌入向量。   固定为 embedding  

 使用的模型 ID。 

 使用信息。   prompt tokens 的数量。   总 tokens 的数量。
