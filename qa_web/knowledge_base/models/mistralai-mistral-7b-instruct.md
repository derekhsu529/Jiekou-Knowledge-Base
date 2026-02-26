---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/mistralai-mistral-7b-instruct"
crawled_at: "2026-02-26T23:18:10.241814"
---

A high-performing, industry-standard 7.3B parameter model, with optimizations for speed and context length.

价格

输入$0.029/百万 tokens
输出$0.059/百万 tokens

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
9    model="mistralai/mistral-7b-instruct",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=8192,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
