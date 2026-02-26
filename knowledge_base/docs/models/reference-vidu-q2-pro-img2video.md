---
title: "VIDU Q2 Pro 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-q2-pro-img2video.md"
crawled_at: "2026-02-26T23:36:01.561762"
---

Published Time: Thu, 26 Feb 2026 15:36:01 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# VIDU Q2 Pro 图生视频

根据参考图像生成新的视频。支持 540p、720p、1080p 三种分辨率。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 是否添加背景音乐 

 随机种子，用于控制生成结果的随机性。相同种子会产生相似的结果。 

 是否生成音频 

 输入图片 URL 列表 数组长度：1 - 无限制 

 文本提示词，详细描述期望生成的视频内容 

 视频时长（秒），支持 1-10 秒 可选值：`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` 

 是否开启离峰任务模式 

 语音 ID，可选 

 是否添加水印 

 输出视频的分辨率。默认值为 720p。 可选值：`540p`, `720p`, `1080p` 

 运动幅度，控制视频中物体的运动强度 可选值：`auto`, `small`, `medium`, `high` 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。 

 Provider request ID (optional)
