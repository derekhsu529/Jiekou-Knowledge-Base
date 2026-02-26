---
title: "KLING V1.6 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-v1.6-t2v.md"
crawled_at: "2026-02-26T23:33:03.661121"
---

Published Time: Thu, 26 Feb 2026 05:02:22 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# KLING V1.6 文生视频

KLING V1.6 文生视频是快手 AI 团队开发的 AI 文本生成视频模型。它可将文本描述转化为动态的 5 秒 720p 视频，具备高质量视觉输出、增强的运动与语义理解能力。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 视频生成模式。 支持： * `Standard`：快速生成，成本较低，生成 720p 视频。 默认值：`Standard`。 

 指导生成所需的提示词文本。 取值范围：`1 <= x <= 2000`。 

 负面提示词，用于指示模型应避免生成的内容。 取值范围：`0 <= x <= 2000`。 

 生成视频的时长（秒）。默认值：`5`。

 可选值：`5`、`10` 

 指导强度参数，控制生成内容与提示词的贴合程度。 取值范围：`0 <= x <= 1`。默认值：`0.5`。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
