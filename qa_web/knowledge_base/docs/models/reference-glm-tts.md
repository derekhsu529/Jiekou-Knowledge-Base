---
title: "GLM 语音合成"
url: "https://docs.jiekou.ai/docs/models/reference-glm-tts.md"
crawled_at: "2026-02-26T23:32:27.861026"
---

Published Time: Thu, 26 Feb 2026 15:32:27 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM 语音合成

使用 GLM-TTS 将文本转换为自然语音，支持多种声音、情感控制和语调调整。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 要转换为语音的文本 长度限制：0 - 1024 

 语速，默认1.0，取值范围\[0.5, 2] 取值范围：\[0.5, 2] 

 生成音频时使用的音色，支持系统音色以及复刻音色两种类型。系统音色包括：tongtong(彤彤，默认音色)、chuichui(锤锤)、xiaochen(小陈)、jam(动动动物圈jam音色)、kazi(动动动物圈kazi音色)、douji(动动动物圈douji音色)、luodo(动动动物圈luodo音色) 

 音量，默认1.0，取值范围(0, 10] 取值范围：\[0, 10] 

 音频输出格式，默认返回pcm格式的文件 可选值：`wav`, `pcm` 

 控制AI生成音频时是否添加水印。true: 默认启用AI生成的显式水印及隐式数字水印，符合政策要求。false: 关闭所有水印，仅对已完成去水印动作的用户生效。 

## 响应

业务处理成功，采样率建议设置为24000

格式: `binary`
