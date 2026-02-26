---
title: "创建聊天对话请求"
url: "https://docs.jiekou.ai/docs/models/reference-llm-create-chat-completion.md"
crawled_at: "2026-02-26T23:33:25.939668"
---

Published Time: Thu, 26 Feb 2026 11:11:03 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 创建聊天对话请求

根据指定的聊天对话生成模型回复

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 要使用的模型名称。 

 组成当前对话的消息列表。   消息的内容。所有消息都需要 content，对于包含函数调用的 assistant 消息，content 可以为 null。 您可以根据不同的模态使用以下参数。  

   
选项 1：

 
您可以使用字符串类型来表示消息的文本内容。

 

 
选项 2：

 
使用内容部分的数组，object\[]。详细字段如下：

  内容部分的类型，在此情况下为 `text`。   文本内容。    
仅可使用视觉语言模型。

 
内容部分的数组，object\[]。详细字段如下：

  内容部分的类型，在此情况下为 `image_url`。     图像的 URL 或 base64 编码的图像数据（claude 系列模型仅支持 base64 编码的图像数据）。      
仅可使用支持视频的模型。

 
内容部分的数组，object\[]。详细字段如下：

  内容部分的类型，在此情况下为 `video_url`。     视频的 URL。      

    消息作者的角色。可以是 system、user 或 assistant。 枚举值: `system`, `user`, `assistant`   此消息作者的名称。可以包含 a-z、A-Z、0-9 和下划线，最大长度为 64 个字符。  

 在完成中生成的最大 tokens 数量。 如果您的提示（先前的消息）加上 max\_tokens 的 tokens 数超过模型的上下文长度，则行为取决于 context\_length\_exceeded\_behavior。默认情况下，max\_tokens 将被降低以适应上下文窗口，而不是返回错误。 

 是否流式返回部分进度。如果设置，tokens 将作为数据专用的服务器发送事件 (SSE) 发送，当它们可用时，流将以 `data: [DONE]` 消息终止。 

 流响应的选项。仅在设置 stream 为 true 时设置此项。   如果设置，将在数据: \[DONE] 消息之前流式传输一个额外的 chunk。此 chunk 中的 usage 字段显示整个请求的 tokens 使用统计信息，而 choices 字段始终为空数组。所有其他 chunk 也将包含一个 usage 字段，但值为 null。  

 为每个提示生成的完成数量。 注意：由于此参数会生成许多完成，因此可能会快速消耗您的 tokens 配额。请谨慎使用，并确保您对 max\_tokens 和 stop 有合理的设置。 必需范围：`1 < x < 128` 

 如果指定，我们的系统将尽力以确定性的方式进行采样，以便使用相同的 seed 和参数重复请求应返回相同的结果。 

 正值会根据新 tokens 在文本中现有的频率进行惩罚，降低模型逐字重复相同行的可能性。 如果目标只是稍微减少重复样本，合理的值在 0.1 到 1 之间。如果目标是强烈抑制重复，则可以将系数增加到 2，但这可能会显著降低样本质量。负值可用于增加重复的可能性。 另请参见 presence\_penalty，用于以固定速率惩罚至少出现一次的 tokens。 必需范围：`-2 < x < 2` 

 正值会根据新 tokens 是否出现在文本中进行惩罚，增加模型谈论新主题的可能性。 如果目标只是稍微减少重复样本，合理的值在 0.1 到 1 之间。如果目标是强烈抑制重复，则可以将系数增加到 2，但这可能会显著降低样本质量。负值可用于增加重复的可能性。 另请参见 `frequency_penalty`，用于根据 tokens 出现的频率以递增速率惩罚 tokens。 必需范围：`-2 < x < 2` 

 对重复的 tokens 应用惩罚以阻止或鼓励重复。值为 1.0 表示没有惩罚，允许自由重复。值高于 1.0 会惩罚重复，降低重复 tokens 的可能性。值在 0.0 和 1.0 之间会奖励重复，增加重复 tokens 的机会。为了获得良好的平衡，通常建议使用 1.2 的值。请注意，惩罚适用于生成的输出和仅解码器模型中的提示。 必需范围：`0 < x < 2` 

 API 将停止生成进一步 tokens 的最多 4 个序列。返回的文本将包含停止序列。 

 使用的采样温度，介于 0 和 2 之间。较高的值如 0.8 会使输出更随机，而较低的值如 0.2 会使其更集中和确定性。 我们通常建议更改此项或 `top_p`，但不要同时更改。 必需范围：`0 < x < 2` 

 一种替代采样温度的方法，称为核采样，其中模型考虑具有 top\_p 概率质量的 tokens 结果。因此，0.1 表示仅考虑构成前 10% 概率质量的 tokens。我们通常建议更改此项或温度，但不要同时更改。 必需范围：`0 < x <= 1` 

 Top-k 采样是另一种采样方法，其中最可能的 k 个下一个 tokens 被过滤，并且概率质量仅在这 k 个下一个 tokens 之间重新分配。k 的值控制文本生成期间每个步骤下一个 tokens 的候选数量。 必需范围：`1 < x < 128` 

 表示 tokens 被考虑的最小概率，相对于最可能 tokens 的概率。 必需范围：`0 <= x <= 1` 

 修改指定 tokens 在完成中出现的可能性。 接受一个 JSON 对象，将 tokens 映射到 -100 到 100 之间的关联偏差值。 数学上，偏差被添加到模型在采样之前生成的 logits 中。确切的效果会因模型而异。 例如，通过设置 `"logit_bias":{"1024": 6}` 将增加 token ID 为 1024 的 tokens 的可能性。 

 是否返回输出 tokens 的对数概率。如果为 true，则返回消息内容中每个输出 tokens 的对数概率。 

 一个介于 0 和 20 之间的整数，指定在每个 tokens 位置返回的最可能 tokens 的数量，每个 tokens 都有一个关联的对数概率。如果使用此参数，则必须将 `logprobs` 设置为 true。 必需范围：`0 <= x <= 20` 

 模型可以调用的工具列表。目前，仅支持函数作为工具。使用此项提供模型可以为其生成 JSON 输入的函数列表。 在[函数调用指南](/docs/model/llm-function-calling)中了解有关函数调用的更多信息。   工具的类型。 支持的类型：`function`     要调用的函数名称。必须是 a-z、A-Z、0-9，或包含下划线和破折号，最大长度为 64。   函数的描述，模型用于选择何时以及如何调用函数。   函数接受的参数，描述为 JSON Schema 对象。有关格式的文档，请参阅 [JSON Schema 参考](https://json-schema.org/understanding-json-schema/)。   在生成函数调用时是否启用严格的模式遵循。如果设置为 true，模型将遵循参数字段中定义的确切模式。    

 允许强制模型生成特定的输出格式。 设置为 `{ "type": "json_schema", "json_schema": {...} }` 启用结构化输出，确保模型将匹配您提供的 JSON schema。 设置为 `{ "type": "json_object" }` 启用旧的 JSON 模式，确保模型生成的消息是有效的 JSON。对于支持它的模型，建议使用 `json_schema`。   枚举值: `text`, `json_object`, `json_schema`   JSON Schema 响应格式。用于生成结构化 JSON 响应。 仅当 `type` 设置为 `json_schema` 时支持，并且当 `type` 设置为 `json_schema` 时也是必需的。 请在[结构化输出指南](/docs/model/llm-structured-outputs)中了解更多信息。   响应格式的名称。必须是 a-z、A-Z、0-9，或包含下划线和破折号，最大长度为 64。   响应格式的描述，模型用于确定如何以该格式响应。   响应格式的模式，描述为 JSON Schema 对象。了解如何在[此处](https://json-schema.org/specification)构建 JSON schema。 支持的类型：`string`, `number`, `integer`, `boolean`, `array`, `object`, `enum`, `anyOf`。   在生成输出时是否启用严格的模式遵循。如果设置为 true，模型将始终遵循 schema 字段中定义的确切模式。当 strict 为 true 时，仅支持 JSON Schema 的子集。 如果您通过提供 `strict: true` 启用结构化输出并使用不支持的 JSON Schema 调用 API，您将收到错误。    

 是否将推理与 "content" 分开到 "reasoning\_content" 字段中。 支持的模型： * `deepseek/deepseek-r1-turbo` 

 控制在思考和非思考模式之间的切换。 支持的模型： * `zai-org/glm-4.5` 

## 响应

 聊天完成选项的列表。   模型停止生成 tokens 的原因。如果模型达到自然停止点或提供的停止序列，则为 "stop"；如果达到请求中指定的最大 tokens 数量，则为 "length"。 可用选项: `stop`, `length`   聊天完成选项的索引。     此消息作者的角色。 可用选项: `system`, `user`, `assistant`   消息的内容。   推理步骤的内容。  仅当 `separate_reasoning` 设置为 true 时，此字段才可用。     

 响应生成时的 Unix 时间（以秒为单位）。 

 响应的唯一标识符。 

 用于聊天完成的模型。 

 对象类型，始终为 `chat.completion`。 

 使用统计信息。 对于流式响应，使用字段包含在返回的最后一个响应块中。   生成的完成中的 tokens 数量。   提示中的 tokens 数量。   请求中使用的 tokens 总数（提示 + 完成）。
