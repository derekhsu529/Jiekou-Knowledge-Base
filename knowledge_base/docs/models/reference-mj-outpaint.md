---
title: "Midjourney 扩图"
url: "https://docs.jiekou.ai/docs/models/reference-mj-outpaint.md"
crawled_at: "2026-02-26T23:34:24.162112"
---

Published Time: Thu, 26 Feb 2026 15:34:24 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Midjourney 扩图

使用 Midjourney 扩图功能，对已生成的图像进行外扩处理，在保持原图内容的基础上扩展图像边界。该接口采用异步处理方式，客户端需要通过 task\_id 查询最终生成结果。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 图片编号，用于指定要进行扩图的图片。 取值范围：0\~3 

 原始图像生成任务的唯一标识符。 

 扩图区域提示词，用于描述扩展区域的内容。 长度限制：1-8192 个字符。 

 扩图目标比例，即在视图中新图所占区域相较原图区域的倍数。 取值范围：1.1\~2.0 例如：一个 1:1 图片扩图后，外扩 20%（scale=1.2） 

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
