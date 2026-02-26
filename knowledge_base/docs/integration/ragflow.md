---
title: "RAGFlow"
url: "https://docs.jiekou.ai/docs/integration/ragflow.md"
crawled_at: "2026-02-26T23:31:23.851053"
---

Published Time: Thu, 26 Feb 2026 15:31:23 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# RAGFlow

RAGFlow 是一款基于深度文档理解的开源 RAG（检索增强生成）引擎。它将前沿的 RAG 技术与代理功能融合，为生命周期管理 (LLM) 创建卓越的上下文层。它提供精简的 RAG 工作流程，可适应各种规模的企业。RAGFlow 由融合的上下文引擎和预构建的代理模板驱动，使开发人员能够以卓越的效率和精度将复杂数据转化为高保真、可用于生产环境的 AI 系统。

为了帮助大家更好地使用 RAGFlow，我们准备了一份详细教程，从环境配置到接入『接口AI』，3 分钟教你玩转 RAGFlow！

## 1.配置前置条件

### （1）获取 API 密钥注册

注册并登录 JieKou.AI，注册时填写邀请码【YGHNZ0】可得 \$2 注册奖励。
![Image 1: Example Image1](https://mintcdn.com/jiekou/plu1OZSHwjdzCc5v/images/common_jiekou_homepage.png?fit=max&auto=format&n=plu1OZSHwjdzCc5v&q=85&s=ca878d25d643316d41367137b72b4a28)

打开【API key】管理页面，点击添加按钮，输入自定义密钥名称，生成API密钥。

![Image 2: Example Image2](https://mintcdn.com/jiekou/plu1OZSHwjdzCc5v/images/common_apikey_menu.png?fit=max&auto=format&n=plu1OZSHwjdzCc5v&q=85&s=742c54b92cd31a1ea915392ec52d8710)
![Image 3: Example Image3](https://mintcdn.com/jiekou/pF-N45tDYnwOGbkA/images/ragflow_3.png?fit=max&auto=format&n=pF-N45tDYnwOGbkA&q=85&s=f0c6277859a61e9610b18844c6239b4e)

### （2）生成并保存 API 密钥

!注意:密钥在服务端是加密存储，创建后无法再次查看，请妥善保存好密钥；若遗失需要在控制台上删除并创建一个新的密钥。

![Image 4: Example Image4](https://mintcdn.com/jiekou/plu1OZSHwjdzCc5v/images/common_apikey_save.png?fit=max&auto=format&n=plu1OZSHwjdzCc5v&q=85&s=30053211224f16298aefbe8602e71089)

### （3）获取需要使用的模型 ID

在 JieKou.AI 的模型广场找到想用的模型，复制模型id和基础URL。

![Image 5: Example Image5](https://mintcdn.com/jiekou/plu1OZSHwjdzCc5v/images/common_model_square-gemini-3-pro.png?fit=max&auto=format&n=plu1OZSHwjdzCc5v&q=85&s=29c3faf0dd833d9b8bbee105c96c80f1)

* Gemini-3-pro-preview
* Gemini-2.5-pro
* Claude-sonnet-4-5
* Gpt-5.1
* Gpt-4o

其他模型ID、最大上下文及价格可参考：[模型广场](https://jiekou.ai/models-console/library?auth_res=success\&is_reg=false)

## 2. RAGFlow添加与配置LLM

### （1）访问 [RAGFlow 官网](https://ragflow.io/)

![Image 6: Example Image6](https://mintcdn.com/jiekou/pF-N45tDYnwOGbkA/images/ragflow_6.png?fit=max&auto=format&n=pF-N45tDYnwOGbkA&q=85&s=e2bee53f85c4032e71edd30dac854d90)

### （2）添加模型

选择【模型供应商】，找到【OpenAI-API-Compatible】，点击【添加模型】

![Image 7: Example Image7](https://mintcdn.com/jiekou/pF-N45tDYnwOGbkA/images/ragflow_7.png?fit=max&auto=format&n=pF-N45tDYnwOGbkA&q=85&s=b596fd313f9a4b5b09337c983913ab03)

### （3）选择和填写对应配置。

![Image 8: Example Image8](https://mintcdn.com/jiekou/pF-N45tDYnwOGbkA/images/ragflow_8.png?fit=max&auto=format&n=pF-N45tDYnwOGbkA&q=85&s=08a07e66bdd0b2af890450caaed6df0e)

### （4）添加成功。

![Image 9: Example Image9](https://mintcdn.com/jiekou/pF-N45tDYnwOGbkA/images/ragflow_9.png?fit=max&auto=format&n=pF-N45tDYnwOGbkA&q=85&s=f3d80be5a4ff0a77f54ae71a18bf31b3)

关于RAGFlow的更多配置，您可参考[RAGFlow文档](https://ragflow.io/docs/dev/)。
