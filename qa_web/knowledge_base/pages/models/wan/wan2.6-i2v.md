---
title: "Untitled"
url: "https://jiekou.ai/models/wan/wan2.6-i2v"
crawled_at: "2026-02-26T23:29:22.116018"
---

input.prompt

0 / 2000

input.img_url*

parameters.audio

input.audio_url

parameters.duration

parameters.resolution

parameters.watermark

parameters.seed

示例结果

示例

请求 JSON

{
  "parameters": {
    "duration": 5,
    "shot_type": "single",
    "watermark": false,
    "resolution": "1080P",
    "prompt_extend": true
  },
  "input": {
    "prompt": "一只可爱的白猫在雨夜的屋顶上玩耍彩色毛线球，霓虹灯光倒映在湿润的地面，镜头缓缓推近",
    "img_url": "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767962301809-86afb2567676e093.png"
  }
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/wan2.6-i2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "parameters": {
    "duration": 5,
    "shot_type": "single",
    "watermark": false,
    "resolution": "1080P",
    "prompt_extend": true
  },
  "input": {
    "prompt": "一只可爱的白猫在雨夜的屋顶上玩耍彩色毛线球，霓虹灯光倒映在湿润的地面，镜头缓缓推近",
    "img_url": "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767962301809-86afb2567676e093.png"
  }
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
