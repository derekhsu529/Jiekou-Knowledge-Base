---
title: "Wan 2.5 Preview 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-wan-2.5-i2v-preview.md"
crawled_at: "2026-02-26T23:36:27.679385"
---

Published Time: Thu, 26 Feb 2026 15:36:27 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.5 Preview 图生视频

Wan 2.5 Preview 图生视频模型支持根据首帧图片和文本生成 5 秒或 10 秒的视频。新增音频能力：支持自动配音，也可自定义音频文件。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 基础输入信息，如提示词等。   文本正向提示词。支持中英文，最长 2000 个字符，超出部分自动截断。 示例值：一只小猫在草地上奔跑。   反向提示词，用于描述生成视频时需要避开的内容，可对画面进行规避或限制。 支持中英文，最长500字符，超出部分自动截断。 示例值：低分辨率、错误、最差质量、低质量、残缺、多余的手指、比例不良等。   用于视频生成的起始帧图片的URL。 要求URL可公开访问，并支持HTTP或HTTPS协议。 图片限制： * 图片格式：JPEG、JPG、PNG（不支持透明）、BMP、WEBP； * 尺寸要求：图片宽高需在\[360, 2000]像素范围内； * 文件大小不得超过10MB。   用于视频生成的音频文件URL。详细用法请参考音频设置说明。 音频要求： * 格式：wav、mp3； * 时长：3-30秒； * 文件大小不超过15MB。 超长处理：若音频时长超过目标视频时长（如5秒或10秒），仅保留前5秒或前10秒，其余部分自动舍弃；若音频时长短于视频时长，超出部分为无声视频。例如音频为3秒，视频为5秒，则输出视频前3秒有声音，后2秒为静音。  

 视频处理参数，例如指定输出视频分辨率、时长等。   生成视频的分辨率档位。

 可选：`480P`、`720P`、`1080P`。默认值：`1080P`。   指定生成视频的时长，支持值：`5` 或 `10`（单位：秒）。 默认值：`5`。   是否开启prompt智能改写。开启后，将使用大模型对输入prompt进行智能改写，对较短提示词可显著提升生成效果，但处理时长也会增加。 * `true`：默认，开启智能改写； * `false`：不改写。 示例值：true。   是否添加音频。 参数优先级：audio\_url > audio，仅当 audio\_url 为空时有效。 * `true`：默认，自动为视频添加配音； * `false`：不添加音频，输出为静音视频。 示例值：true。   随机种子，用于控制模型生成内容的随机性，取值范围：\[0, 2147483647]。 不填写时将自动生成随机数。若期望生成结果较为稳定，可传入相同seed值。 示例值：12345。  

## 返回结果

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
