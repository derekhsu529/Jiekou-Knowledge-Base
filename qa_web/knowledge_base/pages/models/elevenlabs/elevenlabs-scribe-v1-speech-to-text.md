---
title: "Untitled"
url: "https://jiekou.ai/models/elevenlabs/elevenlabs-scribe-v1-speech-to-text"
crawled_at: "2026-02-26T23:28:34.761665"
---

cloud_storage_url*

seed

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "seed": 0,
  "diarize": false,
  "file_format": "other",
  "temperature": 0,
  "num_speakers": 1,
  "tag_audio_events": true,
  "use_multi_channel": false,
  "diarization_threshold": 0.1,
  "timestamps_granularity": "word"
}

API

curl --location --request POST 'https://api.jiekou.ai/v3/elevenlabs-scribe-v1' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "seed": 0,
  "diarize": false,
  "file_format": "other",
  "temperature": 0,
  "num_speakers": 1,
  "tag_audio_events": true,
  "use_multi_channel": false,
  "diarization_threshold": 0.1,
  "timestamps_granularity": "word"
}'
