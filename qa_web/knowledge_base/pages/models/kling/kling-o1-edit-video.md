---
title: "Untitled"
url: "https://jiekou.ai/models/kling/kling-o1-edit-video"
crawled_at: "2026-02-26T23:30:18.467770"
---

video*

prompt*

8 / 2000

images

0/4 张

fast_mode

aspect_ratio

示例结果

示例

请求 JSON

{
  "video": "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767965885719-1ac79691fd90c371.mp4",
  "prompt": "一只快乐的小松鼠",
  "fast_mode": false,
  "keep_original_sound": true
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/kling-o1-video-edit' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "video": "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767965885719-1ac79691fd90c371.mp4",
  "prompt": "一只快乐的小松鼠",
  "fast_mode": false,
  "keep_original_sound": true
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
