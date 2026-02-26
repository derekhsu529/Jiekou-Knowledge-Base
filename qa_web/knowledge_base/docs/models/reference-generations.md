---
title: "GPT 文生图"
url: "https://docs.jiekou.ai/docs/models/reference-generations.md"
crawled_at: "2026-02-26T23:32:17.523647"
---

Published Time: Thu, 26 Feb 2026 04:54:34 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GPT 文生图

使用 GPT 图像生成模型，通过文本描述快速生成高质量图像。支持多种尺寸和质量选项，满足不同场景的图像生成需求。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 用于图像生成的模型。目前仅支持 `gpt-image-1`。 

 期望生成图像的文本描述。 对于 `gpt-image-1`，最大长度为 32000 个字符。 

 生成图像的质量，默认为 `auto`。 对于 `gpt-image-1`，支持的取值有：`auto`、`high`、`medium`、`low`。 

 生成图像的数量，取值范围为 1\~10，默认为 1。 

 生成图像的尺寸，默认为 `auto`。 对于 `gpt-image-1`，支持的取值有： * `1024x1024`：正方形 * `1536x1024`：横向 * `1024x1536`：纵向 * `auto`：默认值 

## 响应参数

 图像生成时间的 Unix 时间戳（秒级）。 

 生成的图像列表。   生成图像的 base64 编码字符串。  

 生成图像的输出格式。可选值：`png`、`webp`、`jpeg`。 

 生成图像的质量。可选值：`low`、`medium`、`high`。 

 生成图像的尺寸。可选值：`1024x1024`、`1024x1536`、`1536x1024`。 

 仅 `gpt-image-1` 支持，图像生成的 token 使用信息。   输入提示词（包括图像和文本）的 token 数量。   输入 token 的详细信息。   输入提示词中图像 token 的数量。   输入提示词中文本 token 的数量。     模型生成的输出 token 数量。   本次图像生成总共消耗的 token 数量（包括图像和文本）。
