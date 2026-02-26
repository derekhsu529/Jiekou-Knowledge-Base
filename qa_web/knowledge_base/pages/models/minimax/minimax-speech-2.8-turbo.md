---
title: "Untitled"
url: "https://jiekou.ai/models/minimax/minimax-speech-2.8-turbo"
crawled_at: "2026-02-26T23:26:03.928374"
---

voice_setting.voice_id*

text*

voice_setting.speed

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "stream": false,
  "voice_modify": {
    "pitch": -100,
    "timbre": -100,
    "intensity": -100
  },
  "audio_setting": {
    "format": "mp3",
    "bitrate": 128000,
    "channel": 1,
    "force_cbr": false,
    "sample_rate": 32000
  },
  "output_format": "hex",
  "voice_setting": {
    "vol": 1,
    "pitch": 0,
    "speed": 1,
    "latex_read": false,
    "text_normalization": false
  },
  "aigc_watermark": false,
  "stream_options": {
    "exclude_aggregated_audio": false
  },
  "subtitle_enable": false,
  "continuous_sound": false
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/minimax-speech-2.8-turbo' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "stream": false,
  "voice_modify": {
    "pitch": -100,
    "timbre": -100,
    "intensity": -100
  },
  "audio_setting": {
    "format": "mp3",
    "bitrate": 128000,
    "channel": 1,
    "force_cbr": false,
    "sample_rate": 32000
  },
  "output_format": "hex",
  "voice_setting": {
    "vol": 1,
    "pitch": 0,
    "speed": 1,
    "latex_read": false,
    "text_normalization": false
  },
  "aigc_watermark": false,
  "stream_options": {
    "exclude_aggregated_audio": false
  },
  "subtitle_enable": false,
  "continuous_sound": false
}'
