---
title: "Untitled"
url: "https://jiekou.ai/models/minimax/minimax-speech-2.8-hd-async"
crawled_at: "2026-02-26T23:25:57.067871"
---

voice_setting.voice_id*

text

voice_setting.speed

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "text_file_id": 0,
  "voice_modify": {
    "pitch": -100,
    "timbre": -100,
    "intensity": -100
  },
  "audio_setting": {
    "format": "mp3",
    "bitrate": 128000,
    "channel": 2,
    "audio_sample_rate": 32000
  },
  "voice_setting": {
    "vol": 1,
    "pitch": 0,
    "speed": 1,
    "english_normalization": false
  },
  "aigc_watermark": false,
  "continuous_sound": false
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/minimax-speech-2.8-hd' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "text_file_id": 0,
  "voice_modify": {
    "pitch": -100,
    "timbre": -100,
    "intensity": -100
  },
  "audio_setting": {
    "format": "mp3",
    "bitrate": 128000,
    "channel": 2,
    "audio_sample_rate": 32000
  },
  "voice_setting": {
    "vol": 1,
    "pitch": 0,
    "speed": 1,
    "english_normalization": false
  },
  "aigc_watermark": false,
  "continuous_sound": false
}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
