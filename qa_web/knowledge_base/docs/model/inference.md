---
title: "推理模型"
url: "https://docs.jiekou.ai/docs/model/inference.md"
crawled_at: "2026-02-26T23:16:56.065440"
---

Published Time: Thu, 26 Feb 2026 15:16:55 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 推理模型

export const ReasoningModels = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    let attempts = 0;
    const maxAttempts = 50;
    const INIT_DISPLAY_COUNT = 3;
    const interval = setInterval(() => {
      const clientComponent = document.getElementById("reasoning-models");
      if (clientComponent && window.jiekouRemoteData.llmModels.status === 'loaded') {
        const modelList = window.jiekouRemoteData.llmModels.data.filter(model => {
          return (model.features || []).includes('reasoning');
        });
        let displayModels = modelList.slice(0, INIT_DISPLAY_COUNT).map(model => {
          return `*   ${model.id}
`;
        }).join('');
        let showMoreButton = '';
        if (modelList.length > INIT_DISPLAY_COUNT) {
          showMoreButton = `展示更多`;
        }
        clientComponent.innerHTML = `
          
${displayModels}

          ${showMoreButton}
        `;
        document.getElementById('show-more-reasoning-model-btn')?.addEventListener('click', () => {
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

## 功能介绍

推理模型是针对复杂问题解决和推理任务优化的高级语言模型，通过输出详细的推理步骤（思维链）提升问题求解的准确性。

### 典型应用场景

* **复杂问题解决**：适用于需要逐步推导、明确逻辑步骤的场景，例如数学、科学推理。
* **决策支持系统**：提供详细推理过程支持决策分析，帮助理解决策背后的逻辑。
* **教育和培训**：帮助用户学习和理解复杂知识，提供详细的推导过程。

## 安装与准备

在使用推理模型前，请确保已安装最新版本的 OpenAI SDK：

```bash  theme={null}
pip install -U openai
```

## API 调用方法

通过调用 `/chat/completions` 接口使用推理模型。

### 请求参数说明

* `max_tokens`：设置模型输出的最大 token 数。
* `temperature`：建议设置为 0.5 至 0.7（推荐 0.6）以平衡输出的创造性与逻辑性。
* `top_p`：建议设置为 0.95。

### 示例请求代码

#### 流式输出请求

```python  theme={null}
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY", base_url="https://api.jiekou.ai/openai")
messages = [
    {"role": "user", "content": "解释一下牛顿第二定律。"}
]

response = client.chat.completions.create(
    model="deepseek/deepseek-r1",
    messages=messages,
    stream=True,
    max_tokens=4096
)

content = ""
reasoning_content = ""
for chunk in response:
    if chunk.choices[0].delta.content:
        content += chunk.choices[0].delta.content
    if chunk.choices[0].delta.reasoning_content:
        reasoning_content += chunk.choices[0].delta.reasoning_content

print("最终回答：", content)
print("推理过程：", reasoning_content)
```

#### 非流式输出请求

```python  theme={null}
response = client.chat.completions.create(
    model="deepseek/deepseek-r1",
    messages=[
        {"role": "user", "content": "什么是温室效应？如何减缓？"}
    ],
    stream=False,
    max_tokens=4096
)

content = response.choices[0].message.content
reasoning_content = response.choices[0].message.reasoning_content

print("最终回答：", content)
print("推理过程：", reasoning_content)
```

## 上下文管理

模型返回的推理内容不会自动拼接到下一轮对话中，用户需手动管理对话历史：

```python  theme={null}
messages.append({"role": "assistant", "content": content})
messages.append({"role": "user", "content": "继续解释一下解决方案。"})
```

## 支持模型列表

 ## 计费方式 * 根据输入和输出的 token 数进行计费。 * 具体计费标准及转换规则，请在模型详情页查询。 ## 注意事项与最佳实践 * 不要在 `system` 消息中添加推理指令，应在 `user` 消息中直接明确指令。 * 在数学问题中明确指出要求，例如：“请逐步推理并明确最终答案。” * 为避免模型跳过推理环节，建议强制模型在输出前添加换行符。
