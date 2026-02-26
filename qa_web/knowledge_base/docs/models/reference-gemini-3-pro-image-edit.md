---
title: "Gemini 3 Pro Image Preview 图片编辑"
url: "https://docs.jiekou.ai/docs/models/reference-gemini-3-pro-image-edit.md"
crawled_at: "2026-02-26T23:32:13.552338"
---

Published Time: Thu, 26 Feb 2026 04:34:15 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini 3 Pro Image Preview 图片编辑

Gemini 3 Pro Image (Nano Banana) 旨在通过集成最先进的推理能力，解决最具挑战性的图像生成任务。它是处理复杂和多轮图像生成与编辑的最佳模型，具备更高的准确性和更优的图像质量。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 正向提示用于图像生成。 

 输入图像的 URL 列表。 

 输入图像的 base64 格式列表用于编辑。选择此项或 `image_urls`。 

 生成图片的宽高比。 可选值：`1:1`、`3:2`、`2:3`、`3:4`、`4:3`、`4:5`、`5:4`、`9:16`、`16:9`、`21:9` 

 生成图像的尺寸，可选值为 `1K`、`2K`、`4K`。 

## 响应参数

 生成图像的 URL 列表。
