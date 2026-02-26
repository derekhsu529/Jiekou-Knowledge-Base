---
title: "API 鉴权方式"
url: "https://docs.jiekou.ai/docs/models/reference-authentication.md"
crawled_at: "2026-02-26T23:16:57.984827"
---

Published Time: Thu, 26 Feb 2026 11:10:59 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# API 鉴权方式

JieKou AI API 使用 `请求头` 中的 Authorization 字段携带 API 密钥进行身份认证。您可以在 [设置页面](https://jiekou.ai/settings/key-management) 查看和管理您的 API 密钥。

```js  theme={null}
{
    "Authorization": "Bearer {{API Key}}"
}
```
