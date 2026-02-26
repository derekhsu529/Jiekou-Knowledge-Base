---
title: "Midjourney 区域重绘"
url: "https://docs.jiekou.ai/docs/models/reference-mj-inpaint.md"
crawled_at: "2026-02-26T23:34:22.199593"
---

Published Time: Thu, 26 Feb 2026 15:34:22 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Midjourney 区域重绘

使用 Midjourney 区域重绘功能，对已生成图像的指定区域进行重新绘制。支持通过多边形区域或黑白蒙版图片指定重绘区域，该接口采用异步处理方式，客户端需要通过 task\_id 查询最终生成结果。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 图片编号，用于指定要进行区域重绘的图片。 取值范围：0\~3 

 原始图像生成任务的唯一标识符。 

 重绘区域提示词，用于描述重绘区域的期望内容。 长度限制：1-8192 个字符。 

 绘制区域配置，替代 area 参数，支持多区域重绘。areas 和 url 二选一。   以黑白二值图片指定多边形区域，支持指定多个区域，白色区域为重绘区域。   多边形区域数组，支持指定多个区域。   多边形区域坐标点数组，以左上为原点，按顺时针方向、以 XYXY 的方式组织。   图片像素宽度。 取值范围：500\~4096   图片像素高度。 取值范围：500\~4096    

 单个多边形区域配置（与 mask 参数二选一使用）。   多边形区域坐标点数组，以左上为原点，按顺时针方向、以 XYXY 的方式组织。   图片像素宽度。 取值范围：500\~4096   图片像素高度。 取值范围：500\~4096  

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
