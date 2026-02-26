---
title: "Kling V2.1 Master 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-v2.1-t2v-master.md"
crawled_at: "2026-02-26T23:33:10.079782"
---

Published Time: Thu, 26 Feb 2026 15:33:09 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.1 Master 文生视频

Kling V2.1 文生视频是快手 AI 团队开发的最新一代文本生成视频模型，可根据输入文本一键生成高质量、电影级短视频。相比 Kling 2.0，2.1 版本在运动流畅性、画面一致性和提示词理解等方面实现了重大突破。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 指导生成的正向文本提示词。长度不超过 2500 字符。 

 生成视频的时长（秒）。 可选值：`5`、`10` 

 输出视频的宽高比。 可选值：`16:9`、`9:16`、`1:1` 

 指导强度参数，控制生成内容与提示词的贴合程度。 取值范围：0 到 1

 步长：0.1 

 反向提示词，用于规避不希望出现的内容；长度不超过 2500 字符。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
