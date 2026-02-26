---
title: "调用频率控制（Rate Limits）"
url: "https://docs.jiekou.ai/docs/model/llm-rate-limits.md"
crawled_at: "2026-02-26T23:31:27.807807"
---

Published Time: Thu, 26 Feb 2026 15:31:27 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 调用频率控制（Rate Limits）

export const DynamicRPMList = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    let attempts = 0;
    const maxAttempts = 50;
    const formatAmount = num => {
      if (typeof num === "number") {
        return num.toLocaleString();
      }
      return num || "-";
    };
    const interval = setInterval(() => {
      const clientComponent = document.getElementById("dynamic-rpm-list");
      if (clientComponent && window.jiekouRemoteData.llmModels.status === 'loaded') {
        const modelList = window.jiekouRemoteData.llmModels.data.filter(model => {
          return Boolean(model.rpm);
        });
        const allModels = modelList.map(model => {
          const t1 = (model.quota_items || []).find(item => item.tier === "T1") || ({});
          const t2 = (model.quota_items || []).find(item => item.tier === "T2") || ({});
          const t3 = (model.quota_items || []).find(item => item.tier === "T3") || ({});
          const t4 = (model.quota_items || []).find(item => item.tier === "T4") || ({});
          const t5 = (model.quota_items || []).find(item => item.tier === "T5") || ({});
          return `
             ${model.id} RPM ${formatAmount(t1.rpm)} ${formatAmount(t2.rpm)} ${formatAmount(t3.rpm)} ${formatAmount(t4.rpm)} ${formatAmount(t5.rpm)} 

             TPM ${formatAmount(t1.tpm)} ${formatAmount(t2.tpm)} ${formatAmount(t3.tpm)} ${formatAmount(t4.tpm)} ${formatAmount(t5.tpm)} 

          `;
        }).join('');
        clientComponent.innerHTML = `
          
  | 模型 |  | T1 | T2 | T3 | T4 | T5 |
| --- | --- | --- | --- | --- | --- | --- |
   ${allModels}  

        `;
        clearInterval(interval);
      }
      attempts++;
      if (attempts >= maxAttempts) {
        clearInterval(interval);
      }
    }, 200);
    return ;
  }
};

## 理解调用频率控制

调用频率控制规定了在特定时间内可发起的 API 请求的数量，可以帮助优化 API 使用。

* 防止 API 滥用和误用
* 确保公平的资源分配
* 保持 API 性能和可靠性
* 保护服务的稳定性

## 默认调用频率控制

每个账户在调用模型时都有默认的速率限制，分别以 RPM（每分钟每个模型的请求数）和 TPM（每分钟每个模型的 token 数）为单位进行衡量。速率限制会因账户等级不同而有所差异，具体标准见下方表格。

  | Quota 等级 | 资质（单位：美元） |
| --- | --- |
   | T1 | 最近 3 个自然月中，单月最高充值总金额\< \$50 |
 | T2 | \$50 ≤ 最近 3 个自然月中，单月最高充值总金额\< \$500 |
 | T3 | \$500 ≤ 最近 3 个自然月中，单月最高充值总金额\< \$3000 |
 | T4 | \$3000 ≤ 最近 3 个自然月中，单月最高充值总金额\< \$10000 |
 | T5 | \$10000 ≤ 最近 3 个自然月中，单月最高充值总金额 |
 

各等级的默认速率限制（RPM / TPM）：

 ## 避免触发调用频率控制 如果您的 API 请求数量超过了调用频率控制，API 将返回： * HTTP 状态码：429（请求过多）。 * 响应体中返回调用频率超出的信息。 为避免触发调用频率控制，您可以采取以下措施： * 在您的应用中实现请求限制。 * 在重试时使用指数退避机制。 * 监控您的 API 使用情况。 ## 处理 429 错误 如果您收到 429 错误，您可以尝试以下操作： * **稍后再试**：等待一段时间后再重试您的请求。 * **优化请求**：减少请求频率。 * **提高调用频率控制**：如果需要更高的调用频率控制，可以联系我们。
