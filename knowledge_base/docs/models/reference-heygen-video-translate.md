---
title: "Heygen Video-translate"
url: "https://docs.jiekou.ai/docs/models/reference-heygen-video-translate.md"
crawled_at: "2026-02-26T23:41:36.763721"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Heygen Video-translate

使用自然语音克隆和精准唇形同步将视频翻译成 175+ 种语言

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

<ParamField body="video" type="string" required={true}>
  要翻译的视频 URL。必须可公开访问。支持直接 URL、Google Drive 和 YouTube 链接。
</ParamField>

<ParamField body="output_language" type="string" required={true}>
  翻译目标语言。支持 70+ 种语言和 175+ 种方言,提供自然语音克隆和唇形同步调整。

  可选值：`English`, `English (Australia)`, `English (India)`, `English (UK)`, `English (US)`, `Spanish`, `Spanish (Mexico)`, `Spanish (Spain)`, `French`, `French (Canada)`, `French (France)`, `Hindi`, `Italian`, `German`, `Polish`, `Portuguese`, `Portuguese (Brazil)`, `Portuguese (Portugal)`, `Chinese`, `Chinese (Cantonese, Traditional)`, `Chinese (Mandarin, Simplified)`, `Chinese (Mandarin, Traditional)`, `Japanese`, `Dutch`, `Turkish`, `Korean`, `Danish`, `Arabic`, `Romanian`, `Mandarin`, `Filipino`, `Swedish`, `Indonesian`, `Ukrainian`, `Greek`, `Czech`, `Bulgarian`, `Malay`, `Slovak`, `Croatian`, `Tamil`, `Finnish`, `Russian`
</ParamField>

## 响应

<ResponseField name="task_id" type="string" required={false}>
  使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
</ResponseField>
