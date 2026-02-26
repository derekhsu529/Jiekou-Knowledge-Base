---
title: "Kling-o1 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-o1-i2v.md"
crawled_at: "2026-02-26T23:41:40.613246"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling-o1 图生视频

这是一个异步 API，仅返回异步 task\_id。你需要使用 task\_id 调用任务结果查询 API 获取生成结果。

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
  首帧是第一帧
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  生成的正向提示词
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  生成媒体的持续时间（秒）

  可选值：`5`, `10`
</ParamField>

<ParamField body="last_image" type="string">
  末帧是最后一帧
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  生成视频的宽高比

  可选值：`16:9`, `9:16`, `1:1`
</ParamField>

## 响应

<ResponseField name="task_id" type="string" required={true}>
  使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
</ResponseField>
