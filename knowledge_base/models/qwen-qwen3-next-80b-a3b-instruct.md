---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/qwen-qwen3-next-80b-a3b-instruct"
crawled_at: "2026-02-26T23:16:05.729417"
---

Qwen3-Next uses a highly sparse MoE design: 80B total parameters, but only ~3B activated per inference step. Experiments show that, with global load balancing, increasing total expert parameters while keeping activated experts fixed steadily reduces training loss.Compared to Qwen3’s MoE (128 total experts, 8 routed), Qwen3-Next expands to 512 total experts, combining 10 routed experts + 1 shared expert — maximizing resource usage without hurting performance. The Qwen3-Next-80B-A3B-Instruct performs comparably to our flagship model Qwen3-235B-A22B-Instruct-2507, and shows clear advantages in tasks requiring ultra-long context (up to 256K tokens).

价格

输入$0.15/百万 tokens
输出$1.5/百万 tokens

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
9    model="qwen/qwen3-next-80b-a3b-instruct",
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
