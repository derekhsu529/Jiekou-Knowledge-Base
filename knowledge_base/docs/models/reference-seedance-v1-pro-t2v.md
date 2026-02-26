---
title: "Seedance V1 Pro 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-seedance-v1-pro-t2v.md"
crawled_at: "2026-02-26T23:35:00.092822"
---

Published Time: Thu, 26 Feb 2026 04:55:46 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedance V1 Pro 文生视频

Seedance V1 Pro 是一个 AI 视频模型，专为生成连贯的多镜头视频而设计，提供流畅的运动和对详细提示的精确遵循。它支持 480p、720p 和 1080p 的分辨率。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 视频生成的文本提示；正面文本提示；支持中英文，建议不超过 500 字。 

 视频质量。可接受的值：`480p`，`720p`，`1080p` 

 生成视频的长宽比。 可接受的值：`21:9`，`16:9`，`4:3`，`1:1`，`3:4`，`9:16` 

 指定生成视频的长度（以秒为单位）。可用选项：`5`，`10` 

 确定相机位置是否应保持固定。 

 用于生成的随机种子。-1 表示将使用随机种子。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
