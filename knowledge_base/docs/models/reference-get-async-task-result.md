---
title: "查询任务结果"
url: "https://docs.jiekou.ai/docs/models/reference-get-async-task-result.md"
crawled_at: "2026-02-26T23:32:19.834018"
---

Published Time: Thu, 26 Feb 2026 15:32:19 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 查询任务结果

「查询任务结果 API」用来获取异步任务返回的图像、音频或视频结果。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 查询参数

 在异步 API 的 200 响应中返回的 task\_id 值。 

## 响应参数

    调试信息   记录请求参数以用于调试。   任务提交时的时间戳（以毫秒为单位）。   任务开始执行时的时间戳（以毫秒为单位）。   任务完成时的时间戳（以毫秒为单位）。    

 任务详细信息。   任务 ID。   任务当前状态。枚举值: * `TASK_STATUS_QUEUED`：任务排队中，等待处理； * `TASK_STATUS_SUCCEED`：任务已成功； * `TASK_STATUS_FAILED`：任务失败； * `TASK_STATUS_PROCESSING`：任务正在处理中；   任务失败原因，当任务失败时，该字段有效。   任务的类型。   任务预计完成时间，以秒为单位。只有部分 API 该字段有效。   任务完成的进度百分比。此功能目前仅适用于：

 1. 视频生成 API; 

 2. 文本到图像 API 和 图像到图像 API。  

 返回与图像类任务的输出图片结果。   图像 URL。   图像 URL 过期时间（以秒为单位）。默认值为 3600 秒。   图像类型。枚举值: `jpeg, png, webp`  

 返回与视频类任务的输出视频结果。   视频 URL。   视频 URL 过期时间（以秒为单位）。默认值为 3600 秒。   视频类型。枚举值: `mp4, gif`  

 返回与音频类任务的输出音频结果。   音频 URL。   音频 URL 过期时间（以秒为单位）。默认值为 3600 秒。   音频类型。枚举值: `wav`   生成的音频文件的详细元数据信息。   音频包含的文本信息。   文本的开始时间（以秒为单位）。   文本的结束时间（以秒为单位）。
