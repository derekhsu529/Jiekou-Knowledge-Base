---
title: "Untitled"
url: "https://jiekou.ai/models/kling/kling-o1-t2v"
crawled_at: "2026-02-26T23:29:55.460376"
---

快手 Kling 系列以运动表现强、镜头控制与编辑能力丰富著称，适合短剧与营销视频。Kling O1 提供参考生成与编辑能力，利于在原视频上做可控修改。文生视频可直接用提示词生成分镜与镜头语言，适合脚本到成片的快速试制。即时推理 API，性能稳定，无需等待，价格亲民

prompt*

0 / 2000

duration

aspect_ratio

待生成

![Image 1: Empty state](https://jiekou.ai/_next/image?url=%2Flogo%2Flogo_small_grey.png&w=384&q=75)

设置参数后点击生成获取结果

示例

请求 JSON

{}

API

curl --location --request POST 'https://api.jiekou.ai/v3/async/kling-o1-t2v' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{}'

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"
