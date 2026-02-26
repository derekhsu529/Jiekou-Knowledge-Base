---
title: "FLUX.1 Kontext Dev"
url: "https://docs.jiekou.ai/docs/models/reference-flux-1-kontext-dev.md"
crawled_at: "2026-02-26T23:37:37.785993"
---

Published Time: Thu, 26 Feb 2026 15:37:37 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# FLUX.1 Kontext Dev

FLUX.1 Kontext Dev 是一款在提高提示词遵循度和字体生成一致性的同时，保持高效速度且适合编辑需求的模型。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 用于生成图像的提示词。 

 用于生成图像的图片列表。最多支持 4 张图片。 

 是否启用极速模式，开启后生成速度更快，但可能降低质量且价格更低。 默认值：`false`。 

 生成媒体的尺寸（像素，宽\*高）。每个维度范围：\[256 \~ 1536]。 

 推理步数。默认值为 28。取值范围：\[1 \~ 50]。 

 引导系数，用于控制生成。默认值为 2.5。取值范围：\[1.0 \~ 20.0]。 

 生成图像的数量。默认值为 1。取值范围：\[1 \~ 4]。 

 随机种子。默认值为 -1，-1 表示使用随机种子。取值范围：\[-1 \~ 2147483647]。 

 输出图像的格式。默认值为 jpeg。

 可选：`jpeg`、`png`、`webp` 

## 返回结果

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
