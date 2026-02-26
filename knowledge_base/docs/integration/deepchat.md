---
title: "DeepChat"
url: "https://docs.jiekou.ai/docs/integration/deepchat.md"
crawled_at: "2026-02-26T23:31:13.713431"
---

Published Time: Thu, 26 Feb 2026 15:31:13 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# DeepChat

DeepChat 是一款企业级智能对话平台，基于先进的大语言模型（LLM）技术，为用户提供流畅自然的对话体验。
专注于为以下场景提供解决方案：

* 个人知识管理：整合个人文档、笔记和知识，实现智能问答和内容生成。
* 企业知识库：连接企业内部知识资源，为团队成员提供智能信息检索。
* 自定义对话场景：通过灵活的模型配置和提示词工程，打造适合特定领域的对话体验。

通过对接 JieKou.AI，你可以轻松接入多种海内外大模型，包括 Claude-haiku-4-5、Gemini-2.5-flash、Gpt-5以及其他兼容模型，享受更高的灵活性和扩展性。

只需1分钟，带你轻松配置JieKou.AI × DeepChat 。

# JieKou.AI × DeepChat 配置教程

## 配置前置条件

### (1) 获取 API 密钥注册

注册并登录 JieKou.AI，注册时填写邀请码【YGHNZ0】可得 \$2 注册奖励。

![Image 1](https://mintcdn.com/jiekou/2XtVQU7ONEmqtSfR/images/jiekou-navigate-apikey.png?fit=max&auto=format&n=2XtVQU7ONEmqtSfR&q=85&s=8ba926d3e7d52c80e3444b6aa39a909d)

打开【API key】管理页面，点击添加按钮，输入自定义密钥名称，生成API密钥。

![Image 2](https://mintcdn.com/jiekou/2XtVQU7ONEmqtSfR/images/jiekou-create-apikey-deepchat.png?fit=max&auto=format&n=2XtVQU7ONEmqtSfR&q=85&s=4976af2497d2054b430c390b34f9087b)

### (2) 生成并保存 API 密钥

!注意:密钥在服务端是加密存储，创建后无法再次查看，请妥善保存好密钥；若遗失需要在控制台上删除并创建一个新的密钥。

![Image 3](https://mintcdn.com/jiekou/2XtVQU7ONEmqtSfR/images/jiekou-copy-new-apikey.png?fit=max&auto=format&n=2XtVQU7ONEmqtSfR&q=85&s=251d82bb27b3dde459d41ff3c7381563)

### (3) 获取需要使用的模型 ID

在 JieKou.AI 的模型广场找到想用的模型，复制模型id。

![Image 4](https://mintcdn.com/jiekou/MUvUpK_FaNySwpe5/images/jiekou-copy-model-name.png?fit=max&auto=format&n=MUvUpK_FaNySwpe5&q=85&s=d0aabb7a0b1c5fe8213f3afb75aca2e8)

* Claude-sonnet-4-5
* Gpt-5
* Gpt-4o
* Gemini-2.5-pro

其他模型ID、最大上下文及价格可参考：模型广场

## 软件配置及使用

### (1) 下载并配置服务商

进入 DeepChat 官网，下载并安装软件。

![Image 5](https://mintcdn.com/jiekou/FMV-ESGh4zA2j9mS/images/download-deepchat.png?fit=max&auto=format&n=FMV-ESGh4zA2j9mS&q=85&s=33842ffb269c35302d35f78963592b12)

打开软件，在【选择服务商】中，开启【JieKou.AI】选项，并将此前复制的API密钥粘贴至【API 密钥】输入框。

![Image 6](https://mintcdn.com/jiekou/FMV-ESGh4zA2j9mS/images/deepchat-x-jiekou.png?fit=max&auto=format&n=FMV-ESGh4zA2j9mS&q=85&s=a2773babac40923e667192173a5551cf)

### (2) 配置所需模型，即可开启畅聊

![Image 7](https://mintcdn.com/jiekou/FMV-ESGh4zA2j9mS/images/deepchat-configure-model.png?fit=max&auto=format&n=FMV-ESGh4zA2j9mS&q=85&s=8fbe0b9ba1f51a9e1621a411b6ad5dad)

在 DeepChat【服务商设置】中选择 JieKou.AI并配置模型列表，选择【添加模型】，填入模型id，点击确认。

![Image 8](https://mintcdn.com/jiekou/FMV-ESGh4zA2j9mS/images/deepchat-select-model.png?fit=max&auto=format&n=FMV-ESGh4zA2j9mS&q=85&s=e879d9bdaa2302b3dc0e9761ed8c8d55)

现在，你可以在 DeepChat 畅用海外大模型啦！

![Image 9](https://mintcdn.com/jiekou/FMV-ESGh4zA2j9mS/images/deepchat-ready.png?fit=max&auto=format&n=FMV-ESGh4zA2j9mS&q=85&s=4c5440d85c56ea370e8ac7d38ad702f3)
