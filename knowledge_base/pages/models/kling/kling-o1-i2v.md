---
title: "Untitled"
url: "https://jiekou.ai/models/kling/kling-o1-i2v"
crawled_at: "2026-02-26T23:30:02.987065"
---

prompt*

32 / 2000

image*

![Image 1: Upload 1](https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767954807886-20204c7a522a7fd8)

1/1 张

duration

aspect_ratio

示例结果

示例

请求 JSON

{
  "image": "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767954807886-20204c7a522a7fd8",
  "prompt": "猫咪轻轻眨眼，在温暖的壁炉光线中慵懒地伸展身体，窗外雪花缓缓飘落",
  "duration": 5,
  "aspect_ratio": "16:9"
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/kling-o1-i2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "image": "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767954807886-20204c7a522a7fd8",
  "prompt": "猫咪轻轻眨眼，在温暖的壁炉光线中慵懒地伸展身体，窗外雪花缓缓飘落",
  "duration": 5,
  "aspect_ratio": "16:9"
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
