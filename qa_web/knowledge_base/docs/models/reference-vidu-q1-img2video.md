---
title: "Vidu Q1 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-q1-img2video.md"
crawled_at: "2026-02-26T23:38:45.536023"
---

Published Time: Thu, 26 Feb 2026 05:01:17 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu Q1 图生视频

Vidu Q1 图生视频将静态图像转换为动态视频，融入创意故事叙述和动画效果。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 用作生成视频起始帧的图像。 图像字段要求： * 仅接受 1 张图像 * 支持公共 URL 或 Base64 格式 * 支持格式：png、jpeg、jpg、webp * 图像宽高比必须小于 1:4 或 4:1 * 所有图像限制为 50MB * base64 解码后的长度必须小于 10MB，且必须包含适当的内容类型字符串。例如： ``` data:image/png;base64,{base64_encode} ``` 

 视频生成的文本提示词，最大长度为 1500 个字符。 

 视频持续时间（秒）。默认为 5 秒，目前仅支持 `5` 秒选项。 

 视频生成的随机种子。 * 默认为随机种子数值 * 手动设置的值将覆盖默认的随机种子 

 输出视频分辨率。默认为 1080p，目前仅支持 `1080p` 选项。 

 画面中物体的运动幅度。默认值：`auto`

 可选值：`auto`、`small`、`medium`、`large` 

 是否为生成的视频添加背景音乐。默认值：`false`

 可选值：`true`、`false` 当设置为 true 时，系统将自动添加合适的 BGM。BGM 无时长限制，系统会自动适配。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
