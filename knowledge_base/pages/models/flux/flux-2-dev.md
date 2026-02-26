---
title: "Untitled"
url: "https://jiekou.ai/models/flux/flux-2-dev"
crawled_at: "2026-02-26T23:30:47.169180"
---

FLUX 2 DEV | 接口AI
===============

[接口AI 上线 gemini-3.1-pro-preview！100 万 token 超长上下文的多模态强推理模型！](https://jiekou.ai/models/model-detail/gemini-3.1-pro-preview)

[![Image 2: JieKou.AI logo](https://jiekou.ai/logo/jiekou-logo.svg)接口AI](https://jiekou.ai/)

Playground

[Cloud Code](https://cc.jiekou.ai/)

[🔥 资源包](https://jiekou.ai/resource-pack)[价格](https://jiekou.ai/pricing)[文档](https://docs.jiekou.ai/docs/support/quickstart)

登录 开始使用

[首页](https://jiekou.ai/)/FLUX 2 DEV

![Image 3: Flux](https://jiekou.ai/_next/image?url=%2Fmodels%2Flogo%2Fflux-logo.png&w=64&q=75)

FLUX 2 DEV
==========

图像 flux-2-dev

[模型 API 文档](https://docs.jiekou.ai/docs/models/reference-flux-2-dev)

Flux 系列提供稳定的生成能力，适合生产场景。该系列面向生产级调用，强调稳定性与可控输出。适合通用内容生成与工具调用，便于集成到你的生产工作流。即时推理 API，性能稳定，无需等待，价格亲民

Playground 示例 请求 JSON API

prompt* 

116 / 2000

images 

0/3 张

上传图片 添加链接

size 

宽

高

loras 

Add LoRA

seed 

登录后使用$0.012

示例结果

下载

预览 JSON 结果

![Image 4: 示例预览](https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767966567478-acba731c1b360c33.jpg)

Preview

复制

{
  "task": {
    "eta": 0,
    "reason": "",
    "status": "TASK_STATUS_SUCCEED",
    "task_id": "e3222b77-e64f-43fd-8b22-3f57cf0a5088",
    "task_type": "FLUX_2_DEV_TXT_TO_IMG",
    "progress_percent": 0
  },
  "extra": {
    "has_nsfw_contents": [],
    "enable_nsfw_detection": false
  },
  "audios": [],
  "images": [
    {
      "image_url": "https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767966567478-acba731c1b360c33.jpg",
      "image_type": "jpeg",
      "image_url_ttl": "172800",
      "nsfw_detection_result": null
    }
  ],
  "videos": []
}

示例

![Image 5: 示例预览](https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767966567478-acba731c1b360c33.jpg)

A majestic dragon flying over a mystical mountain ...

![Image 6: 示例预览](https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767966573201-15d41414c83cb3fd.jpg)

Transform this image into a Van Gogh starry night ...

![Image 7: 示例预览](https://pub-004dff755de44591aede10e5d025301a.r2.dev/multimodal-assets/2026-01/1767966593155-729a1ad301626fac.jpg)

A cute cyberpunk cat wearing neon glasses in a fut...

请求 JSON

复制

{
  "seed": -1,
  "prompt": "A majestic dragon flying over a mystical mountain range at sunset, highly detailed, fantasy art style, 8k resolution"
}

API

### 提交任务

复制

curl --location --request POST 'https://api.jiekou.ai/v3/async/flux-2-dev' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer ${API_KEY}" \
--data-raw '{
  "seed": -1,
  "prompt": "A majestic dragon flying over a mystical mountain range at sunset, highly detailed, fantasy art style, 8k resolution"
}'

### 查询结果

复制

curl --location --request GET "https://api.jiekou.ai/v3/async/task-result?task_id
=${task_id}" \
--header "Authorization: Bearer ${API_KEY}"

联系我们
