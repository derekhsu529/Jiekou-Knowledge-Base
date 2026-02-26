---
title: "KLING V1.6 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-v1.6-i2v.md"
crawled_at: "2026-02-26T23:41:44.260593"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# KLING V1.6 图生视频

KLING V1.6 图生视频是快手 AI 团队开发的 AI 图像生成视频模型。它可以将图片转换为动态的 5 秒视频，支持 720p / 1080p 分辨率，具备高质量的视觉输出、增强的运动与语义理解能力。

<Tip>
  这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。
</Tip>

## 请求头

<ParamField header="Content-Type" type="string" required={true}>
  枚举值: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer 身份验证格式: Bearer \{\{API 秘钥}}。
</ParamField>

## 请求体

<ParamField body="mode" type="string" required={false}>
  视频生成模式。

  支持：

  * `Standard`：快速生成，成本较低，生成 720p 视频。
  * `Professional`：高质量，成本较高，生成 1080p 视频，并允许设置结束帧。

  默认值：`Standard`。
</ParamField>

<ParamField body="image_url" type="string" required={true}>
  用于视频生成的起始帧图片的 URL。
</ParamField>

<ParamField body="end_image_url" type="string" required={false}>
  用于视频生成的结束帧图片的 URL。

  <Warning>仅当 `mode` 为 `Professional` 时可用。</Warning>
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  指导生成所需的提示词。

  取值范围：`1 <= x <= 2000`。
</ParamField>

<ParamField body="negative_prompt" type="string" required={false}>
  负面提示词，用于指示模型应避免生成的内容。

  取值范围：`0 <= x <= 2000`。
</ParamField>

<ParamField body="duration" type="integer" required={false}>
  生成视频的时长（秒）。默认值：`5`。<br />
  可选值：`5`、`10`
</ParamField>

<ParamField body="guidance_scale" type="float" required={false}>
  指导强度参数，控制生成内容与提示词的贴合程度。

  取值范围：`0 <= x <= 1`。默认值：`0.5`。
</ParamField>

## 返回结果

<ResponseField name="task_id" type="string" required={true}>
  异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
</ResponseField>
