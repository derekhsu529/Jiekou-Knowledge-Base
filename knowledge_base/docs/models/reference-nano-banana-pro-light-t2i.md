---
title: "Nano Banana Pro Light 文生图 (reverse)"
url: "https://docs.jiekou.ai/docs/models/reference-nano-banana-pro-light-t2i.md"
crawled_at: "2026-02-26T23:38:23.860540"
---

Published Time: Thu, 26 Feb 2026 15:38:23 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Nano Banana Pro Light 文生图 (reverse)

根据文本描述生成图像

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 要生成的图像数。必须介于1和10之间。 取值范围：\[1, 10] 

 生成图像的大小 可选值：`1x1`, `2x3`, `3x2`, `3x4`, `4x3`, `4x5`, `5x4`, `9x16`, `16x9`, `21x9` 

 所需图像的文本描述。 

 选择图像生成质量 可选值：`1k`, `2k`, `4k` 

 返回生成的图像的格式。必须是url之一—b64\_json。 可选值：`url`, `b64_json` 

## 响应

 生成的图像列表   图像URL（当response\_format为url时）   Base64编码的图像数据（当response\_format为b64\_json时）   修订后的提示词（如果有的话）  

 创建时间戳
