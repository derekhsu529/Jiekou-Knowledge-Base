---
title: "Midjourney 重新执行"
url: "https://docs.jiekou.ai/docs/models/reference-mj-reroll.md"
crawled_at: "2026-02-26T23:34:30.256149"
---

Published Time: Thu, 26 Feb 2026 15:34:30 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Midjourney 重新执行

使用 Midjourney 重新执行功能，对已生成的图像任务进行重新生成，获得不同的结果变体。该接口采用异步处理方式，客户端需要通过 task\_id 查询最终生成结果。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 任务 ID，用于指定要重新执行的原始任务。 

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
