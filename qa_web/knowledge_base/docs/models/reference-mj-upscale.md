---
title: "Midjourney 高清"
url: "https://docs.jiekou.ai/docs/models/reference-mj-upscale.md"
crawled_at: "2026-02-26T23:34:34.220943"
---

Published Time: Thu, 26 Feb 2026 15:34:34 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Midjourney 高清

使用 Midjourney 高清功能，对已生成的图像进行高清化处理，提升图像分辨率和细节质量。该接口采用异步处理方式，客户端需要通过 task\_id 查询最终生成结果。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 图片编号，用于指定要进行高清处理的图片。 取值范围：0\~3 

 原始图像生成任务的唯一标识符。 

 高清类型，控制高清处理的风格。 取值范围：0\~1 * `0`: v6/niji6/v6.1/v7 subtle 高清 * `1`: v6/niji6/v6.1/v7 creative 高清 

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
