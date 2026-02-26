---
title: "会话管理"
url: "https://docs.jiekou.ai/docs/cc/session.md"
crawled_at: "2026-02-26T23:19:50.830049"
---

Published Time: Thu, 26 Feb 2026 15:19:50 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 会话管理

“会话” 是你与 Claude Code 进行对话的容器，其概念与 Claude Code 的 Conversation History（“对话历史”）一致。每个项目可以包含多个会话，不同会话的上下文彼此隔离，适合在同一个项目中处理不同任务或主题而互不干扰。

## 会话概述

每个会话包含：

* **对话历史** — 你与 Claude Code 的对话、工具调用/命令以及关键输出结果，用于维持上下文（例如记住报错文件路径、已讨论的方案等）。
* **项目信息** — Claude Code 记住的项目相关信息。
* **工具调用记录** — Claude Code 执行任务时所有工具调用/命令及其输出结果。

 会话上下文会影响 Claude Code 的响应。如果你想从头开始一个全新的任务，建议创建新会话。 

### 创建会话

  在左侧边栏选择一个项目   在会话列表区域点击 **+ 新会话** 按钮   新会话创建后，即可在右侧聊天框中开始与 Claude Code 对话 

  ![Image 1: 创建新会话](https://mintcdn.com/jiekou/680GrIEScnQsSrRs/docs/cc/assets/cc-new-session.png?fit=max&auto=format&n=680GrIEScnQsSrRs&q=85&s=1d88f80ae7134dc6862ce05f69013112)

### 切换会话

点击会话列表中的任意会话即可切换。切换会话时：

* 当前对话内容会自动保存
* 新会话的历史记录会加载显示
* Claude Code 的上下文会切换到目标会话

### 删除会话

  在会话列表中找到要删除的会话   右键点击会话或点击菜单图标   确认删除操作 

 删除会话会永久删除该会话的所有对话历史，此操作不可撤销。 

## 会话最佳实践

### 何时创建新会话

* **开始新任务** — 当你要开始一个全新的、与之前无关的任务时
* **上下文过长** — 当对话变得很长，响应速度变慢时
* **重新开始** — 当 Claude Code 的理解出现偏差，需要重新开始时
* **分离关注点** — 当你想要分开管理不同功能或模块的开发时

### 何时继续现有会话

* **迭代开发** — 在同一功能上持续迭代改进
* **错误修复** — 修复 Claude Code 之前代码或其他产出物中的错误
* **功能扩展** — 在已有实现的基础上添加新功能
* **上下文相关** — 新问题与之前的对话密切相关

## 会话存储

会话数据存储在项目对应的云端沙箱中，具有以下特性：

| 特性        | 说明                         |
| --------- | -------------------------- |
| **自动保存**  | 对话内容实时自动保存                 |
| **跨设备访问** | 在任何设备使用同一个 API Key 登录后都可访问 |
| **项目绑定**  | 会话与项目关联，删除项目会删除所有会话        |

 重要的对话内容建议导出或复制到本地保存。 

## 相关文档

  管理和组织你的项目   Chat 模式下，你可以通过对话框的形式，让 Claude Code 帮你完成任务。
