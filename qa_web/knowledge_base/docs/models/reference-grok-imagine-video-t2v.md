---
title: "Grok Imagine Video 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-grok-imagine-video-t2v.md"
crawled_at: "2026-02-26T23:17:05.262236"
---

Published Time: Thu, 26 Feb 2026 15:17:05 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Grok Imagine Video 文生视频

这是一个异步 API，仅返回异步任务的 `task_id`。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 要生成的视频的文本描述。支持丰富、详细的提示词以生成高质量视频，涵盖电影场景、自然风光、角色动画等多种风格。 长度限制：1 - 4096 

 视频时长，单位为秒（1-15）。视频越长费用越高，按秒计费。 取值范围：\[1, 15] 

 输出视频分辨率。720p 画质更高，480p 生成更快。 可选值：`720p`, `480p` 

 生成视频的宽高比。常见用途：16:9/9:16 适用于宽屏和手机竖屏，4:3/3:4 适用于演示文稿和肖像，3:2/2:3 适用于摄影，1:1 适用于社交媒体。 可选值：`16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16` 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
