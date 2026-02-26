---
title: "VIDU Q2 Turbo 智能多帧"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-q2-turbo-multiframe.md"
crawled_at: "2026-02-26T23:36:15.783187"
---

Published Time: Thu, 26 Feb 2026 15:36:15 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# VIDU Q2 Turbo 智能多帧

通过多张关键帧图像快速生成连贯视频。支持 540p、720p、1080p 三种分辨率。Turbo 版本在生成速度和视频质量之间取得平衡。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 水印图片URL。启用水印但不传自定义水印URL时，使用默认水印。不添加水印则该参数无效。 

 透传参数。不做任何处理，仅数据传输。最多 1048576 个字符。 

 元数据标识，JSON格式字符串。透传字段。 

 是否添加水印。true：添加水印；false：不添加水印。默认不添加。 

 视频分辨率。默认为 720p。 可选值：`540p`, `720p`, `1080p` 

 首帧图像。支持传入图片 Base64 编码或图片URL。只支持输入 1 张图。支持 png、jpeg、jpg、webp 格式。图片比例需要小于 1:4 或者 4:1。图片大小不超过 50 MB。 

 水印位置。默认为左下。不添加水印则该参数无效。 可选值：`top_left`, `top_right`, `bottom_right`, `bottom_left` 

 关键帧配置数组，每个任务最少 2 个关键帧，最多 9 个关键帧 数组长度：2 - 9   上一张图像继续延长的提示词，用来控制延长的视频内容。   多帧时长。不同关键帧之间的视频时长。默认 5s，可选项为 2～7s。 取值范围：\[2, 7]   中间帧的参考图像。模型将此参数中的图片作为尾帧生成视频。支持传入图片 Base64 编码或图片URL。只支持输入 1 张图。输入顺序即为时间轴顺序（从首帧到尾帧）。支持 png、jpeg、jpg、webp 格式。图片比例需要小于 1:4 或者 4:1。图片大小不超过 50 MB。  

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。 

 Provider request ID (optional)
