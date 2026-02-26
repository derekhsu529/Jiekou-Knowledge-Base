---
title: "创建重排序"
url: "https://docs.jiekou.ai/docs/models/reference-llm-create-rerank.md"
crawled_at: "2026-02-26T23:33:32.032081"
---

Published Time: Thu, 26 Feb 2026 15:33:31 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 创建重排序

创建重排序

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 要使用的模型名称。 

 搜索查询。 

 文档列表。 

 返回的最相关文档或索引的数量。 

## 响应

 ID 

   原始文档内容。      输入候选文档数组中位置的索引值。   相似度分数。  

 Tokens 使用统计。   生成的完成中的 tokens 数量。   提示中的 tokens 数量。   请求中使用的 tokens 总数（prompt + completion）。
