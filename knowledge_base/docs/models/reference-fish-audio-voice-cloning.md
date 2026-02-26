---
title: "Fish Audio 音频复刻"
url: "https://docs.jiekou.ai/docs/models/reference-fish-audio-voice-cloning.md"
crawled_at: "2026-02-26T23:31:59.906926"
---

Published Time: Thu, 26 Feb 2026 15:31:59 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fish Audio 音频复刻

Fish Audio API 用于创建语音模型（声音克隆）。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 密钥}}。 

## 请求体

 模型类型，tts 代表文本转语音。 可选值: `tts` 允许的值: `"tts"` 

 模型标题或名称。 

 模型训练模式，对于 TTS 模型，fast 表示模型在创建后立即可用。 可选值: `fast` 允许的值: `"fast"` 

 上传用于调优模型的语音文件。 

 模型可见性，public 将显示在发现页面，unlist 允许任何拥有链接的人访问，private 仅对创建者可见。 可选值: `public`, `unlist`, `private` 

 模型描述。 

 模型封面图片，如果模型为 public，则此项为必填。 

 与语音对应的文本，如果未指定，将对语音执行 ASR（自动语音识别）。 

 模型标签。 

 增强音频质量。 

## 响应

 已创建模型的唯一标识符。 

 模型类型。 可选值: `svc`, `tts` 

 模型标题或名称。 

 模型描述。 

 模型封面图片的 URL。 

 模型的当前状态。 可选值: `created`, `training`, `trained`, `failed` 

 模型标签。 

 模型创建时的时间戳。 

 模型最后更新时的时间戳。 

 模型可见性设置。 可选值: `public`, `unlist`, `private` 

 模型收到的点赞数。 

 模型收到的收藏/书签数。 

 模型被分享的次数。 

 与模型关联的任务数量。 

 模型作者的信息。   作者的唯一标识符。   作者的昵称。   作者头像图片的 URL。  

 模型使用的训练模式。 可选值: `fast`, `full` 

 与模型关联的样本数据。   样本标题。   样本的文本内容。   样本的任务标识符。   样本音频文件的 URL。  

 模型支持的语言。 

 可见性设置是否被锁定。 

 当前用户是否已取消点赞该模型。 

 当前用户是否已点赞该模型。 

 当前用户是否已收藏/书签该模型。
