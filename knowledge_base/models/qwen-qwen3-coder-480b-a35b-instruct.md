---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/qwen-qwen3-coder-480b-a35b-instruct"
crawled_at: "2026-02-26T23:16:18.416298"
---

Qwen3-Coder-480B-A35B-Instruct is a cutting-edge open coding model from Qwen, matching Claude Sonnet’s performance in agentic programming, browser automation, and core development tasks. With native 256K context (extendable to 1M tokens via YaRN), it excels at repository-scale analysis and features specialized function-call support for platforms like Qwen Code and CLINE—making it ideal for complex, real-world development workflows.

价格

输入$0.29/百万 tokens
输出$1.2/百万 tokens

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
9    model="qwen/qwen3-coder-480b-a35b-instruct",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=65536,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
