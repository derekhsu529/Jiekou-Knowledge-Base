---
title: "Seedream  5.0 lite"
url: "https://docs.jiekou.ai/docs/models/reference-seedream-5.0-lite.md"
crawled_at: "2026-02-26T23:35:12.544419"
---

Published Time: Thu, 26 Feb 2026 15:35:12 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedream  5.0 lite

根据输入的文本提示词和/或参考图片生成图像。支持生成单图或组图（一组内容关联的图片）。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 指定生成图像的尺寸信息。方式1：指定分辨率（2K、3K）；方式2：指定宽高像素值（如2048x2048）。总像素取值范围：\[2560x1440=3686400, 3072x3072x1.1025=10404496]，宽高比取值范围：\[1/16, 16]。 

 输入的图片信息数组，支持 URL 或 Base64 编码。最多支持传入 14 张参考图。图片格式支持 jpeg、png、webp、bmp、tiff、gif。 数组长度：1 - 14 

 用于生成图像的提示词，支持中英文。建议不超过300个汉字或600个英文单词。 

 是否在生成的图片中添加水印。 

 提示词优化功能的配置。   设置提示词优化功能使用的模式。standard：标准模式，质量更高，耗时较长；fast：快速模式，耗时更短，质量一般。当前仅支持 standard 模式。 可选值：`standard`  

 控制是否关闭组图功能。auto：自动判断模式，模型会根据提示词自主判断是否返回组图；disabled：关闭组图功能，只生成一张图。 可选值：`auto`, `disabled` 

 组图功能的配置。仅当 sequential\_image\_generation 为 auto 时生效。   指定本次请求最多可生成的图片数量。输入的参考图数量+最终生成的图片数量≤15张。 取值范围：\[1, 15]  

## 响应

 生成的图片信息数组。
