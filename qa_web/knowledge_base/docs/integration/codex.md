---
title: "OpenAI Codex CLI"
url: "https://docs.jiekou.ai/docs/integration/codex.md"
crawled_at: "2026-02-26T23:31:11.700926"
---

Published Time: Thu, 26 Feb 2026 15:31:11 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Codex CLI

## Codex CLI

Codex CLI 是 OpenAI 推出的一款编程终端智能体，它可以在您的计算机上本地运行。

1. 安装

在终端执行以下命令安装 Codex CLI

```bash  theme={null}
npm install -g @openai/codex

```

MacOS 用户可以使用 Homebrew

```bash  theme={null}
brew install codex
```

2. 配置使用本平台模型（MacOS/Linux）

打开 `~/.codex/config.toml`，做如下配置

```
model = "gpt-5"
model_provider = "jiekou"

[model_providers.jiekou]
name = "JIEKOU using Chat Completions"
base_url = "https://api.jiekou.ai/openai/v1"
env_key = "OPENAI_API_KEY"
wire_api = "chat"
query_params = {}
```

更细节配置方式可以查阅 [官方文档](https://github.com/openai/codex/blob/main/docs/config.md)。

3. 运行 Codex CLI

配置本站 ApiKey 为环境变量并运行 codex

```bash  theme={null}
OPENAI_API_KEY= codex ``` ## Codex VSCode extension 您也可以在 VSCode 中使用 Codex，先按照上一节指引配置好 `~/.codex/config.toml`，接着执行如下命令 ```bash theme={null} { cat << 'EOF' | tee $HOME/.codex/pcodex.sh #!/bin/bash OPENAI_API_KEY=sk_xxx /opt/homebrew/bin/codex "$@" EOF chmod +x $HOME/.codex/pcodex.sh } ``` 再在 VSCode settings.json 中添加如下配置 ```json theme={null} { "chatgpt.cliExecutable": "/home/path/.codex/pcodex.sh" } ``` 注意请将 `/home/path` 替换为实际 Home 目录路径
