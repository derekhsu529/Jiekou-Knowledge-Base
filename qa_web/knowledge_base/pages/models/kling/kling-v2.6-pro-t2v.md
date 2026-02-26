---
title: "Untitled"
url: "https://jiekou.ai/models/kling/kling-v2.6-pro-t2v"
crawled_at: "2026-02-26T23:19:19.956099"
---

prompt*

64 / 2000

duration

aspect_ratio

示例结果

示例

请求 JSON

{
  "sound": true,
  "prompt": "壮丽的山川风景，晨曦中的群山被金色阳光照耀，云海翻涌在山谷之间，瀑布从悬崖飞流直下，溅起水雾，镜头缓缓推进，展现大自然的磅礴气势",
  "duration": 5,
  "cfg_scale": 0.7,
  "aspect_ratio": "16:9",
  "negative_prompt": "模糊, 低质量, 人物, 文字, 水印"
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/kling-v2.6-pro-t2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "sound": true,
  "prompt": "壮丽的山川风景，晨曦中的群山被金色阳光照耀，云海翻涌在山谷之间，瀑布从悬崖飞流直下，溅起水雾，镜头缓缓推进，展现大自然的磅礴气势",
  "duration": 5,
  "cfg_scale": 0.7,
  "aspect_ratio": "16:9",
  "negative_prompt": "模糊, 低质量, 人物, 文字, 水印"
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
