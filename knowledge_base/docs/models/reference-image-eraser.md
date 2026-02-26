---
title: "图像擦除"
url: "https://docs.jiekou.ai/docs/models/reference-image-eraser.md"
crawled_at: "2026-02-26T23:37:43.816149"
---

Published Time: Thu, 26 Feb 2026 15:37:43 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 图像擦除

这是一个异步 API，仅返回异步 task\_id。你需要使用 task\_id 调用任务结果查询 API 获取图像擦除结果。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 遮罩图像，用于指示要擦除的区域。要擦除的区域应为白色，要保留的区域应为黑色。 

 要生成图像的原始图像。 

 用于指定要从图像中移除的对象或区域的文本提示。例如：'dog' 或 'hat'。 

 输出图像的格式。 可选值：`jpeg`, `png`, `webp` 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
