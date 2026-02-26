---
title: "LangBot"
url: "https://docs.jiekou.ai/docs/integration/langbot.md"
crawled_at: "2026-02-26T23:31:17.962506"
---

Published Time: Thu, 26 Feb 2026 15:31:17 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# LangBot

LangBot 是一个开源的大语言模型（LLM）原生即时通信机器人平台，旨在提供开箱即用的 IM 机器人开发体验，具有 Agent、RAG、MCP 等多种 LLM 应用功能，适配飞书、钉钉、QQ 、企业微信、Discord、Slack 等全球主流即时通信平台，并提供丰富的 API 接口，支持自定义开发。

在JieKou.AI 提供的模型 API 服务加持下，LangBot 可接入 Claude-sonnet-4-5、Gpt-5、Gpt-4o、Gemini-2.5-pro 等海内外主流模型，用户可按需选择，适配不同场景调用需求。

# JieKou.AI × LangBot 配置教程

## 1.获取API key

访问[JieKou.AI](https://jiekou.ai/),注册并登录。

填写邀请码【YGHNZ0】可得 \$2 注册奖励。

### **（1）获取 API 密钥**

打开【API key】管理页面，点击添加按钮，输入自定义密钥名称，生成API密钥。

![Image 1](https://mintcdn.com/jiekou/VH6T3aYyodfbgXLh/images/apikey-management.png?fit=max&auto=format&n=VH6T3aYyodfbgXLh&q=85&s=9b9c1a2ad7bfd1d74e26b22ed5c401d5)

### **（2）生成并保存 API 密钥**

\*\*!!注意：\*\*密钥在服务端是加密存储，创建后无法再次查看，请妥善保存好密钥；若遗失需要在控制台上删除并创建一个新的密钥。

![Image 2](https://mintcdn.com/jiekou/OxdfhkzbMZ3sorJ1/images/apikey-list.png?fit=max&auto=format&n=OxdfhkzbMZ3sorJ1&q=85&s=6fe186a02a7c1d15b67fa8799599a1cd)

### **（3）获取【模型 ID】**

**推荐使用的模型 ID：**

* Claude-sonnet-4-5
* Gpt-5
* Gpt-4o
* Gemini-2.5-pro

其他模型 ID、最大上下文及价格可参考[模型广场](https://jiekou.ai/models-console/library)。

![Image 3](https://mintcdn.com/jiekou/OxdfhkzbMZ3sorJ1/images/model-square.png?fit=max&auto=format&n=OxdfhkzbMZ3sorJ1&q=85&s=779df074aecc6dbb48e4ee6747ee22f1)

## 2.部署并配置 LangBot

通过 Docker 可以方便地将 LangBot 部署到 Windows, Mac, Linux 上。

部署前，请先确保 Git、 Docker 和 Docker Compose 已安装。

项目地址：*[https://github.com/RockChinQ/LangBot](https://github.com/RockChinQ/LangBot)*

### **（1）通过 Docker 部署 LangBot**

Git 克隆本项目：

```
git clone https://github.com/langbot-app/LangBot
cd LangBot/docker
```

启动容器：

```
docker compose up
```

* 如果你的主机位于中国大陆，可以把上方命令的`https://github.com/langbot-app/LangBot`改为`https://gitcode.com/RockChinQ/LangBot`以使用国内镜像源。
* 如果你的主机位于中国大陆，可以考虑把 `docker-compose.yaml` 文件中的镜像名称改为`docker.langbot.app/langbot-public/rockchin/langbot:latest`以使用我们提供的镜像源。
* 推荐设置 Docker 容器代理，以便保证 LangBot 在运行期间的网络访问通畅。

### **（2）创建配置文件**

首次启动会输出创建配置文件的提示，请继续按照文件配置。

容器会映射 5300 端口供 WebUI 使用，您可以访问 [http://127.0.0.1:5300](http://127.0.0.1:5300) 查看 WebUI。

还会映射 2280-2290 端口供使用 OneBot 协议的消息平台适配器反向连接。

### **（3）配置对话模型**

打开 LangBot，点击模型配置，模型提供商选择 **接口AI**。

按以下信息配置模型。

* 模型名称：从 JieKou.AI 官网复制的所需模型名称
* 模型提供商：接口AI
* 请求 URL：*[https://api.jiekou.ai/openai](https://api.jiekou.ai/openai)*
* API Key：从 JieKou.AI 官网保存的密钥

![Image 4](https://mintcdn.com/jiekou/OxdfhkzbMZ3sorJ1/images/langbot-create-model.png?fit=max&auto=format&n=OxdfhkzbMZ3sorJ1&q=85&s=855efd9a4647cc42f8b62e9241b69acd)

## **3.接入平台**

LangBot 支持将聊天机器人接入到 QQ、微信公众平台、飞书等平台，以钉钉为例， LangBot 接入教程如下。

### **（1）创建机器人**

进入钉钉开发者后台，登录并且进入组织。

地址：*[https://open-dev.dingtalk.com/](https://open-dev.dingtalk.com/)*

点击上方的【应用开发】，选择【创建应用】，填写机器人的基本信息并保存。

![Image 5](https://mintcdn.com/jiekou/OxdfhkzbMZ3sorJ1/images/langbot-dingding-1.png?fit=max&auto=format&n=OxdfhkzbMZ3sorJ1&q=85&s=92febfbbeb51f4c20045bdde33855518)

进入机器人的后台，比如我们有机器人 langbot2 ,那么它的管理页面是这样的：

![Image 6](https://mintcdn.com/jiekou/OxdfhkzbMZ3sorJ1/images/langbot-dingding-2.png?fit=max&auto=format&n=OxdfhkzbMZ3sorJ1&q=85&s=95c961d7e8e81187ab69a07aecee8c46)

### **（2）配置机器人**

选择【添加应用能力】，为应用添加机器人能力。

点击左侧【机器人】选项卡，填写机器人配置信息，完成名称、简介、消息名称等基础配置，配置完成后，点击发布。

![Image 7](https://mintcdn.com/jiekou/OxdfhkzbMZ3sorJ1/images/langbot-dingding-3.png?fit=max&auto=format&n=OxdfhkzbMZ3sorJ1&q=85&s=cfcd19931624e511ce0bd951da2639d6)

发布成功之后，点击左侧最下方的【版本管理与发布】，配置应用版本号及版本描述。

如果是第一次创建机器人，那么右边是空的，需要点击【创建新版本】，在其中设置信息，然后设置【应用可见范围】，点击保存。

【事件订阅】选择【Stream 模式】，无需注册公网回调地址。

![Image 8](https://mintcdn.com/jiekou/OxdfhkzbMZ3sorJ1/images/langbot-dingding-4.png?fit=max&auto=format&n=OxdfhkzbMZ3sorJ1&q=85&s=524ade696c50b26224bb30b616130ab2)

点击【凭证与基础信息】，记录 Client ID 和 Client Secret， 点击左侧机器人，记录下 RobotCode 和 机器人名称。

以上配置项记录下来后，填到 LangBot 机器人配置表单中，点击[卡片平台](https://open-dev.dingtalk.com/fe/card?spm=ding_open_doc.document.0.0.33cf2281L0fXsV)模板列表复制绑定的对应的模板id填入卡片模板id。

![Image 9](https://mintcdn.com/jiekou/OxdfhkzbMZ3sorJ1/images/langbot-dingding-5.png?fit=max&auto=format&n=OxdfhkzbMZ3sorJ1&q=85&s=f85f781c4a25c2240442c670b53b0496)

启动 LangBot ，编辑机器人，绑定流水线（初始会有一个 ChatPipeline 流水线），平台选择钉钉。

编辑流水线，在 AI 能力配置中，选择内置 Agent，并选择此前绑定好的所需模型。

![Image 10](https://mintcdn.com/jiekou/OxdfhkzbMZ3sorJ1/images/langbot-dingding-6.png?fit=max&auto=format&n=OxdfhkzbMZ3sorJ1&q=85&s=f7a671f81a03cc2607887c638e59ee0f)

### **（3）添加机器人**

在钉钉搜索刚刚配置的机器人名称，点击机器人即可和机器人聊天。

![Image 11](https://mintcdn.com/jiekou/OxdfhkzbMZ3sorJ1/images/langbot-dingding-7.png?fit=max&auto=format&n=OxdfhkzbMZ3sorJ1&q=85&s=736ba0695c9838e1a242bf81ba0e5e0b)

如果想要将机器人添加到群里，可以点击钉钉群的【群管理】选择【添加机器人】，然后搜索机器人名称即可在群聊中使用。
