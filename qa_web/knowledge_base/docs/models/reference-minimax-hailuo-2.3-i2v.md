---
title: "Minimax Hailuo 2.3 图生视频"
url: "https://docs.jiekou.ai/docs/models/reference-minimax-hailuo-2.3-i2v.md"
crawled_at: "2026-02-26T23:33:42.237599"
---

Published Time: Thu, 26 Feb 2026 15:33:42 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Minimax Hailuo 2.3 图生视频

Minimax Hailuo 2.3 是全新升级的视频生成模型，在肢体动作、物理效果和对指令的理解与执行能力等方面表现更为出色。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索视频生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 指导生成所需的提示词文本。 范围: `1 <= x <= 2000`。 支持 15 种运镜指令的指令: * 左右移: \[左移], \[右移] * 左右摇: \[左摇], \[右摇] * 推拉: \[推进], \[拉远] * 升降: \[上升], \[下降] * 上下摇: \[上摇], \[下摇] * 变焦: \[变焦推近], \[变焦拉远] * 其他: \[晃动], \[跟随], \[固定] 使用规则: * 组合运镜: 同一组 \[] 内的多个指令会同时生效，如 \[左摇,上升]，建议组合不超过 3 个 * 顺序运镜: prompt 中前后出现的指令会依次生效，如 "...\[推进], 然后...\[拉远]" * 自然语言: 也支持通过自然语言描述运镜，但使用标准指令能获得更准确的响应 

 用于视频生成的图片。支持公网 URL 或 Base64 编码（如 `data:image/jpeg;base64,...`）。 

 生成视频的时长（秒）。默认值：`6`

 可选值：`6`、`10` 

 生成视频的分辨率。默认值：`768P` * 6 秒视频支持：`768P`、`1080P` * 10 秒视频仅支持：`768P` 

 是否启用提示词优化。 默认值: `true`。 

 是否缩短提示词优化的耗时。 默认值: `false`。 

## 响应

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
