---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/qwen-qwen3-next-80b-a3b-thinking"
crawled_at: "2026-02-26T23:16:07.455455"
---

Qwen3 Next 80B A3B Thinking API | JieKou.AI
===============

[接口AI 上线 gemini-3.1-pro-preview！100 万 token 超长上下文的多模态强推理模型！](https://jiekou.ai/models/model-detail/gemini-3.1-pro-preview)

[![Image 1: JieKou.AI logo](https://jiekou.ai/logo/jiekou-logo.svg)接口AI](https://jiekou.ai/)

Playground

[Cloud Code](https://cc.jiekou.ai/)

[🔥 资源包](https://jiekou.ai/resource-pack)[价格](https://jiekou.ai/pricing)[文档](https://docs.jiekou.ai/docs/support/quickstart)

登录 开始使用

[首页](https://jiekou.ai/)/Qwen3 Next 80B A3B Thinking

![Image 2: qwen/qwen3-next-80b-a3b-thinking](https://jiekou.ai/_next/image?url=%2Fmodels%2Flogo%2Fqwen-logo.png&w=96&q=75)

Qwen3 Next 80B A3B Thinking
===========================

qwen/qwen3-next-80b-a3b-thinking

试用模型 API 文档

Qwen3-Next uses a highly sparse MoE design: 80B total parameters, but only ~3B activated per inference step. Experiments show that, with global load balancing, increasing total expert parameters while keeping activated experts fixed steadily reduces training loss.Compared to Qwen3’s MoE (128 total experts, 8 routed), Qwen3-Next expands to 512 total experts, combining 10 routed experts + 1 shared expert — maximizing resource usage without hurting performance. The Qwen3-Next-80B-A3B-Thinking excels at complex reasoning tasks — outperforming higher-cost models like Qwen3-30B-A3B-Thinking-2507 and Qwen3-32B-Thinking, outpeforming the closed-source Gemini-2.5-Flash-Thinking on multiple benchmarks, and approaching the performance of our top-tier model Qwen3-235B-A22B-Thinking-2507.

价格

立即体验

输入$0.15/百万 tokens
输出$1.5/百万 tokens

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
9    model="qwen/qwen3-next-80b-a3b-thinking",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=65536,
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

65536

最大输出

65536

函数调用

支持

结构化输出

支持

推理

支持

serverless

支持

Input Capabilities

text

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
