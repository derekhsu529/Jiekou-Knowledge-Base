---
title: "其他常见问题"
url: "https://docs.jiekou.ai/docs/support/faq_others.md"
crawled_at: "2026-02-26T23:37:07.780747"
---

Published Time: Thu, 26 Feb 2026 15:37:07 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 其他常见问题

## 1. 对话历史记录在哪里查看？

平台不保存用户对话数据（隐私保护原则）。如需历史记录功能，建议：

* 使用第三方客户端如 ChatBox、Cherry Studio 等
* 在本地保存日志

## 2. Prompt Caching（提示词缓存）为什么显示命中率为 0？

请确认：

1. 使用的模型支持缓存（如 Claude 3.5 Sonnet、GPT-4o 等，GPT-5-mini 目前不支持）
2. 缓存需要预设的提示词前缀完全一致（逐字符匹配）
3. 首次调用会写入缓存（产生写入费用），后续调用才能命中

## 3. 平台模型是代理还是自部署？

闭源模型（如 OpenAI、Claude、Gemini）为官方 API 代理；开源模型 部分为平台自行部署。所有模型均通过统一网关提供稳定接入。

***

**联系支持**

如以上 FAQ 无法解决您的问题，请通过以下方式联系技术支持：

* 企业微信/微信技术支持群（推荐，响应最快）
* 提供信息格式：
  * 问题描述 + 截图
  * 账号 ID (UUID)
  * Trace ID（如有，通常在错误信息中）
  * 请求参数（脱敏后）
