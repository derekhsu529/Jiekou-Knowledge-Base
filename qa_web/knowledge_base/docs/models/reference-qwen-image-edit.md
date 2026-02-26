---
title: "Qwen-Image 图像编辑"
url: "https://docs.jiekou.ai/docs/models/reference-qwen-image-edit.md"
crawled_at: "2026-02-26T23:38:30.195080"
---

Published Time: Thu, 26 Feb 2026 15:38:30 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen-Image 图像编辑

Qwen-Image 图像编辑 — 一个用于下一代图像编辑生成的 20B MMDiT 模型。基于 20B Qwen-Image，它在保留风格的同时，提供精确的双语文本编辑（中文和英文），并支持语义和外观级别的编辑。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 用于生成图像的提示。 

 用于生成图像的图像。 

 用于生成的随机种子。-1 表示将使用随机种子。范围：-1 \~ 2147483647。默认值为 -1。 

 输出图像的格式。默认是 jpeg。

 枚举值: `jpeg`, `png`, `webp` 

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
