---
title: "VIDU Q2 Pro 智能多帧"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-q2-pro-multiframe.md"
crawled_at: "2026-02-26T23:41:54.608594"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# VIDU Q2 Pro 智能多帧

通过多张关键帧图像生成连贯视频。支持 540p、720p、1080p 三种分辨率。

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

<ParamField body="wm_url" type="string">
  水印图片URL。启用水印但不传自定义水印URL时，使用默认水印。不添加水印则该参数无效。
</ParamField>

<ParamField body="payload" type="string">
  透传参数。不做任何处理，仅数据传输。最多 1048576 个字符。
</ParamField>

<ParamField body="meta_data" type="string">
  元数据标识，JSON格式字符串。透传字段。
</ParamField>

<ParamField body="watermark" type="boolean" default={false}>
  是否添加水印。true：添加水印；false：不添加水印。默认不添加。
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  视频分辨率。默认为 720p。

  可选值：`540p`, `720p`, `1080p`
</ParamField>

<ParamField body="start_image" type="string" required={true}>
  首帧图像。支持传入图片 Base64 编码或图片URL。只支持输入 1 张图。支持 png、jpeg、jpg、webp 格式。图片比例需要小于 1:4 或者 4:1。图片大小不超过 50 MB。
</ParamField>

<ParamField body="wm_position" type="string" default="bottom_left">
  水印位置。默认为左下。不添加水印则该参数无效。

  可选值：`top_left`, `top_right`, `bottom_right`, `bottom_left`
</ParamField>

<ParamField body="image_settings" type="array" required={true}>
  关键帧配置数组，每个任务最少 2 个关键帧，最多 9 个关键帧

  数组长度：2 - 9

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="prompt" type="string">
      上一张图像继续延长的提示词，用来控制延长的视频内容。
    </ParamField>

    <ParamField body="duration" type="integer" default={5}>
      多帧时长。不同关键帧之间的视频时长。默认 5s，可选项为 2～7s。

      取值范围：\[2, 7]
    </ParamField>

    <ParamField body="key_image" type="string" required={true}>
      中间帧的参考图像。模型将此参数中的图片作为尾帧生成视频。支持传入图片 Base64 编码或图片URL。只支持输入 1 张图。输入顺序即为时间轴顺序（从首帧到尾帧）。支持 png、jpeg、jpg、webp 格式。图片比例需要小于 1:4 或者 4:1。图片大小不超过 50 MB。
    </ParamField>
  </Expandable>
</ParamField>

## 响应

<ResponseField name="task_id" type="string" required={true}>
  使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
</ResponseField>

<ResponseField name="provider_request_id" type="string" required={false}>
  Provider request ID (optional)
</ResponseField>
