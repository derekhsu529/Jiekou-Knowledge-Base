---
title: "Prompt caching"
url: "https://docs.jiekou.ai/docs/feature/prompt-caching.md"
crawled_at: "2026-02-26T23:31:05.751440"
---

Published Time: Thu, 26 Feb 2026 15:31:05 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompt caching

## Anthropic

Anthropic 模型支持 **显式 Prompt caching**。

在本平台， 无论是 OpenAI chat/completions 协议，还是 Anthropic v1/messages 协议，均可使用 `"cache_control": {"type": "ephemeral"}` 指定需要缓存的内容。

```json  theme={null}
{
  "model": "claude-sonnet-4-5-20250929",
  "max_tokens": 4096,
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "HUGE TEXT BODY",
          "cache_control": { "type": "ephemeral" }
        },
        {
          "type": "text",
          "text": "Name all the characters in the above book"
        }
      ]
    }
  ]
}
```

⚠️ cache\_control 是我们扩展的字段，在 OpenAI 官方 SDK 协议中不包含此属性，因此在调用时需显式添加。

通过响应可验证缓存创建/命中情况

 ```json OpenAI /chat/completions theme={null} { "prompt_tokens": 7039, "completion_tokens": 650, "total_tokens": 7689, "prompt_tokens_details": { "cached_tokens": 7019, "cache_creation_input_tokens": 7019, # 👈 cache created "cache_read_input_tokens": 0 } } --- { "prompt_tokens": 7042, "completion_tokens": 572, "total_tokens": 7614, "prompt_tokens_details": { "audio_tokens": 0, "cached_tokens": 7019, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 7019 # 👈 cache read } } ``` ```json Anthropic /v1/messages theme={null} {"cache_creation_input_tokens":188086,"cache_read_input_tokens":0,"input_tokens":21,"output_tokens":393} # 👈 cache created {"cache_creation_input_tokens":0,"cache_read_input_tokens":188086,"input_tokens":21,"output_tokens":393} # 👈 cache read ``` 

⚠️⚠️⚠️ 对于 Anthropic 模型，使用 Prompt caching 最小 Input Tokens 要求如下

* Claude Opus 4.1、Claude Opus 4、Claude Sonnet 4.5、Claude Sonnet 4、Claude Sonnet 3.7 为 1024 tokens
* Claude Haiku 4.5、Claude Haiku 3.5 和 Claude Haiku 3 为 2048 tokens

## OpenAI 及 OpenAI 兼容模型

通常，这些模型可能支持隐式缓存。

当用户反复使用相同的 Prompt 前缀访问同一模型，有一定概率命中缓存。

```
// Round 1
{
  "model": "gpt-4",
  "messages": [
    {
      "role": "system",
      "content": "HUGE TEXT BODY: Complete API documentation, code style guide, best practices (5000+ lines)"
    },
    {
      "role": "user",
      "content": "How do I authenticate API requests?"
    }
  ]
}

// Round 2 - Documentation cached
{
  "model": "gpt-4",
  "messages": [
    {
      "role": "system",
      "content": "HUGE TEXT BODY: Complete API documentation, code style guide, best practices (5000+ lines)"
    },
    {
      "role": "user",
      "content": "How do I authenticate API requests?"
    },
    {
      "role": "assistant",
      "content": "Use Bearer token in Authorization header..."
    },
    {
      "role": "user",
      "content": "What about rate limiting?"
    }
  ]
}
```

以下为缓存命中的用量示例

```json  theme={null}
{
  "prompt_tokens": 3003,
  "completion_tokens": 1564,
  "total_tokens": 4567,
  "prompt_tokens_details": {
    "cached_tokens": 2025 # 👈 cache hitted
  }
}
```

## Gemini

目前仅支持隐式缓存。隐式缓存无需手动设置或额外的 cache\_control 配置。当用户反复使用相同的 Prompt 前缀访问同一模型，有一定概率命中缓存。

注意点如下

* 平均 TTL（缓存存活时间）为 3-5 分钟，但可能会有所变化（例如可能仅为几秒）
* Gemini 2.5 Flash 要求最小输入为 1024 tokens，Gemini 2.5 Pro 要求最小为 4096 tokens

以下为缓存命中的用量示例：

```
{
  "prompt_tokens": 2004,
  "completion_tokens": 1564,
  "total_tokens": 3568,
  "prompt_tokens_details": {
    "cached_tokens": 1994 # 👈 cache hitted
  }
}
```

输入示例参考 **OpenAI 模型及 OpenAI 兼容模型** 即可。
