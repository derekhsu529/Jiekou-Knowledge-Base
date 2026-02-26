---
title: "OpenAI Sora 2 (reverse) 生成视频"
url: "https://docs.jiekou.ai/docs/models/reference-sora-2-video-reverse.md"
crawled_at: "2026-02-26T23:35:20.075544"
---

Published Time: Thu, 26 Feb 2026 05:26:08 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Sora 2 (reverse) 生成视频

Sora 2 (reverse) 是一款最先进的视频 + 音频生成器。它在原有 Sora 基础上进行了改进，具备更精确的物理效果、更清晰的真实感、同步的音频、更强的可操控性以及更广泛的风格范围。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 视频生成的正面文本提示。 

 输入图像仅支持 URL 格式，支持的图像格式包括 .jpg、.jpeg、.png。 

 视频时长 (秒) 枚举值：`10`,`15` 

 宽x高，会忽略具体数据 宽 > 高 为横屏，宽 \< 高为竖屏 枚举值： * `1280x720` - 标清横屏（实际输出分辨率约为 480P，价格栏标注为 480P） * `720x1280` - 标清竖屏（实际输出分辨率约为 480P，价格栏标注为 480P） 

 是否需要水印，不传默认无水印 

 创建角色需要的视频链接，注意视频中一定不能出现真人，否则会失败 

 视频角色出现的秒数范围，格式 \{start},\{end}, 注意 end-start 的范围 1～3秒 示例值：`1,3` 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
