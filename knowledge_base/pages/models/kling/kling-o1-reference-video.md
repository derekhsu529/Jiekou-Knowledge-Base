---
title: "Untitled"
url: "https://jiekou.ai/models/kling/kling-o1-reference-video"
crawled_at: "2026-02-26T23:30:11.447028"
---

prompt*

0 / 2000

images

0/7 张

duration

aspect_ratio

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "duration": 5,
  "aspect_ratio": "16:9",
  "keep_original_sound": true
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/kling-o1-ref2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "duration": 5,
  "aspect_ratio": "16:9",
  "keep_original_sound": true
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
