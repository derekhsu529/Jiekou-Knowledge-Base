---
title: "Kling V3.0 Pro 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-v3.0-pro-t2v.md"
crawled_at: "2026-02-26T23:33:20.432196"
---

Published Time: Thu, 26 Feb 2026 15:33:20 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3.0 Pro 文生视频

这是一个异步 API，仅返回异步任务的 `task_id`。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 是否同步生成音频。 

 视频场景和运动的文本描述。 

 视频时长（秒），范围 3-15。 可选值：`3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15` 

 视频生成灵活度。较低值允许更多创意自由，较高值更忠实于提示词。 取值范围：\[0, 1] 

 输出视频宽高比。 可选值：`16:9`, `9:16`, `1:1` 

 多镜头提示词列表，用于多镜头视频生成。 

 需要从生成结果中排除的元素。 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
