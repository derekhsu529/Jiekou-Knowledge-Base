---
title: "Untitled"
url: "https://jiekou.ai/models/vidu/vidu-q2-template2video"
crawled_at: "2026-02-26T23:18:47.740412"
---

template*

prompt

0 / 2000

images*

0/3 张

aspect_ratio

area

watermark

seed

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "bgm": false,
  "area": "auto",
  "seed": 0,
  "beast": "auto",
  "watermark": false,
  "wm_position": 3,
  "aspect_ratio": "16:9"
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/vidu-q2-template2video' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "bgm": false,
  "area": "auto",
  "seed": 0,
  "beast": "auto",
  "watermark": false,
  "wm_position": 3,
  "aspect_ratio": "16:9"
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
