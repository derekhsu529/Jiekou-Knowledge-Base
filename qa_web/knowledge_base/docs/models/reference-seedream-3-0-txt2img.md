---
title: "Seedream 文生图 3.0"
url: "https://docs.jiekou.ai/docs/models/reference-seedream-3-0-txt2img.md"
crawled_at: "2026-02-26T23:35:06.370525"
---

Published Time: Thu, 26 Feb 2026 15:35:06 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedream 文生图 3.0

Seedream 3.0 是一款先进的文生图模型，可以根据文本提示高效且快速地生成高质量图片。

 Currently, only the model version `seedream-3-0-t2i-250415` is supported for Seedream 3.0. 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 用于生成图片的文本提示词。 

 本次请求所使用的模型 ID 或推理 Endpoint ID。目前仅支持 Seedream 3.0 的 `seedream-3-0-t2i-250415`。 

 指定响应中返回的图片格式。默认值为 `url`。

 支持的取值：

 * `"url"`：返回可下载的 JPEG 图片链接。 * `"b64_json"`：返回 base64 编码的图片 JSON 字符串。 

 指定生成图片的尺寸（像素，宽 x 高），范围为 \[512x512, 2048x2048]。默认值为 `1024x1024`。

 推荐的宽高比及分辨率：

 * `1024x1024`（1:1） * `864x1152`（3:4） * `1152x864`（4:3） * `1280x720`（16:9） * `720x1280`（9:16） * `832x1248`（2:3） * `1248x832`（3:2） * `1512x648`（21:9） 

 控制图片生成随机性的种子值。取值范围：\[-1, 2147483647]。如不指定，将自动生成。若想复现相同结果，请使用相同的 seed。默认为 `-1`。 

 控制输出图片与输入提示词的契合度。数值越高，模型自由度越小，与提示词的相关性越强。取值范围：\[1, 10]。默认值为 `2.5`。 

 是否给生成图片加水印。默认值为 `true`。

 * `false`：不添加水印 * `true`：在图片右下角添加“AI generated”水印 

## 响应

 生成图片的链接数组。当 `response_format` 设置为 `"url"` 时，该数组包含生成图片的可下载链接。 

 Base64 编码的图片数据数组。当 `response_format` 设置为 `"b64_json"` 时，该数组包含以 Base64 编码的图片 JSON 字符串。
