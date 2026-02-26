---
title: "Claude Code"
url: "https://docs.jiekou.ai/docs/integration/claudecode.md"
crawled_at: "2026-02-26T23:31:09.904182"
---

Published Time: Thu, 26 Feb 2026 15:31:09 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Code

Claude Code 是 Anthropic 推出的，一款运行于您终端的智能体（Agentic）编程工具，它能够理解您的代码库，并通过执行常规任务来帮助您更快地编程。

本站提供了 Anthropic SDK 兼容的 LLM API 服务，您可以轻松地在 Claude Code 中使用多种大语言模型来完成任务。请参考下面指南完成接入过程。

1. 安装 Claude Code

在终端执行以下命令安装 Claude Code

⚠️ 在安装 Claude Code 前，请确保您的本地环境已安装 Node.js 18 或更高版本

```bash  theme={null}
npm install -g @anthropic-ai/claude-code
```

2. 开启一个终端会话

```bash  theme={null}
{
  export ANTHROPIC_BASE_URL="https://api.jiekou.ai/anthropic"
  export ANTHROPIC_AUTH_TOKEN="" # 设置本平台支持的模型 export ANTHROPIC_MODEL="claude-opus-4-1-20250805" export ANTHROPIC_SMALL_FAST_MODEL="claude-sonnet-4-20250514" } ``` 接下来进入项目文件目录，启动 Claude Code 即可 ```bash theme={null} cd  claude . ```
