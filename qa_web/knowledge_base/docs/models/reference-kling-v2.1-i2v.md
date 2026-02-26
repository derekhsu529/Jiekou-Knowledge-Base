---
title: "Kling V2.1 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-v2.1-i2v.md"
crawled_at: "2026-02-26T23:33:05.899990"
---

Published Time: Thu, 26 Feb 2026 15:33:05 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.1 图生视频

Kling V2.1 是快手团队最新一代 AI 驱动的图生视频模型，可通过一张图片或文本提示一键生成高质量、电影级短视频。相比 Kling 2.0，2.1 版本在运动流畅性、画面一致性和提示词理解等方面有重大突破。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 视频的首帧图片。支持的图片格式包括 `.jpg`、`.jpeg`、`.png`。图片文件大小不超过 10MB，分辨率不低于 300×300 像素。 

 生成视频的正向文本提示，不超过 2500 个字符。 

 视频生成模式。 支持： * `Standard`：快速生成，低成本，生成 720p 视频。 * `Professional`：高质量，高成本，生成 1080p 视频。 默认值：`Standard`。 

 生成视频的时长（秒）。 可选值：`5`、`10` 

 指导强度参数，控制生成内容与提示词的贴合程度。 取值范围：0 到 1

 步长：0.01 

 反向提示词，用于规避不希望出现的内容；长度不超过 2500 字符。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
