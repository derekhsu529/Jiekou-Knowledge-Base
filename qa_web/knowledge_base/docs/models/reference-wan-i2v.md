---
title: "Wan 2.1 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-wan-i2v.md"
crawled_at: "2026-02-26T23:36:31.498493"
---

Published Time: Thu, 26 Feb 2026 15:36:31 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.1 图生视频

Wan 2.1 14B 图生视频模型的加速推理，这是一套全面且开放的视频基础模型套件，推动了视频生成的边界。默认情况下，API 将生成 5 秒的视频。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 指导生成所需的提示文本。 取值范围：`[1, 2000]`。 

 用于视频生成的图像 URL。 

 负面提示指示模型避免生成哪些元素。 取值范围：`[0, 2000]`。 

 输出视频的宽度。 枚举值：`480`、`720`、`832`、`1280`。 默认：`832`。如果未指定宽度或高度，宽度和高度将被强制设置为 `832` 和 `480`。 

 输出视频的高度。 支持： * (480p) 宽度为 `480` 时高度设置为 `832` * (480p) 宽度为 `832` 时高度设置为 `480` * (720p) 宽度为 `720` 时高度设置为 `1280` * (720p) 宽度为 `1280` 时高度设置为 `720` 默认：`480`。如果未指定宽度或高度，宽度和高度将被强制设置为 `832` 和 `480`。  输出视频将保持输入图像的宽高比，`宽度 x 高度` 设置仅决定输出视频的清晰度。例如，720p 视频将比 480p 视频更清晰。 

 应用于视频生成的 LoRA 模型。 支持最多指定 **3 个 LoRA 模型**。   LoRA 模型的路径。您可以指定来自 Hugging Face 的 LoRA 模型名称，例如：`Remade-AI/Painting`；或来自 Civitai 的模型下载 URL，例如：`https://civitai.com/api/download/models/1513385?type=Model&format=SafeTensor`。  LoRA 模型必须与 Wan2.1 14B I2V 兼容，否则将无法工作。使用前请检查兼容性。    LoRA 的缩放值。值越大，LoRA 效果更明显。number(float32) 类型，取值范围：`[0, 4.0]`。  

 随机数种子，稳定扩散产生噪声的数字，取值范围：`[-1, 9999999999]`。默认值为 -1。 

 迭代步数，图片创建过程的迭代数，取值范围：`[1, 40]`。默认：`30`。 

 引导缩放参数控制生成内容对提示的跟随程度。取值范围：`[0, 10]`。默认：`5.0`。 

 flow\_shift 参数主要影响视频中物体运动的速度和幅度。更高的值产生更明显和更快的运动，而较低的值使运动更慢更细微。 取值范围：`[1, 10]`。默认：`5.0`。 

 enable\_safety\_checker 参数控制是否对生成的内容应用安全过滤器。启用时，它有助于从视频输出中过滤掉潜在的有害或不当内容。 默认：`true`。 

 是否启用快速模式，将更快地生成视频但可能降低质量和价格。 默认：`false`。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
