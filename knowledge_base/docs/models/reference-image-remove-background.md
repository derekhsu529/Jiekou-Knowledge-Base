---
title: "图像背景移除"
url: "https://docs.jiekou.ai/docs/models/reference-image-remove-background.md"
crawled_at: "2026-02-26T23:37:45.814517"
---

Published Time: Thu, 26 Feb 2026 15:37:45 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 图像背景移除

这是一个异步 API，仅返回异步 task\_id。你需要使用 task\_id 调用任务结果查询 API 获取图像背景移除结果。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 要擦除背景的图像的URL。 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
