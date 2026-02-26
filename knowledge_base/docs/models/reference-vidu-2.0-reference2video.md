---
title: "Vidu 2.0 参考生视频"
url: "https://docs.jiekou.ai/docs/models/reference-vidu-2.0-reference2video.md"
crawled_at: "2026-02-26T23:41:49.388547"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu 2.0 参考生视频

Vidu 2.0 参考生视频使用参考图像和文本描述生成视频。支持各种主体，如角色和物体。通过上传主体的多个视角，您可以创建保持视觉一致性的视频。

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

<ParamField body="images" type="string[]" required={true}>
  模型将使用提供的图像作为参考，生成具有一致主体的视频。

  图像字段要求：

  * 接受 1 至 3 张图像
  * 图像资源可通过 URL 或 Base64 编码提供
  * 必须使用以下格式之一：PNG、JPEG、JPG、WebP
  * 图像尺寸必须至少为 128x128 像素
  * 图像宽高比必须小于 1:4 或 4:1
  * 所有图像限制为 50MB
  * base64 解码后的长度必须小于 10MB，且必须包含适当的内容类型字符串。例如：

  ```
  data:image/png;base64,{base64_encode}
  ```
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  视频生成的文本提示词，最大长度为 1500 个字符。
</ParamField>

<ParamField body="duration" type="integer" required={false}>
  视频持续时间（秒）。默认：4 秒。可选项：`4`。
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  视频生成的随机种子。

  * 默认为随机种子数值
  * 手动设置的值将覆盖默认的随机种子
</ParamField>

<ParamField body="aspect_ratio" type="string" required={false}>
  输出视频的宽高比。默认值：`16:9`<br />
  可选值：`16:9`、`9:16`、`1:1`
</ParamField>

<ParamField body="resolution" type="string" required={false}>
  分辨率参数默认为 360p，可选 `360p` 和 `720p`。
</ParamField>

<ParamField body="movement_amplitude" type="string" required={false}>
  画面中物体的运动幅度。默认值：`auto`<br />
  可选值：`auto`、`small`、`medium`、`large`
</ParamField>

<ParamField body="bgm" type="boolean" required={false}>
  是否为生成的视频添加背景音乐。默认值：`false`<br />
  可选值：`true`、`false`

  当设置为 true 时，系统将自动添加合适的 BGM。BGM 无时长限制，系统会自动适配。
</ParamField>

## 响应

<ResponseField name="task_id" type="string" required={true}>
  异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
</ResponseField>
