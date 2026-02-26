---
title: "Untitled"
url: "https://jiekou.ai/models/elevenlabs/elevenlabs-flash-v2-text-to-speech"
crawled_at: "2026-02-26T23:28:20.939146"
---

voice_id*

text*

voice_settings.speed

seed

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "seed": 0,
  "output_format": "mp3_44100_128",
  "use_pvc_as_ivc": false,
  "voice_settings": {
    "speed": 1,
    "style": 0,
    "stability": 0.5,
    "similarity_boost": 0.75,
    "use_speaker_boost": true
  },
  "apply_text_normalization": "auto",
  "apply_language_text_normalization": false
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/elevenlabs-tts-flash-v2' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "seed": 0,
  "output_format": "mp3_44100_128",
  "use_pvc_as_ivc": false,
  "voice_settings": {
    "speed": 1,
    "style": 0,
    "stability": 0.5,
    "similarity_boost": 0.75,
    "use_speaker_boost": true
  },
  "apply_text_normalization": "auto",
  "apply_language_text_normalization": false
}'
