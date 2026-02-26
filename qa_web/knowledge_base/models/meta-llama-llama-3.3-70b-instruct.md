---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/meta-llama-llama-3.3-70b-instruct"
crawled_at: "2026-02-26T23:17:57.699138"
---

The Meta Llama 3.3 multilingual large language model (LLM) is a pretrained and instruction tuned generative model in 70B (text in/text out). The Llama 3.3 instruction tuned text only model is optimized for multilingual dialogue use cases and outperforms many of the available open source and closed chat models on common industry benchmarks. Supported languages: English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai.

价格

输入$0.13/百万 tokens
输出$0.39/百万 tokens

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
9    model="meta-llama/llama-3.3-70b-instruct",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=120000,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
