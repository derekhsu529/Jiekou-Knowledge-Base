---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/moonshotai-kimi-k2-instruct"
crawled_at: "2026-02-26T23:21:50.919247"
---

Kimi K2 is a state-of-the-art mixture-of-experts (MoE) language model with 32 billion activated parameters and 1 trillion total parameters. Trained with the Muon optimizer, Kimi K2 achieves exceptional performance across frontier knowledge, reasoning, and coding tasks while being meticulously optimized for agentic capabilities.Specifically designed for tool use, reasoning, and autonomous problem-solving.

价格

输入$0.57/百万 tokens
输出$2.3/百万 tokens

使用以下代码示例来集成我们的API：

```
1from openai import OpenAI
2
3client = OpenAI(
4    api_key="<Your API Key>",
5    base_url="https://api.jiekou.ai/openai"
6)
7
8response = client.chat.completions.create(
9    model="moonshotai/kimi-k2-instruct",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=131072,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
