---
title: "Z Image 文生图 Turbo LoRA"
url: "https://docs.jiekou.ai/docs/models/reference-z-image-turbo-lora.md"
crawled_at: "2026-02-26T23:36:43.769859"
---

Published Time: Thu, 26 Feb 2026 15:36:43 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Z Image 文生图 Turbo LoRA

这是一个异步 API，仅返回异步 task\_id。你需要使用 task\_id 调用任务结果查询 API 获取生成结果。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 生成的随机种子。-1 表示使用随机种子 取值范围：\[-1, 2147483647] 

 生成图像的像素尺寸（宽\*高） 

 要应用的 LoRA 列表（最多 3 个） 数组长度：0 - 3   LoRA 权重的 URL 或路径   LoRA 权重的缩放比例。用于在与基础模型合并前缩放 LoRA 权重 取值范围：\[0, 4]  

 生成的正向提示词 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
