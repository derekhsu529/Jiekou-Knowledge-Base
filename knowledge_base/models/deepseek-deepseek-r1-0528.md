---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/deepseek-deepseek-r1-0528"
crawled_at: "2026-02-26T23:18:07.762015"
---

DeepSeek R1 0528 is the latest open-source model released by the DeepSeek team, featuring impressive reasoning capabilities, particularly achieving performance comparable to OpenAI's o1 model in mathematics, coding, and reasoning tasks.

价格

输入$0.7/百万 tokens
Cache read$0.35/百万 tokens
输出$2.5/百万 tokens

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
9    model="deepseek/deepseek-r1-0528",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=32768,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
