---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/deepseek-deepseek-v3-0324"
crawled_at: "2026-02-26T23:21:56.382012"
---

DeepSeek V3, a 685B-parameter, mixture-of-experts model, is the latest iteration of the flagship chat model family from the DeepSeek team.

价格

输入$0.28/百万 tokens
Cache write$0.14/百万 tokens
Cache read$0.14/百万 tokens
输出$1.14/百万 tokens

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
9    model="deepseek/deepseek-v3-0324",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=163840,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
