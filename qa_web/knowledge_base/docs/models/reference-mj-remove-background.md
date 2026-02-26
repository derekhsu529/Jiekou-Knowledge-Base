---
title: "Midjourney 移除背景"
url: "https://docs.jiekou.ai/docs/models/reference-mj-remove-background.md"
crawled_at: "2026-02-26T23:34:28.273328"
---

Published Time: Thu, 26 Feb 2026 15:34:28 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Midjourney 移除背景

使用 Midjourney 移除背景功能，自动识别并移除图像中的背景，保留主体对象。该接口采用异步处理方式，客户端需要通过 task\_id 查询最终生成结果。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 图片 url，指定要移除背景的图像地址。 最大长度：1024 字符 

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
