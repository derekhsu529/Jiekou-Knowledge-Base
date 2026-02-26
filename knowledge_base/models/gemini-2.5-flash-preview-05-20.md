---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/gemini-2.5-flash-preview-05-20"
crawled_at: "2026-02-26T23:23:44.148572"
---

gemini-2.5-flash-preview-05-20 API | JieKou.AI
===============

[接口AI 上线 gemini-3.1-pro-preview！100 万 token 超长上下文的多模态强推理模型！](https://jiekou.ai/models/model-detail/gemini-3.1-pro-preview)

[![Image 1: JieKou.AI logo](https://jiekou.ai/logo/jiekou-logo.svg)接口AI](https://jiekou.ai/)

Playground

[Cloud Code](https://cc.jiekou.ai/)

[🔥 资源包](https://jiekou.ai/resource-pack)[价格](https://jiekou.ai/pricing)[文档](https://docs.jiekou.ai/docs/support/quickstart)

登录 开始使用

[首页](https://jiekou.ai/)/gemini-2.5-flash-preview-05-20

![Image 2: gemini-2.5-flash-preview-05-20](https://jiekou.ai/_next/image?url=%2Fmodels%2Flogo%2Fgoogle-logo.png&w=96&q=75)

gemini-2.5-flash-preview-05-20
==============================

gemini-2.5-flash-preview-05-20

试用模型 API 文档

价格

立即体验

输入$0.135/百万 tokens$0.15/百万 tokens
输出$3.15/百万 tokens$3.5/百万 tokens

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
9    model="gemini-2.5-flash-preview-05-20",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=200000,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```

### 信息

提供商

Google

量化

-

### 支持的功能

上下文长度

1048576

最大输出

200000

函数调用

支持

结构化输出

支持

serverless

支持

Input Capabilities

text, image, video, audio

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
