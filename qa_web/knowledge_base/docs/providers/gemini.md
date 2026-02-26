---
title: "Gemini"
url: "https://docs.jiekou.ai/docs/providers/gemini.md"
crawled_at: "2026-02-26T23:41:57.475936"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini

平台支持使用 OpenAI chat/completions 协议和 Gemini 原生协议访问 Gemini 模型。

以下示例均使用非 Stream 模式，如需 Stream 模式，改 Path 为 /gemini/v1/models/{model}:**streamGenerateContent** 即可。

## 快速开始

<CodeGroup>
  ```bash OpenAI theme={null}
  curl https://api.jiekou.ai/openai/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <YOUR-API-KEY>" \
  -d '{
      "model": "gemini-2.5-flash",
      "messages": [{
          "role": "user", "content": "What is the capital of France?"
      }],
      "reasoning_effort": "low"
    }'
  ```

  ```bash Gemini theme={null}
  curl https://api.jiekou.ai/gemini/v1/models/gemini-2.5-flash:generateContent \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <YOUR-API-KEY>" \
  -d '{
      "contents": [{
          "role": "user",
          "parts": [{"text": "What is the capital of France?"}]
      }],
      "generationConfig": {
          "thinkingConfig": {
              "thinkingBudget": 1024
          }
      }
    }'
  ```
</CodeGroup>

## OpenAI 协议思考控制

平台会将 OpenAI chat/completions 请求的 reasoning\_effort 参数转换为 Gemini thinking 参数。

| reasoning\_effort | thinking               |
| ----------------- | ---------------------- |
| "disable", "none" | "budget\_tokens": 0    |
| "low"             | "budget\_tokens": 1024 |
| "medium"          | "budget\_tokens": 2048 |
| "high"            | "budget\_tokens": 4096 |

⚠️ 非 OpenAI 标准值 disable/none 可用于关闭思考过程

### 各模型默认设置

| 模型             | 默认设置（未设置 reasoning\_effort） |
| -------------- | --------------------------- |
| 2.5 Pro        | 动态思考：模型决定何时以及思考多少           |
| 2.5 Flash      | 动态思考：模型决定何时以及思考多少           |
| 2.5 Flash Lite | 思考已禁用                       |

⚠️ 无法为 Gemini 2.5 Pro 禁用思考，reasoning\_effort: none 将被转换为最小 thinkingBudget 128
⚠️ thinkingBudget 仅在 Gemini 2.5 Flash、2.5 Pro 和 2.5 Flash-Lite 中支持。根据提示的不同，模型可能会超出或低于 token 预算。

## 服务端工具使用

### Google Search

依托 Google Search 可将 Gemini 模型与实时网络内容相关联，并支持所有可用语言。这样一来，Gemini 就可以提供更准确的回答，并引用知识截止日期之后的可验证来源。

<CodeGroup>
  ```bash OpenAI theme={null}
  curl https://api.jiekou.ai/openai/chat/completions \
  -H "Authorization: Bearer <YOUR-API-KEY>" \
  -H "Content-Type: application/json" -d @- <<EOF
  {
    "model": "gemini-2.5-flash-lite",
    "messages": [
      {
        "role": "user",
        "content": "列一下今天中国的热点新闻"
      }
    ],
    "tools": [
      {
        "function": {"name": "google_search"}
      }
    ]
  }
  EOF
  ```

  ```bash Gemini theme={null}
  curl https://api.jiekou.ai/gemini/v1/models/gemini-2.5-flash-lite:generateContent \
  -H "Authorization: Bearer <YOUR-API-KEY>" \
  -H "Content-Type: application/json" -d @- <<EOF
  {
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "列一下今天中国的热点新闻"}]
      }
    ],
    "tools": [
      {
        "googleSearch": {}
      }
    ]
  }
  EOF
  ```
</CodeGroup>

结果示例如下，OpenAI 协议可从非标准字段 gemini\_grounding\_metadata 可获取 Grounding 信息。

<CodeGroup>
  ```json OpenAI theme={null}
  {
    "id": "dcc7eab10b5adeb9e8648d134e815409",
    "object": "chat.completion",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "Here are some of today's top news in China: ..."
        },
        "finish_reason": "stop"
      }
    ],
    "gemini_grounding_metadata": {  # 👈 GEMINI GROUNDING
      "webSearchQueries": [
        "中国今日热点新闻"
      ],
      ...
      "groundingChunks": [
        ...
      ]
    }
  }
  ```

  ```json Gemini theme={null}
  {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": "根据您提供的搜索结果，以下是今日中国的一些热点新闻：..."
            }
          ]
        },
        "finishReason": "STOP",
        "index": 0,
        "groundingMetadata": {
          "webSearchQueries": [
            "今日中国热点新闻",
            "中国最新新闻头条"
          ],
          "searchEntryPoint": {...},
          "groundingChunks": [...],
          "groundingSupports": [...]
        }
      }
    ]
  }
  ```
</CodeGroup>

### Code Execution

Gemini 提供了一个代码执行工具，可让模型生成和运行 Python 代码。然后，模型可以根据代码执行结果进行迭代学习，直到获得最终输出。

<CodeGroup>
  ```bash OpenAI theme={null}
  curl https://api.jiekou.ai/openai/chat/completions \
  -H "Authorization: Bearer <YOUR-API-KEY>" \
  -H "Content-Type: application/json" -d @- <<EOF
  {
    "model": "gemini-2.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
      }
    ],
    "tools": [
        {
             "function":  {"name": "code_execution"}
        }
    ],
    "reasoning_effort": "low"
  }
  EOF
  ```

  ```bash Gemini theme={null}
  curl https://api.jiekou.ai/gemini/v1/models/gemini-2.5-flash:generateContent \
  -H "Authorization: Bearer <YOUR-API-KEY>" \
  -H "Content-Type: application/json" -d @- <<EOF
  {
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."}]
      }
    ],
    "tools": [
      {
        "codeExecution": {}
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingBudget": 1024
      }
    }
  }
  EOF
  ```
</CodeGroup>

结果示例如下，对于 OpenAI 协议，代码和代码执行结果将在 content 中体现。对于 Gemini 协议，代码在 executableCode 字段， 执行结果在 codeExecutionResult 字段，总结在 text 字段。

<CodeGroup>
  ````markdown OpenAI theme={null}
  Okay, I can help you with that. I will write a Python script to find the
  first 50 prime numbers and then calculate their sum.

  Here's the plan:

  1.  Create a function to check if a number is prime.
  2.  Create a function to generate the first `n` prime numbers.
  3.  Call the generation function for the first 50 primes.
  4.  Sum the resulting list of primes.

  Here is the code to perform this calculation:

  ```PYTHON
  def is_prime(num):
      """Checks if a number is prime."""
      if num <= 1:
          return False
      if num <= 3:
          return True
      if num % 2 == 0 or num % 3 == 0:
          return False
      i = 5
      while i * i <= num:
          if num % i == 0 or num % (i + 2) == 0:
              return False
          i += 6
      return True

  def get_first_n_primes(n):
      """Generates a list of the first n prime numbers."""
      primes = []
      num = 2
      while len(primes) < n:
          if is_prime(num):
              primes.append(num)
          num += 1
      return primes

  # Get the first 50 prime numbers
  first_50_primes = get_first_n_primes(50)


  # Calculate the sum of these prime numbers

  sum_of_primes = sum(first_50_primes)


  print(f"The first 50 prime numbers are: {first_50_primes}")

  print(f"The sum of the first 50 prime numbers is: {sum_of_primes}")
  \```

  The first 50 prime numbers are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
  37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
  109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
  193, 197, 199, 211, 223, 227, 229]

  The sum of the first 50 prime numbers is: 5117
  ````

  ```markdown Gemini theme={null}
  - executableCode:
      language: PYTHON
      code: |
        import sympy

        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        prime_numbers = []
        num = 2
        while len(prime_numbers) < 50:
            if is_prime(num):
                prime_numbers.append(num)
            num += 1

        sum_of_primes = sum(prime_numbers)

        print(f"The first 50 prime numbers are: {prime_numbers}")
        print(f"The sum of the first 50 prime numbers is: {sum_of_primes}")
  - codeExecutionResult:
      outcome: OUTCOME_OK
      output: >
        The first 50 prime numbers are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
        107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229]

        The sum of the first 50 prime numbers is: 5117
  - text: The sum of the first 50 prime numbers is 5117.
  ```
</CodeGroup>

### URL context

借助 URL context 工具，您可以网址的形式向模型提供更多上下文。
通过在请求中添加网址，模型将访问这些网页中的内容，从而为回答提供信息并提高回答质量。

<CodeGroup>
  ```bash OpenAI theme={null}
  curl https://api.jiekou.ai/openai/chat/completions \
  -H "Authorization: Bearer <YOUR-API-KEY>" \
  -H "Content-Type: application/json" -d @- <<EOF
  {
    "model": "gemini-2.5-flash-lite",
    "messages": [
      {
        "role": "user",
        "content": "这份食谱适合什么人士 https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
      }
    ],
    "tools": [
      {
        "function": {"name": "url_context"}
      }
    ]
  }
  EOF
  ```

  ```bash Gemini theme={null}
  curl https://api.jiekou.ai/gemini/v1/models/gemini-2.5-flash-lite:generateContent \
  -H "Authorization: Bearer <YOUR-API-KEY>" \
  -H "Content-Type: application/json" -d @- <<EOF
  {
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "这份食谱适合什么人士 https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"}]
      }
    ],
    "tools": [
      {
        "urlContext": {}
      }
    ]
  }
  EOF
  ```
</CodeGroup>

示例响应如下

<CodeGroup>
  ```json OpenAI theme={null}
  {
    "id": "82f10046aebe6697ed9d33a9fa398de4",
    "object": "chat.completion",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "这份食谱是关于如何制作 Ina Garten 的完美烤鸡。\n\n**关键信息：**\n* **食谱来源：** Ina Garten，改编自《Barefoot Contessa Cookbook》。\n* **准备时间：** 20 分钟\n* **烘烤时间：** 1 小时 30 分钟\n* **总时间：** 2 小时 10 分钟\n* **份量：** 8 人份\n* **难度：** 中等\n\n**食材：**\n* 一只 5-6 磅的烤鸡\n* 犹太盐\n* 新鲜磨碎的黑胡椒\n* 一大把新鲜百里香，外加 20 枝\n* 一个柠檬，对半切\n* 一头大蒜，横向切半\n* 2 汤匙（1/4 条）黄油，融化\n* 1 个大黄洋葱，厚切\n* 4 根胡萝卜，切成 2 英寸块\n* 1 个茴香头，去掉顶部，切成楔形\n* 橄榄油\n\n**制作步骤：**\n1. 预热烤箱至 425 华氏度（约 220 摄氏度）。\n2. 清理鸡的内脏，冲洗鸡的内外。去除多余的脂肪和残留的羽毛，并拍干鸡的外部。\n3. 在鸡的内部慷慨地撒上盐和胡椒。将一把百里香、半个柠檬和所有大蒜塞入鸡腔。\n4. 用融化的黄油刷鸡的外部，并再次撒上盐和胡椒。\n5. 用厨房绳子将鸡腿绑在一起，并将鸡翅尖塞到鸡身下方。\n6. 将洋葱、胡萝卜和茴香放入烤盘。用盐、胡椒、20 枝百里香和橄榄油拌匀。将蔬菜铺在烤盘底部，然后将鸡放在蔬菜上面。\n7. 烘烤鸡肉 1.5 小时，或直至用刀在腿和 thigh 之间切割时，汁水清澈。\n8. 将烤好的鸡和蔬菜移至盘子，用铝箔覆盖静置约 20 分钟。\n9. 将鸡肉切片装盘，与蔬菜一起食用。\n\n**烹饪技巧和用户反馈：**\n* 食谱中提到，如果蔬菜底部开始变褐色，可以加入一杯鸡汤帮助保持湿润。\n* 有用户建议使用更小的烤盘，以避免蔬菜烤焦。\n* 有用户将茴香替换成土豆。\n* 许多用户反馈鸡肉非常鲜嫩多汁，风味十足，而且烹饪过程简单。"
        },
        "finish_reason": "stop"
      }
    ],
    "gemini_grounding_metadata": {
      "groundingChunks": [
        {
          "web": {
            "uri": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "title": "Perfect Roast Chicken Recipe | Ina Garten | Food Network"
          }
        }
      ],
      "groundingSupports": [....]
    }
  }
  ```

  ```json Gemini theme={null}
  {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [
            {
              "text": "\n这份食谱适合那些喜欢经典烤鸡的人士，特别是对于那些想要制作一道美味又相对容易的菜肴的家庭厨师来说。食谱的难度被评为“中等”，总共需要2小时10分钟（包括20分钟的准备时间，20分钟的空闲时间，以及1小时30分钟的烹饪时间）。\n\n此外，它也适合那些希望在聚会或特殊场合制作一道令人印象深刻的主菜的人士，因为烤鸡通常是节日餐桌上的亮点。\n\n食谱还提到了可以根据个人口味调整配料，例如有评论提到可以省略茴香，或者加入鸡汤来帮助 Basting，这表明它也可以适合那些喜欢在烹饪中进行尝试和调整的人。"
            }
          ]
        },
        "finishReason": "STOP",
        "index": 0,
        "safetyRatings": null,
        "groundingMetadata": {
          "groundingChunks": [
            {
              "web": {
                "uri": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
                "title": "Perfect Roast Chicken Recipe | Ina Garten | Food Network"
              }
            }
          ],
          "groundingSupports": [
            {
              "segment": {
                "startIndex": 148,
                "endIndex": 317,
                "text": "食谱的难度被评为“中等”，总共需要2小时10分钟（包括20分钟的准备时间，20分钟的空闲时间，以及1小时30分钟的烹饪时间）。"
              },
              "groundingChunkIndices": [
                0
              ]
            },
            {
              "segment": {
                "startIndex": 319,
                "endIndex": 475,
                "text": "此外，它也适合那些希望在聚会或特殊场合制作一道令人印象深刻的主菜的人士，因为烤鸡通常是节日餐桌上的亮点。"
              },
              "groundingChunkIndices": [
                0
              ]
            },
            {
              "segment": {
                "startIndex": 477,
                "endIndex": 695,
                "text": "食谱还提到了可以根据个人口味调整配料，例如有评论提到可以省略茴香，或者加入鸡汤来帮助 Basting，这表明它也可以适合那些喜欢在烹饪中进行尝试和调整的人。"
              },
              "groundingChunkIndices": [
                0
              ]
            }
          ]
        }
      }
    ],
    "promptFeedback": {
      "safetyRatings": null
    },
    "usageMetadata": {
      "promptTokenCount": 37,
      "candidatesTokenCount": 159,
      "totalTokenCount": 3270,
      "trafficType": "ON_DEMAND",
      "promptTokensDetails": [
        {
          "modality": "TEXT",
          "tokenCount": 37
        }
      ],
      "candidatesTokensDetails": [
        {
          "modality": "TEXT",
          "tokenCount": 159
        }
      ],
      "toolUsePromptTokensDetails": [
        {
          "modality": "TEXT",
          "tokenCount": 3074
        }
      ],
      "toolUsePromptTokenCount": 3074
    },
    "responseId": "0472efecb0da2db5f78d047e70e54db6",
    "modelVersion": "gemini-2.5-flash-lite"
  }
  ```
</CodeGroup>
