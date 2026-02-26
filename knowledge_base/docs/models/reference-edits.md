---
title: "GPT 图像编辑"
url: "https://docs.jiekou.ai/docs/models/reference-edits.md"
crawled_at: "2026-02-26T23:37:17.752829"
---

Published Time: Thu, 26 Feb 2026 15:37:17 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GPT 图像编辑

使用 GPT 图像编辑模型，通过文本描述对现有图像进行智能编辑和修改。支持多种图像格式和质量选项，满足不同场景的图像编辑需求。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 用于图像编辑的模型。目前仅支持 `gpt-image-1`。 

 待编辑的图像数组（multipart/form-data）。 对于 `gpt-image-1`，每张图片需为 png、webp 或 jpg 格式，单张小于 50MB，最多可上传 16 张图片。 

 期望编辑后图像的文本描述。 对于 `gpt-image-1`，最大长度为 32000 个字符。 

 生成图像的质量，默认为 `auto`。 对于 `gpt-image-1`，支持的取值有：`auto`、`high`、`medium`、`low`。 

## 响应参数

 图像生成时间的 Unix 时间戳（秒级）。 

 生成的图像列表。   生成图像的 base64 编码字符串。  

 仅 `gpt-image-1` 支持，图像生成的 token 使用信息。   输入提示词（包括图像和文本）的 token 数量。   输入 token 的详细信息。   输入提示词中图像 token 的数量。   输入提示词中文本 token 的数量。     模型生成的输出 token 数量。   本次图像生成总共消耗的 token 数量（包括图像和文本）。
