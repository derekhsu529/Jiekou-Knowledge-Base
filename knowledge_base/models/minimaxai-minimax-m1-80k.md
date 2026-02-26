---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/minimaxai-minimax-m1-80k"
crawled_at: "2026-02-26T23:18:04.825410"
---

MiniMax-M1: The World's First Open-Weight, Large-Scale Hybrid Attention Inference Model MiniMax-M1 adopts a Mixture of Experts (MoE) architecture and integrates the Flash Attention mechanism. The model contains a total of 456 billion parameters, with 45.9 billion parameters activated per token. Natively, the M1 model supports a context length of 1 million tokens—8 times that of DeepSeek R1. Additionally, by combining the CISPO algorithm with an efficient hybrid attention design for reinforcement learning training, MiniMax-M1 achieves industry-leading performance in long-context reasoning and real-world software engineering scenarios.

价格

输入$0.55/百万 tokens
输出$2.2/百万 tokens

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
9    model="minimaxai/minimax-m1-80k",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=40000,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
