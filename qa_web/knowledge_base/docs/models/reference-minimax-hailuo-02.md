---
title: "Minimax Hailuo-02"
url: "https://docs.jiekou.ai/docs/models/reference-minimax-hailuo-02.md"
crawled_at: "2026-02-26T23:37:59.454821"
---

Published Time: Thu, 26 Feb 2026 04:56:18 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Minimax Hailuo-02

Minimax Hailuo-02 是一款支持文本生成视频和图片生成视频的 AI 视频生成模型。它可以生成 6 秒的 768P 或 1080P 分辨率视频，以及 10 秒的 768P 分辨率视频。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 指导生成所需的提示词文本。 范围: `1 <= x <= 2000`。 

 用于视频生成的首帧图片。支持公网 URL 或 Base64 编码（如 `data:image/jpeg;base64,...`）。 

 用于视频生成的结束帧图片。支持公网 URL 或 Base64 编码（如 `data:image/jpeg;base64,...`）。 

 生成视频的时长（秒）。默认值：`6`

 可选值：`6`、`10` 

 生成视频的分辨率。默认值：`768P` * 6 秒视频支持：`768P`、`1080P` * 10 秒视频仅支持：`768P` 

 是否启用提示词优化。 默认值: `true`。 

 是否缩短提示词优化的耗时。 默认值: `false`。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
