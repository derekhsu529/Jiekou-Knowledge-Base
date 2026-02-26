---
title: "Untitled"
url: "https://jiekou.ai/models/flux/flux-2-pro"
crawled_at: "2026-02-26T23:19:44.956712"
---

prompt*

135 / 2000

images

0/3 张

size

seed

示例结果

![Image 1: 示例预览](https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767966726002-a60836045e945694.jpg)

Preview

示例

请求 JSON

{
  "seed": 42,
  "size": "1024*1024",
  "prompt": "A majestic phoenix rising from flames, surrounded by golden sparks and mystical energy, highly detailed digital art, cinematic lighting"
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/flux-2-pro' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "seed": 42,
  "size": "1024*1024",
  "prompt": "A majestic phoenix rising from flames, surrounded by golden sparks and mystical energy, highly detailed digital art, cinematic lighting"
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
