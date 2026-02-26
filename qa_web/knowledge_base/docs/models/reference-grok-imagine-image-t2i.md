---
title: "Grok Imagine Image 文生图"
url: "https://docs.jiekou.ai/docs/models/reference-grok-imagine-image-t2i.md"
crawled_at: "2026-02-26T23:32:33.862898"
---

Published Time: Thu, 26 Feb 2026 15:32:33 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Grok Imagine Image 文生图

这是一个异步 API，仅返回异步任务的 `task_id`。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 要生成的图片的文本描述。模型支持丰富、详细的提示词以生成高质量图片，支持多种视觉风格，包括超写实摄影、动漫、油画、铅笔素描等。 长度限制：1 - 无限制 

 每次请求生成的图片数量（1-4）。按张计费。 取值范围：\[1, 4] 

 生成图片的宽高比。常见用途：1:1 适用于社交媒体和缩略图，16:9/9:16 适用于宽屏和手机竖屏，4:3/3:4 适用于演示文稿和肖像，3:2/2:3 适用于摄影，2:1/1:2 适用于横幅和标题图，20:9/9:20 适用于超宽屏显示。 可选值：`2:1`, `20:9`, `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`, `9:20`, `1:2` 

 输出图片格式。 可选值：`jpeg`, `png` 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
