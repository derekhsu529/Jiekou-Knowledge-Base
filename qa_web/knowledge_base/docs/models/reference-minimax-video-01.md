---
title: "Minimax Video-01"
url: "https://docs.jiekou.ai/docs/models/reference-minimax-video-01.md"
crawled_at: "2026-02-26T23:34:17.828346"
---

Published Time: Thu, 26 Feb 2026 04:59:36 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Minimax Video-01

Minimax Video-01（又名海螺）是一款 AI 视频生成模型，可生成 6 秒、720p 分辨率、25 帧/秒的视频。支持文本生成视频（文生视频）和图片生成视频（图生视频）两种模式。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 指导生成所需的提示词文本。 取值范围：`1 <= x <= 2000`。 

 用于视频生成的首帧图片的 URL。 

 是否启用提示词优化。 默认值：`true`。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
