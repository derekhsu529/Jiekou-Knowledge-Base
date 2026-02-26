---
title: "Untitled"
url: "https://jiekou.ai/models/vidu/vidu-q3-pro-t2v"
crawled_at: "2026-02-26T23:25:33.514908"
---

prompt*

0 / 2000

audio

duration

resolution

aspect_ratio

watermark

seed

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "seed": 0,
  "audio": true,
  "duration": 5,
  "off_peak": false,
  "watermark": false,
  "resolution": "720p",
  "wm_position": 1,
  "aspect_ratio": "16:9"
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/vidu-q3-pro-t2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "seed": 0,
  "audio": true,
  "duration": 5,
  "off_peak": false,
  "watermark": false,
  "resolution": "720p",
  "wm_position": 1,
  "aspect_ratio": "16:9"
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
