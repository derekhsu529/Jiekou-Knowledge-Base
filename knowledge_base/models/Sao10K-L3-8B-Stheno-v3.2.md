---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/Sao10K-L3-8B-Stheno-v3.2"
crawled_at: "2026-02-26T23:21:40.348196"
---

Sao10K/L3-8B-Stheno-v3.2 is a highly skilled actor that excels at fully immersing itself in any role assigned.

价格

输入$0.05/百万 tokens
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
9    model="Sao10K/L3-8B-Stheno-v3.2",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=32000,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
