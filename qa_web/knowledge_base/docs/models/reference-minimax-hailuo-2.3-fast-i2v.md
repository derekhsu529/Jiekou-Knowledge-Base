---
title: "Minimax Hailuo 2.3 Fast 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-minimax-hailuo-2.3-fast-i2v.md"
crawled_at: "2026-02-26T23:38:01.953481"
---

Published Time: Thu, 26 Feb 2026 15:38:01 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Minimax Hailuo 2.3 Fast 图生视频

Minimax Hailuo 2.3 Fast 在保持优异画质与表现力的同时，大幅提升了生成速度，具备更高性价比。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 指导生成所需的提示词文本。 范围: `1 <= x <= 2000`。 

 用于视频生成的图片。支持公网 URL 或 Base64 编码（如 `data:image/jpeg;base64,...`）。 

 生成视频的时长（秒）。默认值：`6`

 可选值：`6`、`10` 

 生成视频的分辨率。默认值：`768P` * 6 秒视频支持：`768P`、`1080P` * 10 秒视频仅支持：`768P` 

 是否启用提示词优化。 默认值: `true`。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
