---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/qwen-qwen3-235b-a22b-fp8"
crawled_at: "2026-02-26T23:18:15.658638"
---

Achieves effective integration of inference and non-inference modes, enabling seamless switching between modes during conversations. The model's inference capability significantly surpasses that of QwQ, and its general capabilities exceed those of Qwen2.5-72B-Instruct, reaching the state-of-the-art (SOTA) level among models of the same scale.

价格

输入$0.2/百万 tokens
输出$0.8/百万 tokens

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
9    model="qwen/qwen3-235b-a22b-fp8",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=20000,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
