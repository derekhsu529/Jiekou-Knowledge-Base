---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/zai-org-glm-4.5"
crawled_at: "2026-02-26T23:16:21.780752"
---

GLM-4.5 Series Models are foundation models specifically engineered for intelligent agents. The flagship GLM-4.5 integrates 355 billion total parameters (32 billion active), unifying reasoning, coding, and agent capabilities to address complex application demands. As a hybrid reasoning system, it offers dual operational modes: - Thinking Mode: Enables complex reasoning, tool invocation, and strategic planning - Non-Thinking Mode: Delivers low-latency responses for real-time interactions This architecture bridges high-performance AI with adaptive functionality for dynamic agent environments.

价格

输入$0.6/百万 tokens
输出$2.2/百万 tokens

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
9    model="zai-org/glm-4.5",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=98304,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
