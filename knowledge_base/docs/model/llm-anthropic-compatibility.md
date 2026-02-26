---
title: "兼容 Anthropic SDK"
url: "https://docs.jiekou.ai/docs/model/llm-anthropic-compatibility.md"
crawled_at: "2026-02-26T23:16:56.440118"
---

Published Time: Thu, 26 Feb 2026 15:16:56 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 兼容 Anthropic SDK

export const AnthropicCompatibilityModels = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    let attempts = 0;
    const maxAttempts = 50;
    const INIT_DISPLAY_COUNT = 3;
    const interval = setInterval(() => {
      const clientComponent = document.getElementById("anthropic-compatibility-models");
      if (clientComponent && window.jiekouRemoteData.llmModels.status === 'loaded') {
        const modelList = window.jiekouRemoteData.llmModels.data.filter(model => {
          return (model.endpoints || []).includes('anthropic');
        });
        let displayModels = modelList.slice(0, INIT_DISPLAY_COUNT).map(model => {
          return `*   ${model.id}
`;
        }).join('');
        let showMoreButton = '';
        if (modelList.length > INIT_DISPLAY_COUNT) {
          showMoreButton = `查看更多`;
        }
        clientComponent.innerHTML = `
          
${displayModels}

          ${showMoreButton}
        `;
        document.getElementById('show-more-anthropic-compatibility-model-btn')?.addEventListener('click', () => {
          clientComponent.innerHTML = `
            
${modelList.map(model => { return `*   ${model.id}
`; }).join('')}

          `;
        });
        clearInterval(interval);
      }
      attempts++;
      if (attempts >= maxAttempts) {
        clearInterval(interval);
      }
    }, 200);
    return ;
  }
};

JieKou AI 提供了与 Anthropic SDK 兼容的 API 服务，方便您集成到现有应用程序中。如果您已经使用 Anthropic SDK 开发了应用程序，只需要将 base URL 和 API Key 替换为 JieKou AI 的 API 地址和 API Key 即可。请参考下面的接入指南。

## 支持的模型

目前只有以下模型提供了 Anthropic SDK 兼容性支持：

 ## 快速开始 ### 1. 安装 Anthropic SDK  ```bash Python icon="python" theme={null} pip install anthropic ``` ```bash TypeScript icon="js" theme={null} npm install @anthropic-ai/sdk ```  ### 2. 初始化客户端 Anthropic SDK 会尝试从环境变量 `ANTHROPIC_API_KEY` 和 `ANTHROPIC_BASE_URL` 中分别获取 API Key 和 base URL。您也可以在初始化客户端的时候通过参数来指定。 * 基于环境变量设置  ```bash Bash icon="terminal" theme={null} export ANTHROPIC_BASE_URL="https://api.jiekou.ai/anthropic" export ANTHROPIC_API_KEY="" ```  * 通过在初始化 Anthropic 客户端时设置参数  ```python Python icon="python" theme={null} import anthropic client = anthropic.Anthropic( base_url="https://api.jiekou.ai/anthropic", api_key="", # 重写 header default_headers={ "Content-Type": "application/json", "Authorization": "Bearer ", } ) ``` ```typescript TypeScript icon="js" theme={null} import Anthropic from "@anthropic-ai/sdk"; const anthropic = new Anthropic({ baseURL: "https://api.jiekou.ai/anthropic", apiKey: "", // 重写 header defaultHeaders: { "Content-Type": "application/json", Authorization: `Bearer `, } }); ```  ### 3. 调用 API  ```python Python icon="python" theme={null} import anthropic # 初始化客户端，如果您已经通过环境变量 `ANTHROPIC_BASE_URL` 和 `ANTHROPIC_API_KEY` # 设置了 API Key 和 base URL，可以省略 `api_key` 和 `base_url` 参数。 client = anthropic.Anthropic( base_url="https://api.jiekou.ai/anthropic", api_key="", # 重写 header default_headers={ "Content-Type": "application/json", "Authorization": "Bearer ", } ) message = client.messages.create( model="moonshotai/kimi-k2-instruct", max_tokens=1000, temperature=1, system=[ { "type": "text", "text": "你是 JieKou AI AI 助手，你会以诚实专业的态度帮助用户，用中文回答问题。" } ], messages=[ { "role": "user", "content": [ { "type": "text", "text": "你是谁?" } ] } ] ) print(message.content) ``` ```typescript TypeScript icon="js" theme={null} import Anthropic from "@anthropic-ai/sdk"; // 初始化客户端，如果您已经通过环境变量 `ANTHROPIC_BASE_URL` 和 `ANTHROPIC_API_KEY` // 设置了 API Key 和 base URL，可以省略 `baseURL` 和 `apiKey` 参数。 const anthropic = new Anthropic({ baseURL: "https://api.jiekou.ai/anthropic", apiKey: "", // 重写 header defaultHeaders: { "Content-Type": "application/json", Authorization: `Bearer `, }, }); const msg = await anthropic.messages.create({ model: "moonshotai/kimi-k2-instruct", max_tokens: 1000, temperature: 1, system: "你是 JieKou AI AI 助手，你会以诚实专业的态度帮助用户，用中文回答问题。", messages: [ { role: "user", content: [ { type: "text", text: "你是谁?" } ] } ] }); console.log(msg); ```
