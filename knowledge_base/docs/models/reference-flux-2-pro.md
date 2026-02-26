---
title: "Flux 2 Pro 生图"
url: "https://docs.jiekou.ai/docs/models/reference-flux-2-pro.md"
crawled_at: "2026-02-26T23:32:08.025536"
---

Published Time: Thu, 26 Feb 2026 15:32:07 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux 2 Pro 生图

这是一个异步 API，仅返回异步 task\_id。你需要使用 task\_id 调用任务结果查询 API 获取图像编辑结果。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 用于生成的随机种子。-1 表示使用随机种子。范围：-1 到 2147483647 取值范围：\[-1, 2147483647] 

 输出媒介的像素尺寸（宽\*高），每个维度范围为 256 到 1536 像素 

 编辑待处理图像的输入图像 URL 列表，最多可支持 3 张 数组长度：1 - 3 

 描述图片期望编辑效果的文本提示 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
