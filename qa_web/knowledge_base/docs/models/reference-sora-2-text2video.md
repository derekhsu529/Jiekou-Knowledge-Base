---
title: "OpenAI Sora 2 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-sora-2-text2video.md"
crawled_at: "2026-02-26T23:35:18.542304"
---

Published Time: Thu, 26 Feb 2026 15:35:18 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Sora 2 文生视频

OpenAI Sora 2 是一款最先进的视频+音频生成器。它在原有 Sora 基础上进行了改进，具备更精确的物理效果、更清晰的真实感、同步的音频、更强的可操控性以及更广泛的风格范围。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 视频生成的正面文本提示。 

 生成视频的像素大小（宽度\*高度）。 枚举值： * professional 为 true（Pro 版）：`720*1280`、`1280*720`、`1024*1792`、`1792*1024`。 * professional 为 false： `720*1280`、`1280*720`。 默认：`720*1280`。 

 生成视频的时长（秒）。 枚举值：`4`、`8`、`12`。 默认：`4`。 

 该参数支持是否使用 Pro 版本。如果未提供，则默认值为 false。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
