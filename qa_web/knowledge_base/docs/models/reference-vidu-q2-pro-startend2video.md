---
title: "VIDU Q2 Pro 首尾帧"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-q2-pro-startend2video.md"
crawled_at: "2026-02-26T23:36:05.493866"
---

Published Time: Thu, 26 Feb 2026 15:36:05 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# VIDU Q2 Pro 首尾帧

根据首尾两帧图像生成连贯的视频。支持 540p、720p、1080p 三种分辨率。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 是否为生成的视频添加背景音乐。true: 系统将从预设 BGM 库中自动挑选合适的音乐并添加；false: 不添加 BGM。BGM不限制时长，系统根据视频时长自动适配。 

 随机种子。当默认不传或者传0时，会使用随机数替代；手动设置则使用设置的种子。 

 图像数组，第一张图片视作首帧图，第二张图片视作尾帧图，模型将以此参数中传入的图片来生成视频。支持输入两张图。注1: 首尾帧两张输入图的分辨率需相近，首帧图的分辨率/尾帧图的分辨率要在0.8～1.25之间；注2: 支持传入图片 Base64 编码或图片URL（确保可访问）；注3: 图片支持 png、jpeg、jpg、webp格式；注4: 图片大小不超过50M；注5: Base64编码必须包含适当的内容类型字符串，例如：data:image/png;base64,{base64_encode} 数组长度：2 - 2 

 是否使用推荐提示词。true：是，由系统自动推荐提示词，并使用提示词内容生成视频（每个任务多消耗10积分）；false：否，根据输入的prompt生成视频 

 文本提示词，生成视频的文本描述。注1：字符长度不能超过 2000 个字符；注2：若使用is\_rec推荐提示词参数，模型将不考虑此参数所输入的提示词 长度限制：0 - 2000 

 水印内容，此处为图片URL。不传时，使用默认水印：内容由AI生成 

 透传参数，不做任何处理，仅数据传输。最多 1048576个字符。 长度限制：0 - 1048576 

 视频时长（秒），支持 1-8 秒 可选值：`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` 

 错峰模式。true：错峰生成视频（消耗积分更低，48小时内生成）；false：即时生成视频。注：错峰模式下提交的任务，未能完成的任务会被自动取消并返还积分；您也可以手动取消错峰任务。 

 元数据标识，json格式字符串，透传字段，您可以自定义格式或使用示例格式。该参数为空时，默认使用vidu生成的元数据标识。 

 是否添加水印。默认不加水印。您可以通过watermarked\_url参数查询获取带水印的视频内容。 

 输出视频的分辨率。默认值为 720p。 可选值：`540p`, `720p`, `1080p` 

 水印位置，表示水印出现在图片的位置。1：左上角；2：右上角；3：右下角（默认）；4：左下角 可选值：`1`, `2`, `3`, `4` 

 运动幅度，控制视频中物体的运动强度 可选值：`auto`, `small`, `medium`, `large` 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。 

 Provider request ID (optional)
