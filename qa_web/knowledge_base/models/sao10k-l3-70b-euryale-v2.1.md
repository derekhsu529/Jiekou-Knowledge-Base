---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/sao10k-l3-70b-euryale-v2.1"
crawled_at: "2026-02-26T23:20:40.852316"
---

The uncensored llama3 model is a powerhouse of creativity, excelling in both roleplay and story writing. It offers a liberating experience during roleplays, free from any restrictions. This model stands out for its immense creativity, boasting a vast array of unique ideas and plots, truly a treasure trove for those seeking originality. Its unrestricted nature during roleplays allows for the full breadth of imagination to unfold, akin to an enhanced, big-brained version of Stheno. Perfect for creative minds seeking a boundless platform for their imaginative expressions, the uncensored llama3 model is an ideal choice

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
9    model="sao10k/l3-70b-euryale-v2.1",
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
