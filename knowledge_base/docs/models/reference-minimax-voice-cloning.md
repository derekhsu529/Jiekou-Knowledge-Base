---
title: "MiniMax 音频快速复刻"
url: "https://docs.jiekou.ai/docs/models/reference-minimax-voice-cloning.md"
crawled_at: "2026-02-26T23:34:20.148095"
---

Published Time: Thu, 26 Feb 2026 15:34:20 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax 音频快速复刻

本接口支持单、双声道复刻声音，支持按照指定音频文件快速复刻相同音色的语音。
本接口产出的快速复刻音色为临时音色，如您希望永久保留某复刻音色，请于 168 小时（7 天）内在任意 T2A 语音合成接口中调用该音色（不包含本接口内的试听行为）；否则，该音色将被删除。

本接口适用场景：IP 复刻、音色克隆等需要快速复刻某一音色的相关场景。

说明：

* 上传的音频文件格式需为：mp3、m4a、wav 格式；
* 上传的音频文件的时长最少应不低于 10 秒，最长应不超过 5 分钟；
* 上传的音频文件大小需不超过 20mb。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 需要复刻音色的音频文件 url。支持 mp3、m4a、wav 格式。 

 音色复刻参数，提供本参数将有助于增强语音合成的音色相似度和稳定性。 若使用本参数，需同时上传一小段示例音频（时长小于 8s）及音频对应文本，音频支持 mp3、m4a、wav 格式。   音频 prompt 参数，示例音频 url，时长必须小于 8s。   音频 prompt 参数，填入示例音频的对应文本，需确保和音频内容一致，句末需有标点符号做结尾。  

 复刻试听参数。模型将使用复刻后的音色念诵本段文本内容，并以链接的形式将音频合成结果返回，供试听复刻效果。限制 2000 字符以内。注：试听将根据字符数正常收取语音合成费用，定价与 T2A 各接口一致。 

 复刻试听参数。指定试听使用的语音模型，传"text"字段时必传该字段。

 可选项：`speech-02-hd`, `speech-02-turbo`, `speech-2.5-hd-preview`, `speech-2.5-turbo-preview` 

 音频复刻参数。取值范围\[0,1]。上传该字段会设置文本校验准确率阈值，不传时该字段值默认 0.7。 

 音频复刻参数。是否开启降噪。不传时默认取 false。 

 音频复刻参数。是否开启音量归一化。不传时默认取 false。 

## 响应

 如果请求体中传入了试听文本 text 以及试听模型 model，那么本参数将以链接形式返回试听音频。 

 生成的 voice\_id
