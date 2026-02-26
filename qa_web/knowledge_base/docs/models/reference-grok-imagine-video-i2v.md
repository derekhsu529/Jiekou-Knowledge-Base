---
title: "Grok Imagine Video 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-grok-imagine-video-i2v.md"
crawled_at: "2026-02-26T23:41:35.547725"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Grok Imagine Video 图生视频

这是一个异步 API，仅返回异步任务的 `task_id`。

<Tip>
  这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。
</Tip>

## 请求头

<ParamField header="Content-Type" type="string" required={true}>
  枚举值: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer 身份验证格式: Bearer \{\{API 密钥}}。
</ParamField>

## 请求体

<ParamField body="image" type="string" required={true}>
  用于视频生成的输入图片 URL。支持公开可访问的图片 URL 或 base64 编码的 data URI（例如 data:image/jpeg;base64,...）。
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  描述要对输入图片施加的运动或变化的文本提示。支持描述场景动态、角色动作和镜头运动等详细提示词。

  长度限制：1 - 4096
</ParamField>

<ParamField body="duration" type="integer" default={6}>
  视频时长，单位为秒（1-15）。视频越长费用越高，按秒计费。

  取值范围：\[1, 15]
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  输出视频分辨率。720p 画质更高，480p 生成更快。

  可选值：`720p`, `480p`
</ParamField>

<ParamField body="aspect_ratio" type="string">
  生成视频的宽高比。如果不指定，默认使用输入图片的宽高比。如果指定，将覆盖原始比例并拉伸图片。

  可选值：`16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`
</ParamField>

## 响应

<ResponseField name="task_id" type="string" required={true}>
  使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
</ResponseField>
