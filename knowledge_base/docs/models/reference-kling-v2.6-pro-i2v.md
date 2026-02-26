---
title: "Kling V2.6 Pro 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-v2.6-pro-i2v.md"
crawled_at: "2026-02-26T23:33:11.992674"
---

Published Time: Thu, 26 Feb 2026 15:33:11 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.6 Pro 图生视频

这是一个异步 API，仅返回异步任务的 `task_id`。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 视频首帧图片；支持 `.jpg`、`.jpeg`、`.png`。 图片文件大小不得超过 10MB；宽高均需 >= 300px；宽高比需在 1:2.5 与 2.5:1 之间。 

 是否在生成视频时同时生成音频。 

 生成视频的正向提示词文本；不可超过 2500 个字符。 

 生成媒体的持续时间（秒） 可选值：`5`, `10` 

 控制视频生成的灵活性，数值越高，模型生成内容对提示词的贴合度越高。 取值范围：\[0, 1] 

 语音 ID 列表（最多 2 个）。 数组长度：0 - 2 

 生成视频的宽高比 可选值：`16:9`, `9:16`, `1:1` 

 反向提示词；长度不超过 2500 字符。 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
