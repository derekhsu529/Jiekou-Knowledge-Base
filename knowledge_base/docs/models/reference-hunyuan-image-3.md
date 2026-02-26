---
title: "Hunyuan Image 3"
url: "https://docs.jiekou.ai/docs/models/reference-hunyuan-image-3.md"
crawled_at: "2026-02-26T23:17:04.903677"
---

Published Time: Thu, 26 Feb 2026 04:59:03 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Hunyuan Image 3

Hunyuan Image 3 是一款先进的文生图模型。只需提供文字描述，即可生成高质量、富有情感和故事性的图片，助力您的创意表达与艺术创作。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 正向提示词，用于指导图片生成内容。 

 生成图片的尺寸，像素为宽\*高。每个维度范围 \[256 \~ 1536]，默认值为 `1024*1024`。 

 随机种子。取值为 -1 时表示随机种子，取值范围为 \[-1 \~ 2147483647]，默认值为 `-1`。 

## 返回结果

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
