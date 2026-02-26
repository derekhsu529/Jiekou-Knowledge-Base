---
title: "Untitled"
url: "https://jiekou.ai/models/wan/wan2.6-v2v"
crawled_at: "2026-02-26T23:29:14.675999"
---

input.reference_urls*

0/3 项 (最少 1 项)

格式mp4，mov，数量1-3条，单条长度2-30s，单文件小于30MB，与audio不能同时输入

input.prompt*

0 / 2000

parameters.audio

input.audio_url

parameters.duration

parameters.size

parameters.watermark

parameters.seed

示例结果

示例

请求 JSON

{
  "parameters": {
    "size": "1920*1080",
    "audio": true,
    "duration": 5,
    "shot_type": "single",
    "watermark": false,
    "prompt_extend": true
  },
  "input": {
    "prompt": "character1在阳光明媚的草地上奔跑，背景是蓝天白云，画面充满活力与生机",
    "reference_video_urls": [
      "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767961636922-40238eb7ceb3f19b.mp4"
    ]
  }
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/wan2.6-v2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "parameters": {
    "size": "1920*1080",
    "audio": true,
    "duration": 5,
    "shot_type": "single",
    "watermark": false,
    "prompt_extend": true
  },
  "input": {
    "prompt": "character1在阳光明媚的草地上奔跑，背景是蓝天白云，画面充满活力与生机",
    "reference_video_urls": [
      "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767961636922-40238eb7ceb3f19b.mp4"
    ]
  }
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
