---
title: "Fish Audio 语音合成"
url: "https://docs.jiekou.ai/docs/models/reference-fish-audio-txt2speech.md"
crawled_at: "2026-02-26T23:31:57.927343"
---

Published Time: Thu, 26 Feb 2026 15:31:57 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fish Audio 语音合成

 为了获得最佳效果，建议在使用此 API 之前，先使用[音频复刻](/docs/models/reference-fish-audio-voice-cloning)上传参考音频。这将提高语音质量并降低延迟。 

Fish Audio 将文本转换为语音。

支持的音频格式：

* WAV / PCM
  * 采样率：8kHz, 16kHz, 24kHz, 32kHz, 44.1kHz
  * 默认采样率：44.1kHz
  * 16-bit，单声道

* MP3
  * 采样率：32kHz, 44.1kHz
  * 默认采样率：44.1kHz
  * 单声道
  * 比特率：64kbps, 128kbps (默认), 192kbps

* Opus
  * 采样率：48kHz
  * 默认采样率：48kHz
  * 单声道
  * 比特率：-1000 (自动), 24kbps, 32kbps (默认), 48kbps, 64kbps

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 要转换为语音的文本。 

 控制语音生成的随机性。较高的值（例如 1.0）使输出更随机，较低的值（例如 0.1）使其更确定。我们建议 `s1` 模型使用 `0.9`。 必需范围：`0 <= x <= 1` 

 通过核采样控制多样性。较低的值（例如 0.1）使输出更集中，较高的值（例如 1.0）允许更多样性。我们建议 `s1` 模型使用 `0.9`。 必需范围：`0 <= x <= 1` 

 用于语音的参考音频，这需要 MessagePack 序列化，这将覆盖 reference\_voices 和 reference\_texts。   参考音频文件。   与音频对应的参考文本。  

 用于语音的参考模型 ID。 

 用于语音的韵律控制。   语音速度控制。   语音音量控制。  

 用于语音的分块长度。 必需范围：`100 <= x <= 300` 

 是否规范化语音，这将降低延迟，但可能会降低对数字和日期的处理性能。 

 用于语音的格式。 可选值：`wav`, `pcm`, `mp3`, `opus` 

 用于语音的采样率。 

 用于语音的 MP3 比特率。 可选值：`64`, `128`, `192` 

 用于语音的 Opus 比特率。 可选值：`-1000`, `24`, `32`, `48`, `64` 

 用于语音的延迟设置，balanced 将降低延迟但可能导致性能下降。 可选值：`normal`, `balanced` 

## 响应

API 将直接返回由 `format` 参数指定格式的音频流（默认：mp3）。
