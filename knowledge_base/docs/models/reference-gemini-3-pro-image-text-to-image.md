---
title: "Gemini 3 Pro Image Preview 文生图"
url: "https://docs.jiekou.ai/docs/models/reference-gemini-3-pro-image-text-to-image.md"
crawled_at: "2026-02-26T23:32:15.884047"
---

Published Time: Thu, 26 Feb 2026 15:32:15 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini 3 Pro Image Preview 文生图

Gemini 3 Pro Image（Nano Banana）融合顶尖推理引擎，专为攻克高难度图像生成而生。无论是复杂场景还是多轮创作，它都能以更高精度、更优画质，成为您图像生成与编辑的首选利器。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 正向提示用于图像生成。 

 生成图片的宽高比。 可选值：`1:1`、`3:2`、`2:3`、`3:4`、`4:3`、`4:5`、`5:4`、`9:16`、`16:9`、`21:9` 

 生成图像的尺寸，可选值为 `1K`、`2K`、`4K`。 

## 响应参数

 生成图像的 URL 列表。
