---
title: "PixVerse V4.5 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-pixverse-v4.5-i2v.md"
crawled_at: "2026-02-26T23:38:26.054758"
---

Published Time: Thu, 26 Feb 2026 15:38:25 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# PixVerse V4.5 图生视频

使用 PixVerse 最新的 v4.5 模型从文本描述和图像生成高质量视频。支持多种分辨率、纵横比和运动模式，以实现多样化的视频创作。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 视频生成的文本提示。 * 最大长度：2048 个字符 * 清晰描述所需场景和动作 

 视频的第一帧。 * 支持的图像格式包括 .jpg/.jpeg/.png * 图像文件大小不能超过 10MB * 图像分辨率不应小于 300\*300 像素 * 图像的宽高比应在 1:2.5 \~ 2.5:1 之间 

 视频质量。默认值：`540p`

 可接受的值： * fast\_mode 为 false：`360p`、`540p`、`720p`、`1080p` * fast\_mode 为 true：`360p`、`540p`、`720p` 

 生成的负面提示。 * 最大长度：2048 个字符 

 是否启用快速模式，该模式将更快地生成视频，但可能降低质量并降低价格。 默认值：`false`。 

 风格预设（仅限 v3.5）。

 可接受的值：`anime`、`3d_animation`、`clay`、`comic`、`cyberpunk` 

 用于生成的随机种子。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
