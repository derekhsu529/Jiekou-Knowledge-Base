---
title: "Vidu 2.0 首末帧"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-2.0-startend2video.md"
crawled_at: "2026-02-26T23:38:44.003327"
---

Published Time: Thu, 26 Feb 2026 15:38:43 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu 2.0 首末帧

Vidu 2.0 首末帧通过起始帧和结束帧生成动态视频，融入创意故事叙述和动画效果。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 两张图像：第一张为起始帧，第二张为结束帧。 注意事项： 1. 支持公共 URL 或 Base64 格式 2. 宽高比必须接近：起始帧与结束帧的比例必须在 0.8\~1.25 之间 3. 支持格式：png、jpeg、jpg、webp 4. 最大尺寸：50MB 5. base64 解码后的长度必须小于 10MB，且必须包含适当的内容类型字符串。例如： ``` data:image/png;base64,{base64_encode} ``` 

 提示词描述，最大 1500 个字符。 

 视频持续时间（秒）。默认为 4 秒，可选 `4` 秒或 `8` 秒。 

 视频生成的随机种子。 * 默认为随机种子数值 * 手动设置的值将覆盖默认的随机种子 

 基于时长的分辨率选项： * 4 秒：默认 360p，可选 `360p`、`720p`、`1080p` * 8 秒：默认 720p，可选 `720p` 

 画面中物体的运动幅度。默认值：`auto`

 可选值：`auto`、`small`、`medium`、`large` 

 是否为生成的视频添加背景音乐。默认值：`false`

 可选值：`true`、`false` 当设置为 true 时，系统将自动添加合适的 BGM。BGM 无时长限制，系统会自动适配。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
