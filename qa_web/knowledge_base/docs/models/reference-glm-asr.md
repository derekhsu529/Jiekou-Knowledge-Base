---
title: "GLM 音频转文字"
url: "https://docs.jiekou.ai/docs/models/reference-glm-asr.md"
crawled_at: "2026-02-26T23:32:23.964878"
---

Published Time: Thu, 26 Feb 2026 15:32:23 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM 音频转文字

使用 GLM-ASR-2512 模型将音频文件转录为文本，支持多语言转录。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 需要转录的音频文件URL或Base64编码字符串，支持的音频文件格式：.wav / .mp3，规格限制：文件大小 ≤ 25 MB、音频时长 ≤ 30 秒 

 在长文本场景中，可以提供之前的转录结果作为上下文。建议小于8000字。 

 热词表，用于提升特定领域词汇识别率。格式例如\["人名","地名"]，建议不超过100个。 数组长度：0 - 100 

## 响应

 音频转录的完整内容
