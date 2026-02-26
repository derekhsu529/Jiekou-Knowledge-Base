---
title: "Seedance 1.5 Pro 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-seedance-v1.5-pro-i2v.md"
crawled_at: "2026-02-26T23:38:37.850234"
---

Published Time: Thu, 26 Feb 2026 15:38:37 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedance 1.5 Pro 图生视频

这是一个异步 API，返回 task\_id。使用 task\_id 查询任务结果 API 以获取视频生成结果。支持文生视频、图生视频（首帧）和图生视频（首尾帧）生成。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 帧率（每秒帧数）。仅支持 24 fps。 可选值：`24` 

 用于控制随机性的种子整数。范围：\[-1, 2^32-1]。-1 表示使用随机种子。相同种子和相同请求会产生相似（但不完全相同）的结果。 取值范围：\[-1, 4294967295] 

 图生视频的首帧图像。可以是图像 URL 或 Base64 编码的图像。URL 必须可访问。Base64 格式：`data:image/<图像格式>;base64,`。支持的格式：jpeg、png、webp、bmp、tiff、gif。宽高比：(0.4, 2.5)，尺寸：(300, 6000) 像素，大小：\< 30 MB。 

 生成视频的宽高比。'adaptive'：文生视频时，模型根据提示词智能选择最佳比例；图生视频时，根据上传的首帧图像比例自动选择。 可选值：`16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `21:9`, `adaptive` 

 描述预期视频内容的文本提示词。支持中英文。建议不超过 500 个字符。如需生成带对话的音频，请将语音内容放在双引号内以获得更好的音频生成效果。 

 视频时长，单位为秒。支持 \[4, 12] 范围内的指定时长。注意：时长会影响计费。 取值范围：\[4, 12] 

 生成的视频是否包含水印。true：带水印。false：不带水印。 

 首尾帧图生视频的尾帧图像。可以是图像 URL 或 Base64 编码的图像。要求与 image 字段相同。当宽高比不同时，尾帧将自动裁剪以匹配首帧。 

 视频分辨率。Seedance 1.5 pro 支持 480p 和 720p（暂不支持 1080p）。 可选值：`480p`, `720p` 

 是否固定摄像机位置。true：平台在提示词中追加固定摄像机指令（效果不保证）。false：不固定摄像机。 

 处理请求的服务层级。'default'：在线推理模式，RPM 和并发配额较低，适用于时效性要求高的场景。'flex'：离线推理模式，TPD 配额更高，价格为在线模式的 50%，适用于对延迟不敏感的场景。 可选值：`default`, `flex` 

 生成的视频是否包含同步音频。true：视频包含基于提示词和视觉内容自动生成的语音、音效和背景音乐。false：输出无声视频。 

 任务超时阈值，单位为秒，从 created\_at 时间戳开始计算。默认值：172800（48 小时）。范围：\[3600, 259200]。超过此时间的任务将被自动终止并标记为 'expired'。 取值范围：\[3600, 259200] 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
