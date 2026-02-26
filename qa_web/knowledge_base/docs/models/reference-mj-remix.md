---
title: "Midjourney 重塑"
url: "https://docs.jiekou.ai/docs/models/reference-mj-remix.md"
crawled_at: "2026-02-26T23:34:26.167351"
---

Published Time: Thu, 26 Feb 2026 15:34:26 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Midjourney 重塑

使用 Midjourney 重塑功能，对已生成图像进行重新创作和调整。支持强烈调整和细微调整两种模式，通过新的提示词对指定图片进行重塑处理。该接口采用异步处理方式，客户端需要通过 task\_id 查询最终生成结果。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 图片编号，用于指定要进行重塑的图片。 取值范围：0\~3 

 原始图像生成任务的唯一标识符。 

 新提示词，用于描述重塑后图像的期望内容和风格。 长度限制：1-8192 个字符。 

 Remix 模式，控制重塑的强度和程度。 * `0`: 强烈调整 - 对图像进行较大幅度的重塑和改变 * `1`: 细微调整 - 对图像进行轻微的调整和优化 

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
