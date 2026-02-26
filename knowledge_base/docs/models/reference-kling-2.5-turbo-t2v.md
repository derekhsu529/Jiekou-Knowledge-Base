---
title: "Kling V2.5 Turbo 文生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-2.5-turbo-t2v.md"
crawled_at: "2026-02-26T23:41:39.013102"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.5 Turbo 文生视频

Kling 2.5 Turbo 是一款先进的文本生成视频模型，能够生成超流畅的动作、电影级画面，并高度贴合提示词内容。

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

<ParamField body="prompt" type="string" required={true}>
  指导生成的正向文本提示词。长度不超过 2500 字符。
</ParamField>

<ParamField body="duration" type="string" default="5">
  生成视频的时长（秒）。

  可选值：`5`、`10`
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  输出视频的宽高比。

  可选值：`16:9`、`9:16`、`1:1`
</ParamField>

<ParamField body="cfg_scale" type="number" default={0.5}>
  控制视频生成的灵活性，数值越高，模型生成内容对提示词的贴合度越高，创意自由度越低。

  取值范围：0 到 1
</ParamField>

<ParamField body="mode" type="string" default="pro">
  视频生成模式。可选值：

  * `pro`：专业模式
</ParamField>

<ParamField body="negative_prompt" type="string">
  反向提示词，用于规避不希望出现的内容；长度不超过 2500 字符。
</ParamField>

## 响应

<ResponseField name="task_id" type="string" required={true}>
  异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
</ResponseField>
