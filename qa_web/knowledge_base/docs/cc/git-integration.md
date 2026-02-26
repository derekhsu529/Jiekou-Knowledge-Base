---
title: "Git 集成"
url: "https://docs.jiekou.ai/docs/cc/git-integration.md"
crawled_at: "2026-02-26T23:19:48.776061"
---

Published Time: Thu, 26 Feb 2026 15:19:48 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Git 集成

Cloud Code 内置完整的 Git 支持，您可以通过 Git 来对您的项目内容进行版本控制。

## 配置 Git 用户信息

首次使用需要配置用户信息：

  进入 **设置 > Git**   输入用户名和邮箱   点击保存按钮 

```
用户名：Your Name
邮箱：your.email@example.com
```

 此信息用于 Git 提交记录，建议使用与 GitHub 账户相同的邮箱。 

  ![Image 1: Git 用户信息配置](https://mintcdn.com/jiekou/680GrIEScnQsSrRs/docs/cc/assets/cc-git-config-user.png?fit=max&auto=format&n=680GrIEScnQsSrRs&q=85&s=266562fad0d76b392df90873a5c94283)

## 连接远程仓库

### 配置 GitHub 凭据

  进入 **设置 > Git**   在「Git Credentials」区域点击 **+ 添加** 按钮   输入你的 GitHub Username   输入你的 GitHub Personal Access Token（点击输入框右上角 **创建 Tokens** 按钮，按照提示创建即可）   点击 **保存凭据** 按钮 

如果配置成功，你会看到「Git Credentials」区域显示你的凭据信息，显示为「已激活」。

  ![Image 2: Git 凭据配置](https://mintcdn.com/jiekou/680GrIEScnQsSrRs/docs/cc/assets/cc-git-credentials.png?fit=max&auto=format&n=680GrIEScnQsSrRs&q=85&s=37b3ef5da4b8ae2f0dbe520ea7242bda)

## 初始化 Git 仓库

  点击顶部标签栏的 **源代码管理** 标签   在 GitHub 上创建一个新的空仓库   输入远程仓库地址，并点击 **绑定** 按钮，即可完成 Git 仓库的初始化 

初始化成功后，你会看到「源代码管理」页面下会显示如下界面：

  ![Image 3: Git 仓库列表](https://mintcdn.com/jiekou/680GrIEScnQsSrRs/docs/cc/assets/cc-git-bind-succ.png?fit=max&auto=format&n=680GrIEScnQsSrRs&q=85&s=b7cd8ecec49063985aa2d7a42f7388a9)

## 提交更改

  点击文件旁的 **+** 按钮暂存单个文件，或点击 **全部暂存** 暂存所有更改   在提交信息输入框中描述你的更改   点击 **提交** 按钮将你的更改提交到本地仓库   点击 **发布** 按钮发布你的更改到远程仓库 

## 查看历史

在 Git 面板中可以查看提交历史：

* **提交列表** — 显示所有提交记录
* **提交详情** — 点击提交查看更改的文件
* **文件差异** — 查看具体的代码更改

  ![Image 4: Git 仓库提交历史](https://mintcdn.com/jiekou/680GrIEScnQsSrRs/docs/cc/assets/cc-git-repo-history.png?fit=max&auto=format&n=680GrIEScnQsSrRs&q=85&s=3b0d503397e1268beaaefc86acfcc089)

## 通过 Claude Code 操作 Git

你可以让 Claude Code 帮你执行 Git 操作：

| 请求                    | Claude Code 操作 |
| --------------------- | -------------- |
| "提交这些更改"              | 暂存文件并创建提交      |
| "推送到 GitHub"          | 执行 git push    |
| "创建新分支 feature/login" | 创建并切换分支        |
| "查看提交历史"              | 显示 git log     |
| "回滚到上一个提交"            | 执行 git reset   |

## 相关文档

  管理项目信息   Shell 模式下，你能在浏览器中获得 Claude Code 的原生终端体验。
