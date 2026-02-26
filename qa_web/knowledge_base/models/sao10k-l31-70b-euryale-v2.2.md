---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/sao10k-l31-70b-euryale-v2.2"
crawled_at: "2026-02-26T23:25:10.666115"
---

Euryale L3.1 70B v2.2 is a model focused on creative roleplay from Sao10k. It is the successor of Euryale L3 70B v2.1.

价格

输入$1.48/百万 tokens
输出$1.48/百万 tokens

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
9    model="sao10k/l31-70b-euryale-v2.2",
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
