---
title: "速率限制与性能"
url: "https://docs.jiekou.ai/docs/support/faq_rpm.md"
crawled_at: "2026-02-26T23:37:09.861276"
---

Published Time: Thu, 26 Feb 2026 15:37:09 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 速率限制与性能

## 1. 生图/生视频模型有 RPM 限制吗？

是的，各模型 RPM（每分钟请求数）限制不同：

* Veo 3.1：约 50 RPM
* Seedance：约 200 RPM
* Kling：视具体模型而定

## 2. 可以申请增加 RPM 限制吗？

可以。允许根据使用需求灵活升级 RPM，请联系我们并告知您的需求。

## 3. 如果实际使用未达到承诺的 RPM 会怎样？

如果用户的实际 RPM 连续一周低于承诺水平，平台将调整速率限制，政策如下（以较低者为准）：

* 将限制减少到过去一周的峰值 RPM
* 恢复到模型的默认速率限制

## 4. 返回 429 "server overload" 或 "RPM limit exceeded" 怎么办？

这是触发了速率限制。各模型限制请参考：[https://docs.jiekou.ai/docs/model/llm-rate-limits](https://docs.jiekou.ai/docs/model/llm-rate-limits)

临时解决方案：

* 降低请求频率
* 在代码中加入指数退避重试（exponential backoff）
* 联系客服根据充值金额提升 RPM 配额

## 5. 模型响应经常出现超时（Timeout）？

特别是 Gemini 等图像编辑模型，处理时间较长（可能 1-10 分钟）。建议：

* 将超时时间设置为 10 分钟以上
* 使用异步任务模式（如适用）
* 避免在高峰期调用重型任务

***

**联系支持**

如以上 FAQ 无法解决您的问题，请通过以下方式联系技术支持：

* 企业微信/微信技术支持群（推荐，响应最快）
* 提供信息格式：
  * 问题描述 + 截图
  * 账号 ID (UUID)
  * Trace ID（如有，通常在错误信息中）
  * 请求参数（脱敏后）
