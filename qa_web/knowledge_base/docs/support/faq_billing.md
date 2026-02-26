---
title: "充值与计费"
url: "https://docs.jiekou.ai/docs/support/faq_billing.md"
crawled_at: "2026-02-26T23:37:01.953498"
---

Published Time: Thu, 26 Feb 2026 07:40:41 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 充值与计费

## 1. 充值后余额未实时到账怎么办？

正常情况下充值是随充随到账。如遇到账延迟，请提供以下信息联系客服：

* 账号 ID (UUID)
* 充值订单号 (product\_xxx)
* 支付截图

注：系统偶尔会出现延迟，一般会在排查后手动到账。如确认是系统问题，平台通常会发放代金券作为补偿。

## 2. 充值比例是多少？人民币如何充值？

充值按照美元计算，您可以通过支付宝直接充值，点击充值页面即可看到实时汇率。

## 3. 如何避免充值失败？

充值失败通常由两个主要原因引起：

* 发卡行拒绝。 可能由于以下原因导致，请检查或联系您的发卡行了解详情：
  * 相应的支付通道未激活。
  * 信用卡已过期或被冻结。
  * 信用卡余额不足。
  * 卡号不正确。
  * 安全码不正确。
* 支付通道的风控措施。 请检查并进行必要的调整：
  * 设备 ID 关联的卡片数量过多。
  * 使用此电子邮件地址拒绝的卡片数量非常高。
  * 此卡在 Stripe 网络中与此设备 ID 首次出现的时间非常短。
  * 与此电子邮件地址关联的授权率非常低。
  * 电子邮件地址上的姓名与卡上的姓名不匹配。

## 4. 价格是如何计算的？

不同模型/能力按不同计费方式收取：

* 大语言模型 / Embedding / Reranker： 按 token 计费，包含 input / output / cache write / cache read 等维度。
* 图片 / 视频 / 音频： 按调用次数收费。

## 5. 如何查看详细的账单和用量？

* 账单总览：[https://jiekou.ai/billing/transactions](https://jiekou.ai/billing/transactions)
* 详细用量：[https://jiekou.ai/billing/details](https://jiekou.ai/billing/details) （可查看各模型的 Token 用量明细）
* 价格表：[https://jiekou.ai/pricing](https://jiekou.ai/pricing)

## 6. 为什么调用量很少却被扣了大量费用？

请检查以下情况：

* 模型选择：Claude Opus 4.5 等高端模型消耗较快（输入 11W token 可能就需 0.45 美金以上）
* Token 计算：Gemini 等模型的图片输入按分辨率计算 Token，高分辨率图片可能产生大量 Token
* 缓存计费：部分模型（如 Claude）的 Prompt Caching 如未命中，会以"缓存输入"价格计费，可能比普通输入更贵

## 7. 为什么代金券/余额还有，却提示余额不足(403)？

可能原因包括：

* 账户确实费用不足（现金+代金券总和不足）
* 系统计费延迟显示（实际已扣完）
* 超过单分钟 RPM/TPM 限制被限流（错误提示可能显示为余额不足）

## 8. 免费模型为什么也在扣费？

请确认是否在使用过程中切换过模型。如果在付费模型会话中切换至免费模型，可能因上下文 tokens 计算产生费用。建议检查账单详情中的模型调用记录。

## 9. 支持退款吗？如何申请？

一般情况下，已使用的余额不支持退款。如确需退款（如平台无法满足业务需求），请提供：

* 账号 ID (UUID)
* 注册邮箱
* 退款原因

注：通过第三方工具（如 Cursor）使用遇到兼容性问题通常不支持退款，建议先使用小额充值测试。

## 10. 退款是原路返回吗？

是的，退款会原路退回至原支付账户。如为公司充值，需与财务确认原支付渠道。

***

**联系支持**

如以上 FAQ 无法解决您的问题，请通过以下方式联系技术支持：

* 企业微信/微信技术支持群（推荐，响应最快）
* 提供信息格式：
  * 问题描述 + 截图
  * 账号 ID (UUID)
  * Trace ID（如有，通常在错误信息中）
  * 请求参数（脱敏后）
