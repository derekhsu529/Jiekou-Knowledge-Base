---
title: "ElevenLabs 文字转语音 Turbo v2"
url: "https://docs.jiekou.ai/docs/models/reference-elevenlabs-tts-turbo-v2.md"
crawled_at: "2026-02-26T23:37:25.970075"
---

Published Time: Thu, 26 Feb 2026 15:37:25 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ElevenLabs 文字转语音 Turbo v2

使用您选择的声音将文本转换为语音并返回音频。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 如指定，系统将尽量有确定性地采样。相同seed及参数的重复请求应返回相同结果，但不保证完全确定性。 取值范围：\[0, 4294967295] 

 要转换为语音的文本。 

 要使用的语音ID。 

 当前请求文本之后的文本。用于在多次生成拼接时改善语音连贯性。 

 用于模型和文本规范化的语言代码（ISO 639-1）。如果模型不支持此语言代码，将返回错误。 

 生成音频的输出格式。格式为 codec\_sample\_rate\_bitrate。MP3的192kbps比特率需Creator及以上账户，PCM的44.1kHz采样率需Pro及以上账户。 可选值：`mp3_22050_32`, `mp3_24000_48`, `mp3_44100_32`, `mp3_44100_64`, `mp3_44100_96`, `mp3_44100_128`, `mp3_44100_192`, `pcm_8000`, `pcm_16000`, `pcm_22050`, `pcm_24000`, `pcm_32000`, `pcm_44100`, `pcm_48000`, `ulaw_8000`, `alaw_8000`, `opus_48000_32`, `opus_48000_64`, `opus_48000_96`, `opus_48000_128`, `opus_48000_192` 

 当前请求文本之前的文本。用于在多次生成拼接时改善语音连贯性。 

 若为true，使用IVC版本的语音而不是PVC版本。此为针对PVC版本较高延迟的临时方案。 

   调整语音的速度。1.0为默认速度，小于1.0会放慢语速，大于1.0会加快语速。   决定语音风格的夸张程度。尝试放大原始说话者的风格。设置为非0时会消耗更多计算资源，并可能增加延迟。   决定语音生成的稳定性与每次生成之间的随机性。较低的值会带来更宽广的情感范围，较高的值可能导致语音单调。   决定 AI 在尝试复刻原始声音时的贴合程度。   增强与原始说话者的相似度。需要稍高的计算负载，会增加延迟。  

 后续样本的request\_id列表。用于在重新生成样本时保持语音连贯性。最多可传3个request\_id。 数组长度：0 - 3 

 当前生成之前已生成样本的request\_id列表。可用于改善语音连贯性。最多可传3个request\_id。 数组长度：0 - 3 

 控制文本规范化。'auto'由系统决定，'on'总是规范化，'off'则跳过。 可选值：`auto`, `on`, `off` 

 控制针对某些支持语言的语言文本规范化以实现更自然发音。警告：可能大幅增加延迟。目前仅支持日语。 

 需要应用于文本的发音词典定位器（id, version\_id）列表。按顺序生效。每个请求最多可有3个定位器。 数组长度：0 - 3   发音词典版本的ID。如果未指定，则使用最新版本。   发音词典的ID。  

## 响应

生成的音频文件

格式: `binary`
