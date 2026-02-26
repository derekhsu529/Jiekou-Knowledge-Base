---
title: "Qwen-Image 文生图"
url: "https://docs.jiekou.ai/docs/models/reference-qwen-image-txt2img.md"
crawled_at: "2026-02-26T23:38:32.123066"
---

Published Time: Thu, 26 Feb 2026 15:38:31 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen-Image 文生图

Qwen-Image — 一个 20B MMDiT 模型，用于下一代文本到图像生成。特别擅长创建带有本地文本的惊艳图形海报。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 图像生成的文本提示。 

 生成媒体的像素大小（宽\*高）。默认值为 `1024*1024`。长和宽的像素范围：256 \~ 1536。 

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
