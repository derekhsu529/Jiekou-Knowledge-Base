---
title: "Kling V2.6 Pro 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-v2.6-pro-t2v.md"
crawled_at: "2026-02-26T23:33:16.237000"
---

Published Time: Thu, 26 Feb 2026 15:33:16 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.6 Pro 文生视频

这是一个异步 API，仅返回异步任务的 `task_id`。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 是否在生成视频时同时生成音频。 

 生成视频的正向提示词文本；不可超过 2500 个字符。 

 生成媒体的持续时间（秒） 可选值：`5`, `10` 

 控制视频生成的灵活性，数值越高，模型生成内容对提示词的贴合度越高。 取值范围：\[0, 1] 

 生成视频的宽高比 可选值：`16:9`, `9:16`, `1:1` 

 反向提示词；长度不超过 2500 字符。 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
