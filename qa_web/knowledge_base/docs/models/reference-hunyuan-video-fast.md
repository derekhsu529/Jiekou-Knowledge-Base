---
title: "Hunyuan 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-hunyuan-video-fast.md"
crawled_at: "2026-02-26T23:32:42.012690"
---

Published Time: Thu, 26 Feb 2026 15:32:41 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Hunyuan 文生视频

HunyuanVideo 是一款业界领先的文生视频生成模型，可以根据文本描述生成高质量、真实运动的视频。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 模型名称。 支持：`hunyuan-video-fast`。 

 输出视频的宽度。 支持：`720`、`1280`。 

 输出视频的高度。 支持： * 当 `width` 为 `1280` 时，`height` 为 `720` * 当 `width` 为 `720` 时，`height` 为 `1280` 

 随机种子，用于生成噪声，使生成结果可复现。相同的种子和参数会产生相同的内容。 取值范围：`-1 <= x <= 9999999999`。 

 去噪步数。步数越多通常生成效果越好，但耗时也更长。 取值范围：`2 <= x <= 30`。 

 指导生成所需的提示词。 取值范围：`1 <= x <= 2000`。 

## 返回结果

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
