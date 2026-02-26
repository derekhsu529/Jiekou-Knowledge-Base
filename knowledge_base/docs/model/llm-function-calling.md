---
title: "工具调用（Function Calling）"
url: "https://docs.jiekou.ai/docs/model/llm-function-calling.md"
crawled_at: "2026-02-26T23:31:25.883804"
---

Published Time: Thu, 26 Feb 2026 15:31:25 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 工具调用（Function Calling）

export const FunctionCallingModels = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    let attempts = 0;
    const maxAttempts = 50;
    const INIT_DISPLAY_COUNT = 3;
    const interval = setInterval(() => {
      const clientComponent = document.getElementById("function-calling-models");
      if (clientComponent && window.jiekouRemoteData.llmModels.status === 'loaded') {
        const modelList = window.jiekouRemoteData.llmModels.data.filter(model => {
          return (model.features || []).includes('function-calling');
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
        document.getElementById('show-more-function-call-btn')?.addEventListener('click', () => {
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

## 使用场景

Function Calling 功能让模型可以与外部工具进行交互，获取实时信息或执行特定操作。这一功能提升了数据准确性，同时扩展了模型能力，使得模型不仅是简单的文本生成，而是可以支持更具动态性和实用性的应用场景。

Function Calling 的使用场景示例如下：

* **动态信息查询**：通过调用 API 从外部系统实时获取天气、新闻资讯、股票行情等动态数据。例如，调用天气 API 获取实时天气信息，当用户询问当前天气时，模型可以告诉用户此时此刻的天气状况，而不是提供过时的天气预报。
* **任务操作自动化**：通过函数调用执行特定操作，用户可以通过对话触发后台进行自动化操作。例如，调用订票网站 API 预定门票，当用户咨询如何购买某一景点的门票时，模型不再只是告诉用户如何订票，而是可以帮助用户直接完成订票操作。

## 支持的模型

以下模型支持 Function Calling：

 ## 使用方法 1. 定义模型要调用的工具函数。 2. 在请求中添加`tools` 参数定义模型要使用的函数。 ## 使用示例 下文提供了完整的 Python 代码示例，以查询某一地点的当前天气为例，演示如何使用 Function Calling。 对于 Function Calling 的具体 API 格式，请参考[创建聊天对话请求 API ](/docs/models/reference-llm-create-chat-completion)。 ### 1. 初始化客户端 您需要使用您的 JieKou AI API 密钥初始化客户端。 ```python theme={null} from openai import OpenAI import json client = OpenAI( base_url="https://api.jiekou.ai/openai", api_key="", ) model = "deepseek/deepseek-v3" ``` ### 2. 定义要调用的函数 定义模型要调用的函数。以下 Python 示例演示了获取天气信息的功能。 ```python theme={null} # 示例函数，用于模拟获取天气数据。 def get_weather(location): """获取指定地点的当前天气""" print("调用 get_weather 函数，位置: ", location) # 在实际应用中，您需要在这里调用外部天气 API。 # 这是一个简化示例，返回硬编码数据。 return json.dumps({"位置": location, "温度": "20 摄氏度"}) ``` ### 3. 构造包含工具和用户消息的 API 请求 创建 API 调用请求。此请求包括 `tools` 参数，定义模型要使用的函数，以及用户的消息。 ```python theme={null} tools = [ { "type": "function", "function": { "name": "get_weather", "description": "获取一个地点的天气，用户需要首先提供地点", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "城市信息, 例如：上海", } }, "required": ["location"] }, } }, ] messages = [ { "role": "user", "content": "上海的天气怎么样？" } ] # 发送请求并打印响应 response = client.chat.completions.create( model=model, messages=messages, tools=tools, ) # 请在生产环境中检查响应是否包含工具调用 tool_call = response.choices[0].message.tool_calls[0] print(tool_call.model_dump()) ``` **输出**： ```js theme={null} {'id': '0', 'function': {'arguments': '{"location": "上海"}', 'name': 'get_weather'}, 'type': 'function'} ``` ### 4. 根据函数调用结果进行响应并获取最终答案 接下来处理函数调用，执行 `get_weather` 函数，并将结果发送回模型以生成最终响应给用户。 ```python theme={null} # 确保工具调用已从上一步定义 if tool_call: # 扩展对话历史记录，添加助手工具调用消息 messages.append(response.choices[0].message) function_name = tool_call.function.name if function_name == "get_weather": function_args = json.loads(tool_call.function.arguments) # 执行函数并获取响应 function_response = get_weather( location=function_args.get("location")) # 将函数响应添加到消息中 messages.append( { "tool_call_id": tool_call.id, "role": "tool", "content": function_response, } ) # 从模型获取最终响应，包含函数结果 answer_response = client.chat.completions.create( model=model, messages=messages, # 注意：不要在此处包含 tools 参数 ) print(answer_response.choices[0].message) ``` **输出**： ``` ChatCompletionMessage(content="上海目前的温度是 20 摄氏度。请注意，天气情况可能会随时变化，建议您查看最新的天气预报以获取更准确的信息。", refusal=None, role='assistant', function_call=None, tool_calls=None) ``` ## 完整代码 ```python theme={null} from openai import OpenAI import json client = OpenAI( base_url="https://api.jiekou.ai/openai", api_key="", ) model = "deepseek/deepseek-v3" # 示例函数，用于模拟获取天气数据。 def get_weather(location): """获取指定地点的当前天气""" print("调用 get_weather 函数，位置: ", location) # 在实际应用中，您需要在这里调用外部天气 API。 # 这是一个简化示例，返回硬编码数据。 return json.dumps({"位置": location, "温度": "20 摄氏度"}) tools = [ { "type": "function", "function": { "name": "get_weather", "description": "获取一个地点的天气，用户需要首先提供地点", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "城市信息, 例如：上海", } }, "required": ["location"] }, } }, ] messages = [ { "role": "user", "content": "上海的天气怎么样？" } ] # 发送请求并打印响应 response = client.chat.completions.create( model=model, messages=messages, tools=tools, ) # 请在生产环境中检查响应是否包含工具调用 tool_call = response.choices[0].message.tool_calls[0] print(tool_call.model_dump()) # 确保工具调用已从上一步定义 if tool_call: # 扩展对话历史记录，添加助手工具调用消息 messages.append(response.choices[0].message) function_name = tool_call.function.name if function_name == "get_weather": function_args = json.loads(tool_call.function.arguments) # 执行函数并获取响应 function_response = get_weather( location=function_args.get("location")) # 将函数响应添加到消息中 messages.append( { "tool_call_id": tool_call.id, "role": "tool", "content": function_response, } ) # 从模型获取最终响应，包含函数结果 answer_response = client.chat.completions.create( model=model, messages=messages, # 注意：不要在此处包含 tools 参数 ) print(answer_response.choices[0].message) ```
