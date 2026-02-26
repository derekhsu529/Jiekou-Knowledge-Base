---
title: "OpenAI Sora 2 (reverse) 编辑视频"
url: "https://docs.jiekou.ai/docs/models/reference-sora-2-remix-reverse.md"
crawled_at: "2026-02-26T23:35:16.409818"
---

Published Time: Thu, 26 Feb 2026 15:35:16 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Sora 2 (reverse) 编辑视频

支持对 [OpenAI Sora 2 (reverse) 生成视频](/docs/models/reference-sora-2-video-reverse) 已生成的视频进行编辑，可保障一定的一致性。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 视频编辑的正面文本提示。 

 使用 [OpenAI Sora 2 (reverse) 生成视频](/docs/models/reference-sora-2-video-reverse) 生成视频返回的 task\_id。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
