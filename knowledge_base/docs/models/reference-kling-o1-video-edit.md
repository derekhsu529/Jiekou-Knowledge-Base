---
title: "Kling-o1 视频编辑"
url: "https://docs.jiekou.ai/docs/models/reference-kling-o1-video-edit.md"
crawled_at: "2026-02-26T23:32:59.915727"
---

Published Time: Thu, 26 Feb 2026 15:32:59 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling-o1 视频编辑

这是一个异步 API，仅返回异步 task\_id。你需要使用 task\_id 调用任务结果查询 API 获取生成结果。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 视频URL 

 包含元素、场景、风格等的参考图片。最多4张 数组长度：0 - 4 

 生成的正向提示词 

 是否使用 fast 模式 

 生成视频的宽高比 可选值：`16:9`, `9:16`, `1:1` 

 选择是否通过参数保留视频原始声音 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
