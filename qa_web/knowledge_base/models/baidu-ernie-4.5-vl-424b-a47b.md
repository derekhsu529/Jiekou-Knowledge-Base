---
title: "Untitled"
url: "https://jiekou.ai/models/model-detail/baidu-ernie-4.5-vl-424b-a47b"
crawled_at: "2026-02-26T23:21:12.086044"
---

The ERNIE 4.5 series of open-source models adopts a Mixture-of-Experts (MoE) architecture, representing an innovative multimodal heterogeneous model structure. It achieves cross-modal knowledge fusion through a parameter-sharing mechanism while retaining dedicated parameter spaces for individual modalities. This architecture is particularly well-suited for the continuous pre-training paradigm from large language models to multimodal models, significantly enhancing multimodal understanding capabilities while maintaining or even improving performance in text-based tasks. The models are efficiently trained, inferred, and deployed using the PaddlePaddle deep learning framework. During the pre-training of large language models, the Model FLOPs Utilization (MFU) reaches 47%. Experimental results demonstrate that this series of models achieves state-of-the-art (SOTA) performance across multiple text and multimodal benchmarks, with particularly outstanding results in instruction following, world knowledge memorizatio

价格

输入$0.42/百万 tokens
输出$1.25/百万 tokens

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
9    model="baidu/ernie-4.5-vl-424b-a47b",
10    messages=[
11        {"role": "system", "content": "You are a helpful assistant."},
12        {"role": "user", "content": "Hello, how are you?"}
13    ],
14    max_tokens=16000,
15    temperature=0.7
16)
17
18print(response.choices[0].message.content)
```
