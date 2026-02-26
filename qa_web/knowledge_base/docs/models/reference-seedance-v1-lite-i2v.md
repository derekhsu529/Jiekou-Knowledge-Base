---
title: "Seedance V1 Lite图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-seedance-v1-lite-i2v.md"
crawled_at: "2026-02-26T23:41:47.114197"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedance V1 Lite图生视频

Seedance V1 Lite 是一个 AI 视频模型，专为生成连贯的多镜头视频而设计，提供流畅的运动和对详细提示的精确遵循。它支持 480p、720p 和 1080p 的分辨率。

## 请求头

<ParamField header="Content-Type" type="string" required={true}>
  枚举值: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer 身份验证格式: Bearer \{\{API 秘钥}}。
</ParamField>

## 请求体

<ParamField body="prompt" type="string">
  视频生成的文本提示；正面文本提示；支持中英文，建议不超过 500 字。
</ParamField>

<ParamField body="image" type="string" required={true}>
  输入图像支持 URL 和 Base64 格式。

  * 图片格式：`jpeg`、`png`、`webp`、`bmp`、`tiff`、`gif`。
  * 图片文件大小不能超过 30MB。
  * 图片的短边需大于 300 像素，长边需小于 6000 像素。
  * 宽高比要求在 0.4 到 2.5 之间。
</ParamField>

<ParamField body="resolution" type="string" required={true}>
  视频质量。可接受的值：`480p`，`720p`，`1080p`
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  生成视频的长宽比。
  可接受的值：`21:9`，`16:9`，`4:3`，`1:1`，`3:4`，`9:16`
</ParamField>

<ParamField body="last_image" type="string">
  结束图像，支持 URL 和 Base64 格式。

  * 图片格式：`jpeg`、`png`、`webp`、`bmp`、`tiff`、`gif`。
  * 图片文件大小不能超过 30MB。
  * 图片的短边需大于 300 像素，长边需小于 6000 像素。
  * 宽高比要求在 0.4 到 2.5 之间。

  传入的首尾帧图片可相同。首尾帧图片的宽高比不一致时，以首帧图片为主，尾帧图片会自动裁剪适配。
</ParamField>

<ParamField body="camera_fixed" type="boolean" default={false}>
  确定相机位置是否应保持固定。
</ParamField>

<ParamField body="seed" type="integer" default={-1} minimum={-1} maximum={2147483647}>
  用于生成的随机种子。-1 表示将使用随机种子。
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  指定生成视频的长度（以秒为单位）。可用选项：`5`，`10`
</ParamField>

## 响应

<ResponseField name="task_id" type="string" required={true}>
  异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
</ResponseField>
