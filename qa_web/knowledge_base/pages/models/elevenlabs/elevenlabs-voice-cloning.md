---
title: "Untitled"
url: "https://jiekou.ai/models/elevenlabs/elevenlabs-voice-cloning"
crawled_at: "2026-02-26T23:29:07.640569"
---

E

Elevenlabs Voice Clone
----------------------

音频

[模型 API 文档](https://docs.jiekou.ai/docs/models/reference-elevenlabs-voice-clone)

Elevenlabs 系列提供稳定的生成能力，适合生产场景。该系列面向生产级调用，强调稳定性与可控输出。声音克隆可用少量样本快速复刻音色，便于品牌音色与多角色配音。即时推理 API，性能稳定，无需等待，价格亲民

name*

urls*

0/10 项

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

请求 JSON

{
  "remove_background_noise": false
}

API

### 请求

curl --location --request POST 'https://api.jiekou.ai/v3/elevenlabs-voice-clone' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "remove_background_noise": false
}'
