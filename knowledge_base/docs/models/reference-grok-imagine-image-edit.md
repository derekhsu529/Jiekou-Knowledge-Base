---
title: "Grok Imagine Image 图片编辑"
url: "https://docs.jiekou.ai/docs/models/reference-grok-imagine-image-edit.md"
crawled_at: "2026-02-26T23:32:32.038263"
---

Published Time: Thu, 26 Feb 2026 15:32:31 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Grok Imagine Image 图片编辑

这是一个异步 API，仅返回异步任务的 `task_id`。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 要编辑的源图片，以公开 URL 或 base64 数据 URI（例如 "data:image/jpeg;base64,..."）提供。模型会分析图片内容并应用所请求的编辑。 

 描述对源图片所需编辑的文本指令。模型能理解图片内容并进行修改，包括风格迁移、物体修改、场景更改以及迭代优化。 长度限制：1 - 无限制 

 每次请求生成的编辑图片数量（1-4）。按张计费。 取值范围：\[1, 4] 

 输出图片格式。 可选值：`jpeg`, `png` 

 启用 NSFW 内容安全检查器。 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
