---
title: "创建对话请求"
url: "https://docs.jiekou.ai/docs/models/reference-llm-create-completion.md"
crawled_at: "2026-02-26T23:33:28.190822"
---

Published Time: Thu, 26 Feb 2026 15:33:28 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 创建对话请求

根据指定的 prompt 与参数生成模型回复

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 对应的模型名称。可用模型名称请参考：[JieKou AI](https://jiekou.ai/#model-library) 中的模型库。 

 用于生成对话的提示（提示可以是字符串、字符串数组、tokens 数组或 tokens 数组的数组）。 

 在生成对话时可产生的最大 tokens 数。

prompt 的 tokens 数量加上 max\_tokens 不能超过模型的上下文长度。 

 是否使用流式传输。默认为 false，如果设置了，tokens 将以 data-only server-sent events（SSE）发送，并以 data: \[DONE] 消息终止流。 

 流式回复选项。仅当 stream 设置为 true 时设置。   如果设置，将在数据: \[DONE] 消息之前流式传输一个额外的 chunk。此 chunk 中的 usage 字段显示整个请求的 tokens 使用统计信息，而 choices 字段始终为空数组。所有其他 chunk 也将包含一个 usage 字段，但值为 null。  

 每个提示生成多少个对话。默认值为 1。

注意：由于此参数会生成多个对话，因此可能会快速消耗您的 tokens 计费额度。请谨慎使用，并确保为 max\_tokens 和 stop 设置了合理的值。

所需范围：1 \< x \< 128 

 如果指定，我们的系统将尽最大努力进行确定性采样，以便相同的 seed 和参数的重复请求应返回相同的结果。 

 默认值为 0，正值会根据新 tokens 在当前文本中的出现频率对其进行惩罚，从而降低模型重复相同内容的可能性。

如果目的是仅仅减少重复样本，合理的值大约在 0.1 到 1 之间。如果目的是强烈抑制重复，可以将系数提高到 2，但这可能会明显降低样本质量。负值可以用来增加重复的可能性。

另见 presence\_penalty，用于以固定速率惩罚至少出现一次的 tokens

所需范围：-2 \< x \< 2 

 默认值为 0，正值会根据新 tokens 是否出现在当前文本中对其进行惩罚，从而增加模型谈论新话题的可能性。

如果目的是稍微减少重复样本，合理的值大约在 0.1 到 1 之间。如果目的是强烈抑制重复，可以将系数提高到 2，但这可能会显著降低样本质量。负值可以用来增加重复的可能性。

另见 frequency\_penalty，用于根据 tokens 出现的频率按递增速率进行惩罚

所需范围：-2 \< x \< 2 

 对重复的 tokens 应用惩罚，以抑制或鼓励重复。值为 1.0 表示没有惩罚，允许自由重复。大于 1.0 的值会惩罚重复，降低重复 tokens 的可能性。介于 0.0 和 1.0 之间的值会奖励重复，增加重复 tokens 的机会。为了达到良好的平衡，通常建议使用 1.2。请注意，在仅解码器模型中，惩罚会同时应用于生成的输出和提示。

所需范围：0 \< x \< 2 

 最多 4 个序列，API 将停止生成更多 tokens。返回的文本包含停止序列。 

 对话中的随机性程度，默认值为 1，介于 0 和 2 之间。较高的值（如 0.8）会使输出更加随机，而较低的值（如 0.2），会使输出更集中且确定性更强。

我们通常建议只调整此项或 top\_p，而不是同时调整两者。

所需范围：0 \< x \< 2 

 作为 temperature 的替代方法，称为 nucleus sampling，模型会考虑具有 top\_p 概率质量的 tokens 的结果。因此，0.1 意味着只考虑构成前 10% 概率质量的 tokens。我们通常建议只调整此项或 temperature，而不是同时调整两者。

所需范围：0 \< x ≤ 1 

 Top-k 采样是另一种采样方法，在这种方法中，k 个最可能的下一个 tokens 会被筛选出来，并且概率质量仅在这 k 个 tokens 之间重新分配。k 的值控制了在每一步生成文本时，下一个 tokens 的候选数量。

所需范围：1 \< x \< 128 

 表示一个 tokens 被考虑的最小概率的浮动值，相对于最有可能的 tokens 的概率。

所需范围：0 ≤ x ≤ 1 

 默认为 null。修改指定 tokens 在对话中出现的可能性。接受一个 JSON 对象，将 tokens 映射到一个从 -100 到 100 的关联偏差值。 

 返回最可能的 logprobs 个输出 token 的对数概率，同时包含被选中 token 的概率。例如，如果 logprobs 设为 5，API 会返回每步生成时前 5 个最可能 token 的对数概率列表。

logprobs 的最大值为 5。 

 默认为 1。生成 best\_of 个对话并在服务器端进行处理，返回‘最佳’（即每个 tokens 的对数概率最高的那个）。结果无法流式传输。

与 n 一起使用时，best\_of 控制候选对话的数量，n 指定返回多少个对话。best\_of 必须大于 n。

注意：由于此参数会生成多个对话，因此可能会快速消耗您的 tokens 计费额度。请谨慎使用，并确保为 max\_tokens 和 stop 设置了合理的值。 

## 响应

 生成的对话选择列表。   模型停止生成 tokens 的原因。如果模型遇到自然停止点或提供的停止序列，则为 ‘stop’；如果请求中指定的最大 tokens 数量已达到，则为 ‘length’。枚举值: `stop,length`。   对话选择的索引。   最有可能的 tokens 的对数概率。   文本偏移的整数数组。   token 对数概率的数字数组。   tokens 的字符串数组。   包含 top 对数概率的对象数组。   给定键的对数概率值。       对话返回的内容。  

 响应生成的 Unix 时间戳（以秒为单位）。 

 响应的唯一标识符。 

 用于对话的模型。 

 对象类型，始终为 text\_completion。 

 使用统计。

对于流式回复，usage 字段被包含在返回的最后一个回复块中。   对话生成的 tokens 数。   prompt 中的 tokens 数。   请求中使用的总 tokens 数（prompt + completion）。
