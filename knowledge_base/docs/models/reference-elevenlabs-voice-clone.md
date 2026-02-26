---
title: "ElevenLabs 音频快速复刻"
url: "https://docs.jiekou.ai/docs/models/reference-elevenlabs-voice-clone.md"
crawled_at: "2026-02-26T23:37:35.790931"
---

Published Time: Thu, 26 Feb 2026 15:37:35 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ElevenLabs 音频快速复刻

创建语音克隆并将其添加到您的语音库中。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 用于识别此语音的名称。此名称将显示在网站的下拉菜单中。 

 用于语音克隆的音频录音文件列表。 

 语音的序列化标签字典。 

 语音的描述信息。 

 如果设置为 true，将使用音频隔离模型从语音样本中去除背景噪音。如果样本不包含背景噪音，启用此选项可能会降低质量。 

## 响应

 新创建语音的 ID。 

 该语音是否需要验证。
