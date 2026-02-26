---
title: "Midjourney 文生图"
url: "https://docs.jiekou.ai/docs/models/reference-mj-txt2img.md"
crawled_at: "2026-02-26T23:34:32.176079"
---

Published Time: Thu, 26 Feb 2026 15:34:32 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Midjourney 文生图

使用 Midjourney 图像生成模型，通过文本描述快速生成高质量图像。该接口采用异步处理方式，客户端需要通过 task\_id 查询最终生成结果。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 文本信息，用于描述期望生成的图像内容。 长度限制：1-8192 个字符。 

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
