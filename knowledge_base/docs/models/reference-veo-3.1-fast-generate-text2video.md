---
title: "Veo 3.1 Fast 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-veo-3.1-fast-generate-text2video.md"
crawled_at: "2026-02-26T23:35:35.452221"
---

Published Time: Thu, 26 Feb 2026 15:35:35 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Veo 3.1 Fast 文生视频

 Veo 3.1 Preview 版本 API 已自动兼容到本接口 

使用 Veo 3.1 Fast 视频生成模型，通过文本描述生成高质量视频内容。该接口采用异步处理方式，需要通过 task\_id 查询最终生成结果。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 描述您想要生成的视频的文本字符串。 

 指定生成视频的宽高比。 枚举值: `16:9`、`9:16`。默认值为 `16:9`。 

 您想要生成的视频文件的长度（秒）。 枚举值: `4`、`6`、`8`。默认值为 `8`。 

 指定是否使用 Gemini 增强您的提示词。仅支持 `true`。 默认值: `true` 

 指定是否为视频生成音频。 

 描述您想要阻止模型生成的内容的文本字符串。 

 控制是否允许人物或面部生成的安全设置。 枚举值: * `allow_adult` (默认): 仅允许生成成人 * `dont_allow`: 不允许在图像中包含人物或面部 

 生成视频的分辨率。 枚举值: `720p` (默认) 或 `1080p` 

 要生成的视频数量。 取值范围: 1-4 

 用于初始化随机生成过程的数字。使用相同的种子、提示词和其他参数会产生相同的输出视频，使生成过程具有确定性。 取值范围: 0-4,294,967,295 

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
