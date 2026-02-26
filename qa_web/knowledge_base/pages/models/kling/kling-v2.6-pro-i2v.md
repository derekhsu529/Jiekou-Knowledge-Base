---
title: "Untitled"
url: "https://jiekou.ai/models/kling/kling-v2.6-pro-i2v"
crawled_at: "2026-02-26T23:19:17.367247"
---

prompt*

50 / 2000

image*

![Image 1: Upload 1](https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767954991985-ff0c4e55687ab286.png)

1/1 张

duration

aspect_ratio

示例结果

示例

请求 JSON

{
  "image": "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767954991985-ff0c4e55687ab286.png",
  "sound": true,
  "prompt": "一只可爱的橘色小猫在樱花树下轻轻抬头，花瓣随风飘落，阳光温柔地洒在它身上，小猫眨眨眼睛，轻轻摇动尾巴",
  "duration": 5,
  "cfg_scale": 0.5,
  "aspect_ratio": "16:9"
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/kling-v2.6-pro-i2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "image": "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767954991985-ff0c4e55687ab286.png",
  "sound": true,
  "prompt": "一只可爱的橘色小猫在樱花树下轻轻抬头，花瓣随风飘落，阳光温柔地洒在它身上，小猫眨眨眼睛，轻轻摇动尾巴",
  "duration": 5,
  "cfg_scale": 0.5,
  "aspect_ratio": "16:9"
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
