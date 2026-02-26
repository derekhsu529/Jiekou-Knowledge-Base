---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/google-gemma-3-27b-it"
crawled_at: "2026-02-26T23:21:34.818427"
---

Gemma 3 introduces multimodality, supporting vision-language input and text outputs. It handles context windows up to 32k tokens, understands over 140 languages, and offers improved math, reasoning, and chat capabilities, including structured outputs. Gemma 3 27B is Google's latest open source model, successor to Gemma.

价格

输入$0.119/百万 tokens
输出$0.2/百万 tokens

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
9    model="google/gemma-3-27b-it",
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
