---
title: "Gemini 2.5 Flash Image 图片编辑"
url: "https://docs.jiekou.ai/docs/models/reference-gemini-2.5-flash-image-edit.md"
crawled_at: "2026-02-26T23:32:09.859052"
---

Published Time: Thu, 26 Feb 2026 15:32:09 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini 2.5 Flash Image 图片编辑

使用 Gemini 2.5 Flash 模型通过文本提示词编辑图像。您可以通过 URL 或 base64 编码字符串提供图像。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 描述图像预期编辑效果的文本提示词 

 用于编辑的输入图像 URL 列表 

 生成图像的宽高比。可用值：1:1、3:2、2:3、3:4、4:3、4:5、5:4、9:16、16:9、21:9 可选值：`1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` 

 用于编辑的 base64 编码图像列表 

## 响应

 编辑后输出图像的 URL 列表
