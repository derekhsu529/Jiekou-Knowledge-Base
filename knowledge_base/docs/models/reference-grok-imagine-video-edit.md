---
title: "Grok Imagine Video 视频编辑"
url: "https://docs.jiekou.ai/docs/models/reference-grok-imagine-video-edit.md"
crawled_at: "2026-02-26T23:32:35.928471"
---

Published Time: Thu, 26 Feb 2026 15:32:35 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Grok Imagine Video 视频编辑

这是一个异步 API，仅返回异步任务的 `task_id`。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 要编辑的输入视频 URL。视频将被缩放至最大 854x480 像素，并截断至 8 秒。输入时长上限为 8.7 秒，输出保留原始视频的时长。必须为可公开访问的 URL。 

 期望的编辑效果的文本描述。描述要应用到输入视频的风格变换或内容更改，例如「将视频改为动漫风格」或「使其看起来像水彩画」。 长度限制：1 - 4096 

 输出视频分辨率。480p 生成更快，720p 画质更高。输出分辨率匹配输入分辨率，最高不超过所选值。 可选值：`480p`, `720p` 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
