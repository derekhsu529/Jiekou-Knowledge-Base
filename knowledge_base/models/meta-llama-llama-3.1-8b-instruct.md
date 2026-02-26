---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/meta-llama-llama-3.1-8b-instruct"
crawled_at: "2026-02-26T23:17:45.889861"
---

Meta's latest class of models, Llama 3.1, launched with a variety of sizes and configurations. The 8B instruct-tuned version is particularly fast and efficient. It has demonstrated strong performance in human evaluations, outperforming several leading closed-source models.

价格

输入$0.02/百万 tokens
输出$0.05/百万 tokens

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
9    model="meta-llama/llama-3.1-8b-instruct",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=16384,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
