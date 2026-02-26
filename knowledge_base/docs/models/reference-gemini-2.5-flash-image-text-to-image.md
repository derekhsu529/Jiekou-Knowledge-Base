---
title: "Gemini 2.5 Flash Image 文生图"
url: "https://docs.jiekou.ai/docs/models/reference-gemini-2.5-flash-image-text-to-image.md"
crawled_at: "2026-02-26T23:32:11.878429"
---

Published Time: Thu, 26 Feb 2026 15:32:11 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini 2.5 Flash Image 文生图

使用 Gemini 2.5 Flash 模型根据文字提示生成图像。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 描述要生成图像的文字提示 

 生成图像的宽高比。可用值：1:1、3:2、2:3、3:4、4:3、4:5、5:4、9:16、16:9、21:9 可选值：`1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` 

## 响应

 生成图像的 URL 列表
