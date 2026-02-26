---
title: "查询账单"
url: "https://docs.jiekou.ai/docs/models/reference-get-bill-pay-as-you-model.md"
crawled_at: "2026-02-26T23:32:21.897848"
---

Published Time: Thu, 26 Feb 2026 15:32:21 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 查询账单

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 响应

 计费周期粒度。选项： * `Hour`：按小时 * `Day`: 按天 * `Week`：按周 * `Month`：按月 

 产品类型。选项： * `summary`：汇总账单 * `llm`： 大语言模型 

 产品名称。支持模糊匹配。 

 查询账单周期的开始时间，时间戳（秒），默认值：0。 

 查询账单周期的结束时间，时间戳（秒），默认值：0。 

 指定要查询的实例 ID。 

## 响应参数

 按需实例计费信息。   实例所属的用户 ID。   账单的开始时间。格式为 Unix 时间戳。   账单的结束时间。格式为 Unix 时间戳。   实例的计费方式。值为 1 表示按需计费。   产品名称。   产品类别。   实例 ID。   * llm：输入 tokens   * llm：输出 tokens   原价   无意义   * llm：输入 tokens 单价 * 其他：单价   * llm：输出 tokens 单价   总价。   代金券扣除金额。   现金支付金额。    价格精度。   产品 ID。
