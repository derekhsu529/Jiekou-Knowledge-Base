---
title: "Kling V2.6 Pro 动作控制"
url: "https://docs.jiekou.ai/docs/models/reference-kling-v2.6-pro-motion-control.md"
crawled_at: "2026-02-26T23:33:14.002407"
---

Published Time: Thu, 26 Feb 2026 15:33:13 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.6 Pro 动作控制

这是一个异步 API，仅返回异步任务的 `task_id`。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 参考图像 URL 或 base64 编码图像；支持 `.jpg`、`.jpeg`、`.png`。 图片文件大小不得超过 10MB；宽高均需 >= 300px；宽高比需在 1:2.5 与 2.5:1 之间。 

 参考运动视频 URL；支持 `.mp4`、`.mov`。 视频文件大小不得超过 10MB；宽高均需 >= 300px；时长 3-30 秒。 

 场景描述、风格、光线等正向提示词。 

 反向提示词；长度不超过 2500 字符。 

 是否保留参考视频的原始音频。 

 输出帧模式： * `image`：匹配参考图像的取景（输出 5 秒） * `video`：匹配参考视频的取景（最长 30 秒） 可选值：`image`, `video` 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
