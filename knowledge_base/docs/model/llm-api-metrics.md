---
title: "大语言模型监控"
url: "https://docs.jiekou.ai/docs/model/llm-api-metrics.md"
crawled_at: "2026-02-26T23:16:57.032246"
---

Published Time: Thu, 26 Feb 2026 15:16:56 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 大语言模型监控

JieKou AI 为大语言模型 API 使用提供了全面的监控指标。这些指标让您能够深入了解 LLM API 请求的可用性和性能。

您可以通过 [大语言模型（LLM）监控页面](https://jiekou.ai/models-console/llm-metrics) 查看监控指标。

## 指标说明

 以下所有指标均按**模型划分维度**，并以**分钟级别**进行采样，但根据您选择的时间间隔，采样点可能不会每分钟都显示。在这种情况下，该时间间隔内的采样点将被平均后显示。 

* **每分钟请求数 (RPM)**

  显示每分钟发出的 API 请求数量，帮助您了解使用模式和 API 并发级别。
* **请求成功率**

  显示每分钟成功 API 响应（非 5xx 状态码）的百分比，反映 API 的可用性。
* **每个请求的平均 Token 数量**

  显示每分钟每个请求的平均输入和输出 Token 数量，有助于了解 Token 消耗模式。
* **端到端（E2E）延迟**

  显示模型在每分钟请求中生成完整响应所需的总时间。包括 99 分位、95 分位和平均的延迟指标。
* **生成第一个 Token 的时间 (TTFT)**

   该指标仅在启用 `stream=true` 参数的流式请求中进行跟踪。 

  显示每分钟请求中处理 Prompt 并生成第一个输出 Token 所需的时间。包括 99 分位、95 分位和平均的延迟指标。
* **每个输出 Token 的时间 (TPOT)**

   该指标仅在启用 `stream=true` 参数的流式请求中进行跟踪。 

  显示每分钟请求中连续输出 token 之间的平均时间。包括 99 分位、95 分位和平均的延迟指标。
