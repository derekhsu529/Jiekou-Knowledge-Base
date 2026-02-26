---
title: "Nano Banana Light 图生图"
url: "https://docs.jiekou.ai/docs/models/reference-nano-banana-light-i2i.md"
crawled_at: "2026-02-26T23:34:38.162191"
---

Published Time: Thu, 26 Feb 2026 15:34:38 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Nano Banana Light 图生图

根据输入图像和文本描述生成新图像

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 遮罩图像URL或Base64编码 

 生成图像的大小 可选值：`1x1`, `2x3`, `3x2`, `3x4`, `4x3`, `4x5`, `5x4`, `9x16`, `16x9`, `21x9` 

 要处理的输入图像列表 数组长度：1 - 10 图像URL或Base64编码 

 所需图像的文本描述。最大长度为1000个字符。 

 选择图像生成质量 可选值：`1k`, `2k`, `4k` 

 返回生成的图像的格式。目前仅支持 b64\_json 可选值：`url`, `b64_json` 

## 响应

 生成的图像列表   图像URL（当response\_format为url时）   Base64编码的图像数据（当response\_format为b64\_json时）   修订后的提示词（如果有的话）  

 创建时间戳
