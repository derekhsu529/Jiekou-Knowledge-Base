---
title: "Vidu Q3 Pro 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-q3-pro-t2v.md"
crawled_at: "2026-02-26T23:36:21.665591"
---

Published Time: Thu, 26 Feb 2026 15:36:21 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu Q3 Pro 文生视频

这是一个异步 API，仅返回异步任务的 `task_id`。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 随机种子，用于结果可复现。使用 0 表示随机。 取值范围：\[0, 2147483647] 

 是否使用音视频直出能力（包括台词和音效）。仅 Q3 模型支持该参数。 

 视频生成的文本描述，最多 2000 个字符。 长度限制：0 - 2000 

 水印图片 URL。 

 视频时长（秒），范围 1-16。 取值范围：\[1, 16] 

 使用错峰模式。任务将在 48 小时内处理，费用更低。 

 是否添加水印。 

 输出视频画质。 可选值：`540p`, `720p`, `1080p` 

 水印位置：1=左上, 2=右上, 3=左下, 4=右下。 取值范围：\[1, 4] 

 输出视频宽高比。 可选值：`16:9`, `9:16`, `4:3`, `3:4`, `1:1` 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
