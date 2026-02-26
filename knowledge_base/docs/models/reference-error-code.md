---
title: "API 错误码说明"
url: "https://docs.jiekou.ai/docs/models/reference-error-code.md"
crawled_at: "2026-02-26T23:41:34.280152"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# API 错误码说明

<table class="table table-big">
  <thead>
    <tr>
      <th>错误名称</th>
      <th>状态码</th>
      <th>说明</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>INVALID\_API\_KEY</td>
      <td>403</td>
      <td>未提供 API Key</td>
    </tr>

    <tr>
      <td>MODEL\_NOT\_FOUND</td>
      <td>404</td>
      <td>模型不存在</td>
    </tr>

    <tr>
      <td>FAILED\_TO\_AUTH</td>
      <td>401</td>
      <td>认证失败</td>
    </tr>

    <tr>
      <td>NOT\_ENOUGH\_BALANCE</td>
      <td>403</td>
      <td>余额不足</td>
    </tr>

    <tr>
      <td>INVALID\_REQUEST\_BODY</td>
      <td>400</td>
      <td>请求体格式错误，详见 message</td>
    </tr>

    <tr>
      <td>RATE\_LIMIT\_EXCEEDED</td>
      <td>429</td>
      <td>请求过快，请稍后重试</td>
    </tr>

    <tr>
      <td>TOKEN\_LIMIT\_EXCEEDED</td>
      <td>429</td>
      <td>Token 数超限，请稍后重试</td>
    </tr>

    <tr>
      <td>SERVICE\_NOT\_AVAILABLE</td>
      <td>503</td>
      <td>服务不可用</td>
    </tr>

    <tr>
      <td>ACCESS\_DENY</td>
      <td>403</td>
      <td>无权限访问</td>
    </tr>
  </tbody>
</table>
