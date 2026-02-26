---
title: "FLUX.1 Kontext Pro"
url: "https://docs.jiekou.ai/docs/models/reference-flux-1-kontext-pro.md"
crawled_at: "2026-02-26T23:17:00.948351"
---

Published Time: Thu, 26 Feb 2026 05:00:11 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# FLUX.1 Kontext Pro

FLUX.1 Kontext Pro 是一款在提升提示词遵循度和字体生成一致性的同时，依然保持高效速度且适合编辑需求的模型

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 用于生成图像的提示词。 

 用于生成图像的图片列表。最多支持 4 张图片。 

 引导系数，用于控制生成。默认值为 3.5。取值范围：\[1.0 \~ 20.0]。 

 生成图像的宽高比。

 可选：`21:9`、`16:9`、`4:3`、`3:2`、`1:1`、`2:3`、`3:4`、`9:16`、`9:21` 

 随机种子。默认值为 -1，-1 表示使用随机种子。取值范围：\[-1 \~ 2147483647]。 

 仅在文生图模式下支持。

 生成图像的安全容忍等级，1 为最严格，5 为最宽松，默认值为 2。

 可选：`1`、`2`、`3`、`4`、`5` 

## 返回结果

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
