---
title: "Untitled"
url: "https://jiekou.ai/models/vidu/vidu-q2-turbo-multiframe"
crawled_at: "2026-02-26T23:19:12.803764"
---

start_image*

image_settings*

resolution

watermark

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "watermark": false,
  "resolution": "720p",
  "wm_position": "bottom_left"
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/vidu-q2-turbo-multiframe' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "watermark": false,
  "resolution": "720p",
  "wm_position": "bottom_left"
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
