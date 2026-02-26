---
title: "Veo 3.1 视频生成 (Reverse)"
url: "https://docs.jiekou.ai/docs/models/reference-veo-3.1-reverse.md"
crawled_at: "2026-02-26T23:35:41.529253"
---

Published Time: Thu, 26 Feb 2026 15:35:41 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Veo 3.1 视频生成 (Reverse)

Veo 3.1 视频生成与查询 API

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 宽x高，会忽略具体数据 宽>高 为横屏，宽\<高为竖屏，支持值: 1280x720，720x1280 

 提示词，用于引导视频的生成。例如：图像中形象赛跑起来然后相互碰撞 

 视频时长，目前仅支持 8 秒 

 是否需要水印，默认无水印 

 用于指导生成视频的图片文件，veo-3.1-reverse 支持上传首帧和尾帧 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
