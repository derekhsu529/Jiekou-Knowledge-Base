---
title: "Untitled"
url: "https://jiekou.ai/models/wan/wan2.6-t2v"
crawled_at: "2026-02-26T23:29:31.835499"
---

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
    "shot_type": "multi",
    "watermark": false,
    "prompt_extend": true
  },
  "input": {
    "prompt": "璀璨的烟花在夜空中绽放，五彩斑斓的光芒如同盛开的花朵，金色、红色、紫色的火焰交织在一起，照亮了漆黑的天空，倒映在平静的湖面上，营造出绚丽梦幻的节日氛围",
    "negative_prompt": "低分辨率、模糊、画面抖动、色彩暗淡、失焦、变形"
  }
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/wan2.6-t2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "parameters": {
    "size": "1920*1080",
    "audio": true,
    "duration": 5,
    "shot_type": "multi",
    "watermark": false,
    "prompt_extend": true
  },
  "input": {
    "prompt": "璀璨的烟花在夜空中绽放，五彩斑斓的光芒如同盛开的花朵，金色、红色、紫色的火焰交织在一起，照亮了漆黑的天空，倒映在平静的湖面上，营造出绚丽梦幻的节日氛围",
    "negative_prompt": "低分辨率、模糊、画面抖动、色彩暗淡、失焦、变形"
  }
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
