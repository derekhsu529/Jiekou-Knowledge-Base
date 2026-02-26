---
title: "GLM 图像生成"
url: "https://docs.jiekou.ai/docs/models/reference-glm-image.md"
crawled_at: "2026-02-26T23:32:25.882973"
---

Published Time: Thu, 26 Feb 2026 15:32:25 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM 图像生成

这是一个异步 API，仅返回异步任务的 `task_id`。

 这是一个**异步**API，只会返回异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成结果。 

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 图片尺寸。推荐值：1280x1280（默认）、1568x1056、1056x1568、1472x1088、1088x1472、1728x960、960x1728。自定义尺寸：宽高应在 1024-2048px 范围内，最大总像素数 4194304，宽高均需为 32 的整数倍。 

 所需图像的文本描述。描述您希望在生成图像中呈现的场景、主体、风格和细节。 

 图像质量。HD 模式生成更精细、细节更丰富的图像，整体一致性更高。 可选值：`hd` 

 控制 AI 生成图片时是否添加水印。true：启用水印（默认，符合政策要求）。false：关闭水印。 

## 响应

 使用 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 来检索生成的输出。
