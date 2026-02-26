---
title: "Kling V2.1 Master 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-v2.1-i2v-master.md"
crawled_at: "2026-02-26T23:33:08.228597"
---

Published Time: Thu, 26 Feb 2026 15:33:07 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.1 Master 图生视频

Kling 2.1 Master 是 Kling 2.1 系列的旗舰版本，具备顶级图生视频生成能力，拥有极致的运动流畅性、电影级视觉效果、卓越的提示词理解力，并支持 1080p 高清视频输出。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 视频的首帧图片；支持的图片格式包括 `.jpg`、`.jpeg`、`.png`；图片文件大小不得超过 10MB，分辨率不小于 300\*300 像素。 

 生成视频的正向提示词文本；不可超过 2500 个字符。 

 生成视频的时长（单位：秒）。 可选值：`5`、`10` 

 指导强度参数，控制生成内容与提示词的贴合程度。 取值范围：0 到 1

 步长：0.01 

 反向提示词，用于规避不希望出现的内容；长度不超过 2500 字符。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
