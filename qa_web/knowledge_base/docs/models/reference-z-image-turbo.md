---
title: "Z Image 文生图 Turbo"
url: "https://docs.jiekou.ai/docs/models/reference-z-image-turbo.md"
crawled_at: "2026-02-26T23:36:42.865341"
---

Published Time: Thu, 26 Feb 2026 15:36:42 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Z Image 文生图 Turbo

这是一个异步 API，仅返回异步 task\_id。你需要使用 task\_id 调用任务结果查询 API 获取生成结果。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 生成的随机种子。-1 表示使用随机种子。范围：-1 到 2147483647 取值范围：\[-1, 2147483647] 

 生成图像的像素尺寸（宽\*高）。每个维度范围为 256 到 1536 像素 

 生成的正向提示词 

 如果启用，输出将编码为 BASE64 字符串而不是 URL。此属性仅通过 API 可用 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
