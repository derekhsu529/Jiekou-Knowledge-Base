---
title: "Wan 2.2 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-wan-2.2-i2v.md"
crawled_at: "2026-02-26T23:36:23.873960"
---

Published Time: Thu, 26 Feb 2026 15:36:23 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.2 图生视频

Wan 2.2（万相 2.2）专业版图生视频模型根据首帧图像和文本。在画面细节表现、运动稳定性方面均有显著提升。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 输入的基本信息，如提示词等。   文本提示词。支持中英文，长度不超过 800 个字符，每个汉字/字母占一个字符，超过部分会自动截断。 示例值：一只小猫在草地上奔跑。   反向提示词，用来描述不希望在视频画面中看到的内容，可以对视频画面进行限制。 支持中英文，长度不超过 500 个字符，超过部分会自动截断。 示例值：低分辨率、错误、最差质量、低质量、残缺、多余的手指、比例不良等。   生成视频时所使用的首帧图像的 URL。 URL 需为公网可访问地址，支持 HTTP 或 HTTPS 协议。 图像限制： * 图像格式：JPEG、JPG、PNG（不支持透明通道）、BMP、WEBP。 * 图像分辨率：图像的宽度和高度范围为\[360, 2000]，单位为像素。 * 文件大小：不超过 10MB。  

 视频处理参数，如指定输出视频的分辨率、视频时长等。   生成视频的分辨率档位。默认值为 `1080P`。

 可选值：`480P`、`720P`、`1080P`   生成视频的时长。 * `480P` 和 `720P` 分辨率，支持时长为 `5` 或 `8` 秒。 * `1080P` 分辨率时，时长固定为 5 秒。 默认值：`5`。   是否开启 prompt 智能改写。开启后使用大模型对输入 prompt 进行智能改写。对于较短的 prompt 生成效果提升明显，但会增加耗时。 * `true`：默认值，开启智能改写。 * `false`：不开启智能改写。 示例值：true。   随机数种子，用于控制模型生成内容的随机性。取值范围为 `[0, 2147483647]`。 如果不提供，则算法自动生成一个随机数作为种子。如果希望生成内容保持相对稳定，可以使用相同的 seed 参数值。 示例值：12345。   要应用的 LoRA 列表（最多 3 个）。   LoRA 模型的路径   LoRA 模型的作用强度 取值范围：0.0 \~ 4.0    

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
