---
title: "Chat 模式"
url: "https://docs.jiekou.ai/docs/cc/chat-mode.md"
crawled_at: "2026-02-26T23:30:57.842523"
---

Published Time: Thu, 26 Feb 2026 15:30:57 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat 模式

“Chat 模式” 是 Cloud Code 提供的一种默认的与 Claude Code 协作完成任务的方式，如果您不适应原生的 TUI（Terminal User Interface）交互方式，您可以在 “Chat 模式” 下通过聊天框与 Claude Code 协作完成任务。

## 开始对话

  确保已选中一个项目，且项目状态为 **「running」**   打开一个[会话](/docs/cc/session)，在右侧聊天框底部输入框输入你的需求   按 **Enter** 或点击 **发送按钮** 

  ![Image 1: Chat 模式开始会话](https://mintcdn.com/jiekou/680GrIEScnQsSrRs/docs/cc/assets/chat-mode-start-conversation.png?fit=max&auto=format&n=680GrIEScnQsSrRs&q=85&s=f9992fbc444a08a37dbfb3a339b4bd07)

## 选择模型

点击输入框上方的模型选择器，可以切换不同的模型，当前支持接口 AI 上所有提供 [兼容 Anthropic API](/docs/model/llm-anthropic-compatibility) 的大语言模型。

  ![Image 2: Chat 模式模型选择](https://mintcdn.com/jiekou/680GrIEScnQsSrRs/docs/cc/assets/chat-mode-choose-model.png?fit=max&auto=format&n=680GrIEScnQsSrRs&q=85&s=3c72cd346455c71078b532212a1b69a5)

## 权限模式

Cloud Code 提供三种权限模式，控制 Claude Code 执行操作的方式：

  Claude Code 修改文件前需要你确认。适合谨慎操作的场景。 **特点：** * 每次文件修改都需要手动批准 * 可以预览更改内容后再决定 * 适合重要项目或学习 Claude Code 行为   Claude Code 可以自动执行所有操作。适合信任 AI 自主完成任务。 **特点：** * 无需手动确认，Claude Code 直接执行 * 开发效率最高 * 适合快速原型和熟悉 Claude Code 后使用   Claude Code 先制定计划，等待你批准后再执行。适合复杂任务的分步执行。 **特点：** * Claude Code 先分析任务并制定执行计划 * 你可以审查和修改计划 * 批准后按计划逐步执行 * 适合大型功能开发 

## 上传文件

你可以上传文件让 Claude 分析：

  点击输入框旁的附件图标选择文件   直接拖拽文件到输入框区域 

**支持的文件类型：**

* 代码文件（.py, .js, .ts, .html, .css 等）
* 文本文件（.txt, .md, .json 等）
* 图片文件（.png, .jpg, .gif 等）

 Claude Code 可以分析和理解上传的内容，包括代码逻辑和图片内容。 

  ![Image 3: 点击上传文件](https://mintcdn.com/jiekou/680GrIEScnQsSrRs/docs/cc/assets/cc-click-upload-file.png?fit=max&auto=format&n=680GrIEScnQsSrRs&q=85&s=2519326d8010022be7ae95c338a2909b)

## 查看工具调用

当 Claude Code 执行操作时，你可以看到详细的工具调用信息：

*  **工具名称**（如 `edit_file`、`bash`） *  **输入参数** *  **执行结果** *  **执行时间** 点击工具调用可以展开/折叠详细信息。  ![Image 4: 查看工具调用](https://mintcdn.com/jiekou/680GrIEScnQsSrRs/docs/cc/assets/cc-tool-call-details.png?fit=max&auto=format&n=680GrIEScnQsSrRs&q=85&s=99d5863689d63e4eaa2e76d6da2cf293) ### Claude Code 可用的工具 Claude Code 在 Cloud Code 中可以使用以下工具： | 工具 | 说明 | | ------------ | ------- | | `read_file` | 读取文件内容 | | `write_file` | 创建或覆盖文件 | | `edit_file` | 编辑现有文件 | | `bash` | 执行终端命令 | | `glob` | 搜索文件 | | `grep` | 搜索文件内容 | ## 控制响应 ### 停止响应 两种方式停止 Claude Code 的响应： * 点击输入框旁的 **停止** 按钮 * 按 `Esc` 键  Claude Code 会尽快停止生成，但已执行的操作不会回滚。  ![Image 5: 停止响应](https://mintcdn.com/jiekou/680GrIEScnQsSrRs/docs/cc/assets/cc-session-stop-task.png?fit=max&auto=format&n=680GrIEScnQsSrRs&q=85&s=92d7142b4a365dee4680cdd8206babe5) ### 重新生成 如果对 Claude Code 的响应不满意，可以： 1. 编辑你的消息重新发送 2. 提供更详细的说明让 Claude Code 重新尝试 3. 创建新会话从头开始 ## 最佳实践 ### 有效的提示   明确描述你想要的功能和预期行为   告诉 Claude Code 项目背景和技术栈   复杂任务分解为小步骤逐一完成   根据结果提供反馈，让 Claude Code 改进  ### 示例：有效 vs 无效提示 | 无效提示 | 有效提示 | | -------- | ------------------------------------- | | "帮我写代码" | "创建一个 Python 函数，接受用户名和年龄，返回格式化的欢迎消息" | | "修复 bug" | "login.py 第 42 行报 TypeError，请分析原因并修复" | | "优化一下" | "这个函数处理大数组时很慢，请使用更高效的算法优化" | ## 相关文档   管理项目中的会话信息   Shell 模式下，你能在浏览器中获得 Claude Code 的原生终端体验。
