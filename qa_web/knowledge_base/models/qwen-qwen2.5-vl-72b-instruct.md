---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/qwen-qwen2.5-vl-72b-instruct"
crawled_at: "2026-02-26T23:20:35.221401"
---

Qwen2.5 VL 72B Instruct API | JieKou.AI
===============

[接口AI 上线 gemini-3.1-pro-preview！100 万 token 超长上下文的多模态强推理模型！](https://jiekou.ai/models/model-detail/gemini-3.1-pro-preview)

[![Image 1: JieKou.AI logo](https://jiekou.ai/logo/jiekou-logo.svg)接口AI](https://jiekou.ai/)

Playground

[Cloud Code](https://cc.jiekou.ai/)

[🔥 资源包](https://jiekou.ai/resource-pack)[价格](https://jiekou.ai/pricing)[文档](https://docs.jiekou.ai/docs/support/quickstart)

登录 开始使用

[首页](https://jiekou.ai/)/Qwen2.5 VL 72B Instruct

![Image 2: qwen/qwen2.5-vl-72b-instruct](https://jiekou.ai/_next/image?url=%2Fmodels%2Flogo%2Fqwen-logo.png&w=96&q=75)

Qwen2.5 VL 72B Instruct
=======================

qwen/qwen2.5-vl-72b-instruct

试用模型 API 文档

Qwen2.5-VL, the latest vision-language model in the Qwen2.5 series, delivers enhanced multimodal capabilities including advanced visual comprehension for object/text recognition, chart/layout analysis, and agent-based dynamic tool orchestration. It processes long-form videos (>1 hour) with key event detection while enabling precise spatial annotation through bounding boxes or coordinate points. The model specializes in structured data extraction from scanned documents (invoices, tables, etc.) and achieves state-of-the-art performance across multimodal benchmarks encompassing image understanding, temporal video analysis, and agent task evaluations.

价格

立即体验

输入$0.8/百万 tokens
输出$0.8/百万 tokens

API使用

使用以下代码示例来集成我们的API：

Python TypeScript Java Go Shell

聊天 补全

```python
1from openai import OpenAI
2
3client = OpenAI(
4    api_key="<Your API Key>",
5    base_url="https://api.jiekou.ai/openai"
6)
7
8response = client.chat.completions.create(
9    model="qwen/qwen2.5-vl-72b-instruct",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=32768,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```

### 信息

提供商

Qwen

量化

bf16

### 支持的功能

上下文长度

32768

最大输出

32768

serverless

支持

Input Capabilities

text, image, video

Output Capabilities

text

[![Image 3: JieKou.AI logo](https://jiekou.ai/logo/jiekou-logo.svg)接口AI](https://jiekou.ai/)
极简接入，极致性价比

需要更多信息吗?

技术支持：support@jiekou.AI

![Image 4: 联系方式](https://jiekou.ai/_next/image?url=%2Ffooter%2Fcontact-logo.png&w=48&q=75)

![Image 5: 联系方式二维码](https://wild-sunset-4e17.super-8d8.workers.dev/assets/GvxnaY4YtYxAjr7CrW293MqZISuknDlc.jpg)

法律声明

[服务条款](https://jiekou.ai/legal/terms-of-service)

文档与帮助

[文档](https://docs.jiekou.ai/docs/support/quickstart)[常见问题](https://docs.jiekou.ai/docs/support/faq_billing)

Copyright © 2026 jiekouai. All Rights Reserved

联系我们
