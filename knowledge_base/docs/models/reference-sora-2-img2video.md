---
title: "OpenAI Sora 2 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-sora-2-img2video.md"
crawled_at: "2026-02-26T23:35:14.607439"
---

Published Time: Thu, 26 Feb 2026 15:35:14 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Sora 2 图生视频

OpenAI Sora 2 将单个参考图像转换为具有同步音频的连贯视频片段。基于 Sora 2 的核心进步，图像到视频的流程在合成可信的运动和摄像机动态的同时，保留了身份、光照和构图。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 视频生成的正面文本提示。 

 输入图像支持 URL 和 Base64 格式，支持的图像格式包括 .jpg、.jpeg、.png。 

 生成视频的分辨率。 枚举值： * professional 为 true（Pro 版）：`720p`, `1080p`。 * professional 为 false：`720p`。 默认：`720p`。 

 生成视频的时长（秒）。 枚举值：`4`、`8`、`12`。 默认：`4`。 

 该参数支持是否使用 Pro 版本。如果未提供，则默认值为 false。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
