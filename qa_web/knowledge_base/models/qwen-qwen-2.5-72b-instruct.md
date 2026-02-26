---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/qwen-qwen-2.5-72b-instruct"
crawled_at: "2026-02-26T23:17:58.619325"
---

Qwen2.5 is the latest series of Qwen large language models. For Qwen2.5, we release a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters.

价格

输入$0.38/百万 tokens
输出$0.4/百万 tokens

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
9    model="qwen/qwen-2.5-72b-instruct",
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
