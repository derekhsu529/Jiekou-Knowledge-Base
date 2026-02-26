---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/deepseek-deepseek-v3.1"
crawled_at: "2026-02-26T23:16:14.986324"
---

DeepSeek-V3.1 is a hybrid model that supports both thinking mode and non-thinking mode.DeepSeek-V3.1 is post-trained on the top of DeepSeek-V3.1-Base, which is built upon the original V3 base checkpoint through a two-phase long context extension approach, following the methodology outlined in the original DeepSeek-V3 report. We have expanded our dataset by collecting additional long documents and substantially extending both training phases. The 32K extension phase has been increased 10-fold to 630B tokens, while the 128K extension phase has been extended by 3.3x to 209B tokens.

价格

输入$0.27/百万 tokens
输出$1/百万 tokens

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
9    model="deepseek/deepseek-v3.1",
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
