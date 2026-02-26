---
title: "Untitled"
url: "https://jiekou.ai/models/kling/kling-v2.6-pro-motion-control"
crawled_at: "2026-02-26T23:19:21.055622"
---

快手 Kling 系列以运动表现强、镜头控制与编辑能力丰富著称，适合短剧与营销视频。Kling 2.6 Pro 强化运镜与动作控制，适合更复杂的镜头调度。运动控制支持更精细的运镜/动作约束，让镜头调度更可控、可复现。即时推理 API，性能稳定，无需等待，价格亲民

video*

character_orientation*

prompt

0 / 2000

image*

0/1 张

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "keep_original_sound": true
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/kling-v2.6-pro-motion-control' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "keep_original_sound": true
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
