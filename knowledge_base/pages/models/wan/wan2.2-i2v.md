---
title: "Untitled"
url: "https://jiekou.ai/models/wan/wan2.2-i2v"
crawled_at: "2026-02-26T23:26:19.132678"
---

input.prompt

0 / 2000

input.img_url*

parameters.audio

input.audio_url

parameters.duration

parameters.resolution

parameters.loras

parameters.watermark

parameters.seed

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "parameters": {
    "seed": 0,
    "audio": false,
    "duration": 5,
    "watermark": false,
    "resolution": "480P",
    "prompt_extend": false
  }
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/wan-2.2-i2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "parameters": {
    "seed": 0,
    "audio": false,
    "duration": 5,
    "watermark": false,
    "resolution": "480P",
    "prompt_extend": false
  }
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
