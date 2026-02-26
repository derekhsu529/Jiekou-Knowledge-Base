---
title: "Untitled"
url: "https://jiekou.ai/models/vidu/vidu-q2-reference2video"
crawled_at: "2026-02-26T23:19:05.837974"
---

subjects*

prompt*

0 / 2000

audio

duration*

resolution

aspect_ratio

watermark

seed

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "bgm": false,
  "seed": 0,
  "audio": false,
  "duration": 5,
  "watermark": false,
  "resolution": "720p"
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/vidu-q2-reference2video' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "bgm": false,
  "seed": 0,
  "audio": false,
  "duration": 5,
  "watermark": false,
  "resolution": "720p"
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
