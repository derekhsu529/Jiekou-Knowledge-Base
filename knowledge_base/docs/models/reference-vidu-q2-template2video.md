---
title: "VIDU Q2 场景模板"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-q2-template2video.md"
crawled_at: "2026-02-26T23:36:09.644335"
---

Published Time: Thu, 26 Feb 2026 15:36:09 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# VIDU Q2 场景模板

根据场景模板和输入图像生成特效视频。支持多种场景模板，不同模板支持不同的特效参数。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 是否为生成的视频添加背景音乐。默认：false。传 true 时系统将从预设 BGM 库中自动挑选合适的音乐并添加；不传或为 false 则不添加 BGM。BGM 不限制时长，系统根据视频时长自动适配 

 异域公主特效专属参数。仅当 template 传 exotic\_princess 时可用。默认：auto 可选值：`auto`, `denmark`, `uk`, `africa`, `china`, `mexico`, `switzerland`, `russia`, `italy`, `korea`, `thailand`, `india`, `japan` 

 随机种子。当默认不传或者传 0 时，会使用随机数替代；手动设置则使用设置的种子 

 与兽同行特效专属参数。仅当 template 传 beast\_companion 时可用。默认：auto 可选值：`auto`, `bear`, `tiger`, `elk`, `snake`, `lion`, `wolf` 

 输入图像列表。模型将以此参数中传入的图片来生成视频。支持传入图片 Base64 编码或图片 URL（确保可访问）。图片支持 png、jpeg、jpg、webp 格式。图片比例需要小于 1:4 或 4:1，大小不超过 50MB。Base64 decode 之后的字节长度需要小于 10M，且编码必须包含适当的内容类型字符串，例如：`data:image/png;base64,{base64_encode}` 数组长度：1 - 无限制 

 文本提示词，生成视频的文本描述。注：当 template=subject\_3、pubg\_winner\_hit 时，提示词非必传 

 水印内容，此处为图片 URL。不传时，使用默认水印：内容由 AI 生成 

 透传参数，不做任何处理，仅数据传输。最多 1048576 个字符 长度限制：0 - 1048576 

 场景模板参数。不同的场景模板对应不同的调用参数。常见模板：subject\_3（人物换装）、pubg\_winner\_hit（吃鸡特效）、exotic\_princess（异域公主）、beast\_companion（与兽同行）等，具体模板请参考：[https://platform.vidu.cn/docs/templates](https://platform.vidu.cn/docs/templates) 

 元数据标识，json 格式字符串，透传字段。您可以自定义格式或使用示例格式。该参数为空时，默认使用 vidu 生成的元数据标识。示例格式：`{"Label": "your_label", "ContentProducer": "your_content_producer", "ContentPropagator": "your_content_propagator", "ProduceID": "your_product_id", "PropagateID": "your_propagate_id", "ReservedCode1": "your_reserved_code1", "ReservedCode2": "your_reserved_code2"}` 

 是否添加水印。true：添加水印；false：不添加水印。目前水印内容为固定，内容由 AI 生成，默认不加。您可以通过 watermarked\_url 参数查询获取带水印的视频内容 

 水印位置，表示水印出现在图片的位置。1：左上角；2：右上角；3：右下角；4：左下角。默认为 3 可选值：`1`, `2`, `3`, `4` 

 视频比例。默认 16:9，可选值：16:9、9:16。不同 template 支持的可选值不同，详情见模版说明 可选值：`16:9`, `9:16` 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。 

 提供商请求 ID（可选）
