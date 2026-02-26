---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/gryphe-mythomax-l2-13b"
crawled_at: "2026-02-26T23:21:45.774009"
---

The idea behind this merge is that each layer is composed of several tensors, which are in turn responsible for specific functions. Using MythoLogic-L2's robust understanding as its input and Huginn's extensive writing capability as its output seems to have resulted in a model that exceeds at both, confirming my theory. (More details to be released at a later time).

价格

输入$0.09/百万 tokens
输出$0.09/百万 tokens

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
9    model="gryphe/mythomax-l2-13b",
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
