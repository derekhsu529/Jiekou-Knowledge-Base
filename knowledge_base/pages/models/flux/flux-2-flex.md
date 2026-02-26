---
title: "Untitled"
url: "https://jiekou.ai/models/flux/flux-2-flex"
crawled_at: "2026-02-26T23:30:40.105691"
---

prompt*

26 / 2000

images

![Image 1: Upload 1](https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767953909502-66a2a0e5a6c9ce25.jpeg)

1/3 张

size

seed

示例结果

![Image 2: 示例预览](https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767961364977-06564c2b72581e40.jpeg)

Preview

示例

请求 JSON

{
  "seed": 42,
  "size": "1024*1024",
  "images": [
    "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767953909502-66a2a0e5a6c9ce25.jpeg"
  ],
  "prompt": "将这只猫咪转换为油画风格，增加厚重的笔触和浓郁的色彩"
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/flux-2-flex' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "seed": 42,
  "size": "1024*1024",
  "images": [
    "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767953909502-66a2a0e5a6c9ce25.jpeg"
  ],
  "prompt": "将这只猫咪转换为油画风格，增加厚重的笔触和浓郁的色彩"
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
