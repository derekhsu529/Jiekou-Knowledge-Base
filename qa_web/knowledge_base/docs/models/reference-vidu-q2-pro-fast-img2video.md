---
title: "VIDU Q2 Pro Fast 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-q2-pro-fast-img2video.md"
crawled_at: "2026-02-26T23:41:53.062870"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# VIDU Q2 Pro Fast 图生视频

根据参考图像生成新的视频（快速模式）。支持 720p、1080p 两种分辨率。快速模式可显著缩短生成时间，适合对速度要求较高的场景。

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

<ParamField body="bgm" type="boolean" default={false}>
  是否添加背景音乐
</ParamField>

<ParamField body="seed" type="integer">
  随机种子，用于控制生成结果的随机性。相同种子会产生相似的结果。
</ParamField>

<ParamField body="audio" type="boolean" default={false}>
  是否生成音频
</ParamField>

<ParamField body="images" type="array" required={true}>
  输入图片 URL 列表

  数组长度：1 - 无限制
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  文本提示词，详细描述期望生成的视频内容
</ParamField>

<ParamField body="duration" type="integer" required={true} default={5}>
  视频时长（秒），支持 1-10 秒

  可选值：`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
</ParamField>

<ParamField body="off_peak" type="boolean" default={false}>
  是否开启离峰任务模式
</ParamField>

<ParamField body="voice_id" type="string">
  语音 ID，可选
</ParamField>

<ParamField body="watermark" type="boolean" default={false}>
  是否添加水印
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  输出视频的分辨率。支持 720p 和 1080p。默认值为 720p。

  可选值：`720p`, `1080p`
</ParamField>

<ParamField body="movement_amplitude" type="string" default="auto">
  运动幅度，控制视频中物体的运动强度

  可选值：`auto`, `small`, `medium`, `high`
</ParamField>

## 响应

<ResponseField name="task_id" type="string" required={true}>
  使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
</ResponseField>

<ResponseField name="provider_request_id" type="string" required={false}>
  Provider request ID (optional)
</ResponseField>
