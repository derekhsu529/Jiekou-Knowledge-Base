---
title: "Chatbox"
url: "https://docs.jiekou.ai/docs/integration/chatbox.md"
crawled_at: "2026-02-26T23:31:07.823076"
---

Published Time: Thu, 26 Feb 2026 15:31:07 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chatbox

Chatbox 是一个开源的对话应用框架，内置对接大语言模型（如 ChatGPT）的功能，可用于快速搭建基于 AI 的智能聊天工具。
Chatbox 支持丰富的自定义配置，适合个人开发者以及企业开发场景，能够灵活应用于客户服务、知识问答、内容创作、团队协作等场景。

通过对接 JieKou.AI，你可以轻松接入多种开源、闭源大模型，包括 GPT-5、Gemini 2.5、以及其他兼容 OpenAI 接口的模型，享受更高的灵活性和扩展性。

## Chatbox 关键介绍

1. 开源框架
   Chatbox 是完全开源的项目，代码可审计，可根据你的需求进行二次开发，支持扩展更多功能。
2. 支持多模型接入
   默认支持 OpenAI 官方的 GPT 系列模型，同时开放接口配置，允许接入其他兼容模型，灵活满足不同场景需求。
3. 丰富的功能场景

* 搭建智能聊天机器人
* 人工智能内容生成（如文案写作、代码生成）
* 企业知识管理对话助手
* 客户服务 FAQ
* 多语言翻译与对话支持

4. 跨平台支持
   客户端和服务端均可灵活部署，支持浏览器运行，也支持本地化部署，兼容性强。

## 为什么选择 JieKou.AI 对接 Chatbox？

1. 统一标准接口
   jiekou.ai 完全兼容 OpenAI 官方 API 格式，无需重新编写代码，仅需替换 API 地址即可完成快速迁移。
2. 多模型支持
   除 GPT 系列模型外，还支持其他如中文大模型等多种开源和专有模型，满足更多业务场景需求。
3. 高性价比
   提供灵活的计费模式，帮助企业降低智能对话相关的运营成本。
4. 稳定可靠
   稳定的技术架构与服务支持，保障模型调用的高可用性体验。

如何对接 JieKou.AI 与 Chatbox？

只需 3 步配置，即可实现对接：

1. 获取 API Key

* 登录 jiekou.ai 官网 注册并进入管理后台，点击右上方“我的”，在下拉列表中选择“API 密钥管理”
  ![Image 1](https://mintcdn.com/jiekou/VH6T3aYyodfbgXLh/images/apikey-management.png?fit=max&auto=format&n=VH6T3aYyodfbgXLh&q=85&s=9b9c1a2ad7bfd1d74e26b22ed5c401d5)
* 点击“添加”，输入密钥名称
  ![Image 2](https://mintcdn.com/jiekou/VH6T3aYyodfbgXLh/images/create-apikey.png?fit=max&auto=format&n=VH6T3aYyodfbgXLh&q=85&s=4097234c8ebd43e5ec6cab648deccf93)
* 点击复制，并记录下生成的 Key(控制台不可再次查看)，在后续配置中使用
  ![Image 3](https://mintcdn.com/jiekou/VH6T3aYyodfbgXLh/images/save-apikey.png?fit=max&auto=format&n=VH6T3aYyodfbgXLh&q=85&s=567b2bf1f4b8ed266120bdea1064b843)

2. 按如下图配置，即可实现 Chatbox 与 JieKou.AI 的无缝对接
   ![Image 4](https://mintcdn.com/jiekou/VH6T3aYyodfbgXLh/images/configures-jiekou-in-chatbox.png?fit=max&auto=format&n=VH6T3aYyodfbgXLh&q=85&s=839145053e576c592e0313fbe09de362)
