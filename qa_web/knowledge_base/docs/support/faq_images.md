---
title: "图像与视频生成"
url: "https://docs.jiekou.ai/docs/support/faq_images.md"
crawled_at: "2026-02-26T23:39:15.928577"
---

Published Time: Thu, 26 Feb 2026 15:39:15 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 图像与视频生成

## 1. Nano Banana Pro 和 Light 版本有什么区别？

* Nano Banana Pro：直连官方正式版，稳定性好，支持完整功能（如参考图）
* Nano Banana Pro Light：逆向/破解版本，价格便宜，但稳定性较差，某些特性不支持（如参考图功能可能失效），且可能触发内容审核（PROHIBITED\_CONTENT）

建议：生产环境建议使用非 Light 版本，测试环境可使用 Light 版本节约成本。

## 2. 图像高清化(Upscale)接口只是放大了图片，没有变清晰？

目前 Upscale 接口主要是通过提高分辨率实现"高清化"，并不具备 AI 重绘细节的能力。如需真正的细节增强，建议使用：

* Midjourney 的 Upscale 功能（需配合 MJ 生成的图片使用）
* 或其他专门的图像增强模型

## 3. 生图接口返回 500 错误或排队时间过长？

可能原因：

* 资源紧张：高峰期（如下午、晚上）生视频/生图任务可能排队（TASK\_STATUS\_QUEUED），建议避开高峰期
* Light 版不稳定：如使用 Light 版本，可能出现间歇性失败，建议重试或改用正式版
* 内容审核：提示词触发安全审核（如 Gemini 返回 PROHIBITED\_CONTENT），请修改提示词

## 4. 生成的图片 URL 无法访问？

平台返回的 COS URL 是预签名链接（Presigned URL），通常可以公开访问。如无法访问请检查：

* 是否在复制 URL 时截断或添加了多余字符
* 如用于微信小程序等场景，需配置 CORS（跨域）支持，平台已默认配置，如仍报错请联系客服

## 5. Sora 2 / Veo 3.1 生成慢或失败？

生视频属于重资源任务：

* 排队正常：高峰期可能需要等待 2-30 分钟
* 任务丢失：如超过 30 分钟仍无结果且查询返回 "task not found"，可能是任务失败，建议重试
* 横竖屏问题：部分版本（如 Sora2）的横竖屏参数可能失效，建议先使用默认横屏

***

**联系支持**

如以上 FAQ 无法解决您的问题，请通过以下方式联系技术支持：

* 企业微信/微信技术支持群（推荐，响应最快）
* 提供信息格式：
  * 问题描述 + 截图
  * 账号 ID (UUID)
  * Trace ID（如有，通常在错误信息中）
  * 请求参数（脱敏后）
