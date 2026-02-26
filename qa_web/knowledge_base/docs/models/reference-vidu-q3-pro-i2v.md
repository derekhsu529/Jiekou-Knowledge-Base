---
title: "Vidu Q3 Pro 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-q3-pro-i2v.md"
crawled_at: "2026-02-26T23:36:19.578872"
---

Published Time: Thu, 26 Feb 2026 15:36:19 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu Q3 Pro 图生视频

Vidu Q3 Pro 图像转视频工具可将静态图像转换为动态视频，在保持主体一致性的同时，生成自然运动与更流畅的场景动态效果。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 随机种子，用于可重复生成；0 或不传则随机生成 取值范围：\[0, 2147483647] 

 视频背景音乐的自定义音频URL；支持 mp3、wav、m4a、flac 格式；最大 20MB 

 输出视觉风格；general 为写实风格，anime 为动漫风格 可选值：`general`, `anime` 

 参考图片 URL 数组；支持 `.jpg`、`.jpeg`、`.png`、`.webp`。 每张图片大小不超过 50MB；宽高比需在 1:4 与 4:1 之间。 目前只支持输入 1 张图 

 启用音画匹配；设为 true 时，音频节奏与视频动态同步 

 视频生成的运动描述；描述场景运动、动作和动态效果。 长度限制：0 - 1500 

 自定义水印图片URL；支持 png、jpeg、jpg、webp 格式；最大 10MB 

 视频时长（秒） 取值范围：\[1, 16] 

 使用非高峰时段定价；设为 true 时，任务排队等待非高峰时段处理以降低成本 

 在输出视频上启用水印 

 输出视频分辨率 可选值：`540p`, `720p`, `1080p` 

 水印在视频上的位置 可选值：`top-left`, `top-right`, `bottom-left`, `bottom-right` 

 输出视频宽高比 可选值：`16:9`, `9:16`, `4:3`, `3:4`, `1:1` 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
