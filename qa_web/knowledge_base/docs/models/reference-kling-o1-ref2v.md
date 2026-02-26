---
title: "Kling-o1 参考生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-o1-ref2v.md"
crawled_at: "2026-02-26T23:41:43.062200"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling-o1 参考生视频

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

<ParamField body="video" type="string">
  视频URL
</ParamField>

<ParamField body="images" type="array" default="[]">
  包含元素、场景、风格等的参考图片。最多7张

  数组长度：0 - 7
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  正向提示词
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  生成媒体的持续时间（秒）

  可选值：`3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  生成视频的宽高比

  可选值：`16:9`, `9:16`, `1:1`
</ParamField>

<ParamField body="keep_original_sound" type="boolean" default={true}>
  选择是否通过参数保留视频原始声音
</ParamField>

## 响应

<ResponseField name="task_id" type="string" required={true}>
  使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
</ResponseField>
