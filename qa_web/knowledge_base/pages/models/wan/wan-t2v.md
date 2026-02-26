---
title: "Untitled"
url: "https://jiekou.ai/models/wan/wan-t2v"
crawled_at: "2026-02-26T23:25:23.447821"
---

prompt*

0 / 2000

fast_mode

width

height

steps

loras

watermark

seed

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "seed": -1,
  "steps": 1,
  "width": 832,
  "height": 480,
  "fast_mode": false,
  "watermark": false,
  "flow_shift": 1,
  "guidance_scale": 0,
  "enable_safety_checker": false
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/wan-t2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "seed": -1,
  "steps": 1,
  "width": 832,
  "height": 480,
  "fast_mode": false,
  "watermark": false,
  "flow_shift": 1,
  "guidance_scale": 0,
  "enable_safety_checker": false
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
