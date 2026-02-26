---
title: "Midjourney 变化"
url: "https://docs.jiekou.ai/docs/models/reference-mj-variation.md"
crawled_at: "2026-02-26T23:34:36.208057"
---

Published Time: Thu, 26 Feb 2026 15:34:36 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Midjourney 变化

使用 Midjourney 变化功能，对已生成的图像进行轻微或强烈的变换，创造出不同风格的变体图像。该接口采用异步处理方式，客户端需要通过 task\_id 查询最终生成结果。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 图片编号，用于指定要进行变化的图片。 取值范围：0\~3 

 原始图像生成任务的唯一标识符。 

 新的提示词，用于指导图像变化的方向。 长度限制：1-8192 个字符。 

 变换类型，控制变化的强度。 取值范围：0\~1 * `0`: subtle 轻微变换 * `1`: strong 强烈变换 

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
