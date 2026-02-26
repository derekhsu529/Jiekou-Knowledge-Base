---
title: "Anthropic"
url: "https://docs.jiekou.ai/docs/providers/anthropic.md"
crawled_at: "2026-02-26T23:36:45.744376"
---

Published Time: Thu, 26 Feb 2026 15:36:45 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Anthropic

## 原生协议支持

本站所有 Anthropic 模型均可通过原生 `/v1/messages` 协议访问。比如激活 1M token 上下文，可使用如下请求

```bash  theme={null}
curl https://api.jiekou.ai/anthropic/v1/messages \
  -H "x-api-key: $API_KEY" \
  -H "anthropic-beta: context-1m-2025-08-07" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-20250514",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Process this large document..."}
    ]
  }'
```

## Prompt caching

本站支持通过 Anthropic 协议或 OpenAI 兼容协议使用 Prompt caching。
具体可参考文档 [模型特性 - Prompt caching](/docs/feature/prompt-caching)。

## Extend thinking

当前仅支持通过 Anthropic 协议控制思考过程。

```bash  theme={null}
curl https://api.jiekou.ai/anthropic/v1/messages \
     -H "x-api-key: $API_KEY" \
     -H "content-type: application/json" \
     -d \
'{
    "model": "claude-sonnet-4-20250514",
    "max_tokens": 16000,
    "thinking": {
        "type": "enabled",
        "budget_tokens": 10000
    },
    "messages": [
        {
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?"
        }
    ]
}'
```

## Tools

暂时只支持 Bash 和 Text editor。Computer use, Web fetch, Web search 等暂不支持。

使用方式参考[官网文档](https://docs.claude.com/en/docs/agents-and-tools/tool-use)即可。

## Claude Code 使用

参考 [第三方工具配置 - Claude Code](/docs/integration/claudecode)。
