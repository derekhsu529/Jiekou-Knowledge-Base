---
title: "Kling V3.0 Pro 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-kling-v3.0-pro-i2v.md"
crawled_at: "2026-02-26T23:33:18.009497"
---

Published Time: Thu, 26 Feb 2026 15:33:17 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V3.0 Pro 图生视频

Kling V3.0 Pro 图生视频可将输入图片生成高质量视频，具有专业级视觉细节、流畅的运动效果，支持首尾帧引导和同步声音生成。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 起始帧图片 URL；支持 .jpg、.jpeg、.png 格式；最大 10MB；最小宽高 300px；宽高比需在 1:2.5 与 2.5:1 之间。 

 启用同步声音生成；设为 true 时生成与视频内容匹配的音频。启用后费用增加 1.5 倍。 

 视频生成的运动描述；描述场景动态、人物动作和镜头运动。 

 视频时长（秒）；支持 3 至 15 秒。 可选值：`3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15` 

 提示词遵循强度；数值越高输出越严格遵循提示词。范围：0.0 到 1.0。 取值范围：\[0, 1] 

 结束帧图片 URL，用于引导过渡；格式限制与 image 相同。提供时模型将生成从起始帧到结束帧的过渡视频。 

 自定义角色对话语音条目；最多 2 条。 数组长度：0 - 2 

 多提示词元素列表，用于包含多个提示词片段的复杂生成场景。 

 需要排除的元素描述；帮助避免不需要的伪影或内容。 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
