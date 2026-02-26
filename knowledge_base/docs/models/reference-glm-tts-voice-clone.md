---
title: "GLM 音频复刻"
url: "https://docs.jiekou.ai/docs/models/reference-glm-tts-voice-clone.md"
crawled_at: "2026-02-26T23:32:29.997612"
---

Published Time: Thu, 26 Feb 2026 15:32:29 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM 音频复刻

使用音色复刻技术，基于示例音频生成指定音色、文本内容的语音合成。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 示例音频的文本内容，选填 

 生成试听音频的目标文本内容 

 示例音频的URL地址。大小限制不超过10M，建议音频时长在3秒到30秒之间。 

 指定唯一的音色名称 

## 响应

 音色 

 生成的试听音频文件URL地址
