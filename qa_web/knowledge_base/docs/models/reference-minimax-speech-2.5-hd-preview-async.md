---
title: "MiniMax Speech-2.5-hd-preview 异步语音合成"
url: "https://docs.jiekou.ai/docs/models/reference-minimax-speech-2.5-hd-preview-async.md"
crawled_at: "2026-02-26T23:38:15.770703"
---

Published Time: Thu, 26 Feb 2026 15:38:15 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Speech-2.5-hd-preview 异步语音合成

该 API 支持基于文本到语音的异步生成，单次文本生成传输最大支持 100 万字符，生成的完整音频结果支持异步的方式进行检索。支持 100+系统音色、复刻音色自主选择；支持语调、语速、音量、比特率、采样率、输出格式自主调整。

提交长文本语音合成请求后，需要注意的是返回的 url 的有效期为自 url 返回开始的 24 个小时，请注意下载信息的时间。

适用于整本书籍等长文本的语音生成，任务排队耗时可能会较长。短句生成、语音聊天、在线社交等场景，建议使用 [同步调用语音合成](/docs/models/reference-minimax-speech-2.5-hd-preview)。

## 请求头

 枚举值: `application/json` 

 Bearer 身份验证格式: Bearer \{\{API 秘钥}}。 

## 请求体

 待合成的文本，限制最长 5 万字符。 

   范围\[0.5,2]，默认值为 1.0 生成声音的语速，可选，取值越大，语速越快。   范围（0,10]，默认值为 1.0 生成声音的音量，可选，取值越大，音量越高。   范围\[-12,12]，默认值为 0 生成声音的语调，可选，（0 为原音色输出，取值需为整数）。   请求的音色编号。 支持系统音色(id)以及复刻音色（id）两种类型，其中系统音色（ID）如下： * 青涩青年音色：`male-qn-qingse` * 精英青年音色：`male-qn-jingying` * 霸道青年音色：`male-qn-badao` * 青年大学生音色：`male-qn-daxuesheng` * 少女音色：`female-shaonv` * 御姐音色：`female-yujie` * 成熟女性音色：`female-chengshu` * 甜美女性音色：`female-tianmei` * 男性主持人：`presenter_male` * 女性主持人：`presenter_female` * 男性有声书 1：`audiobook_male_1` * 男性有声书 2：`audiobook_male_2` * 女性有声书 1：`audiobook_female_1` * 女性有声书 2：`audiobook_female_2` * 青涩青年音色-beta：`male-qn-qingse-jingpin` * 精英青年音色-beta：`male-qn-jingying-jingpin` * 霸道青年音色-beta：`male-qn-badao-jingpin` * 青年大学生音色-beta：`male-qn-daxuesheng-jingpin` * 少女音色-beta：`female-shaonv-jingpin` * 御姐音色-beta：`female-yujie-jingpin` * 成熟女性音色-beta：`female-chengshu-jingpin` * 甜美女性音色-beta：`female-tianmei-jingpin` * 聪明男童：`clever_boy` * 可爱男童：`cute_boy` * 萌萌女童：`lovely_girl` * 卡通猪小琪：`cartoon_pig` * 病娇弟弟：`bingjiao_didi` * 俊朗男友：`junlang_nanyou` * 纯真学弟：`chunzhen_xuedi` * 冷淡学长：`lengdan_xiongzhang` * 霸道少爷：`badao_shaoye` * 甜心小玲：`tianxin_xiaoling` * 俏皮萌妹：`qiaopi_mengmei` * 妩媚御姐：`wumei_yujie` * 嗲嗲学妹：`diadia_xuemei` * 淡雅学姐：`danya_xuejie` * Santa Claus：`Santa_Claus` * Grinch：`Grinch` * Rudolph：`Rudolph` * Arnold：`Arnold` * Charming Santa：`Charming_Santa` * Charming Lady：`Charming_Lady` * Sweet Girl：`Sweet_Girl` * Cute Elf：`Cute_Elf` * Attractive Girl：`Attractive_Girl` * Serene Woman：`Serene_Woman`   控制合成语音的情绪； 当前支持 7 种情绪：高兴，悲伤，愤怒，害怕，厌恶，惊讶，中性； 参数范围：`["happy", "sad", "angry", "fearful", "disgusted", "surprised", "neutral"]`   该参数支持英语文本规范化，可提升数字阅读场景的性能，但会略微增加延迟。如果未提供，则默认值为 false。  

   范围【8000，16000，22050，24000，32000，44100】 生成声音的采样率。可选，默认为 32000。   范围【32000，64000，128000，256000】 生成声音的比特率。可选，默认值为 128000。该参数仅对 mp3 格式的音频生效。   生成的音频格式。默认 mp3。可选：`mp3`, `pcm`, `flac`, `wav`。wav 仅在非流式输出下支持。   生成音频的声道数.默认 1：单声道，可选： 1：单声道 2：双声道  

   替换需要特殊标注的文字、符号及对应的注音。 替换发音（调整声调/替换其他字符发音），格式如下： `["燕少飞/(yan4)(shao3)(fei1)","达菲/(da2)(fei1)"，"omg/oh my god"]` 声调用数字代替，一声（阴平）为 1，二声（阳平）为 2，三声（上声）为 3，四声（去声）为 4），轻声为 5。  

 增强对指定的小语种和方言的识别能力，设置后可以提升在指定小语种/方言场景下的语音表现。如果不明确小语种类型，则可以选择"auto"，模型将自主判断小语种类型。支持以下取值： `'Chinese', 'Chinese,Yue', 'English', 'Arabic', 'Russian', 'Spanish', 'French', 'Portuguese', 'German', 'Turkish', 'Dutch', 'Ukrainian', 'Vietnamese', 'Indonesian', 'Japanese', 'Italian', 'Korean', 'Thai', 'Polish', 'Romanian', 'Greek', 'Czech', 'Finnish', 'Hindi', 'Bulgarian', 'Danish', 'Hebrew', 'Malay', 'Persian', 'Slovak', 'Swedish', 'Croatian', 'Filipino', 'Hungarian', 'Norwegian', 'Slovenian', 'Catalan', 'Nynorsk', 'Tamil', 'Afrikaans', 'auto'` 

 声音效果器设置，该参数支持的音频格式：mp3, wav, flac   音高调整（低沉/明亮），范围 \[-100,100]，数值接近 -100，声音更低沉；接近 100，声音更明亮   强度调整（力量感/柔和），范围 \[-100,100]，数值接近 -100，声音更刚劲；接近 100，声音更轻柔   音色调整（磁性/清脆），范围 \[-100,100]，数值接近 -100，声音更浑厚；数值接近 100，声音更清脆   音效设置，单次仅能选择一种，可选值： * `spacious_echo`（空旷回音） * `auditorium_echo`（礼堂广播） * `lofi_telephone`（电话失真） * `robotic`（电音）  

## 响应参数

 异步任务的 task\_id。您应该使用该 task\_id 请求 [查询任务结果 API](/docs/models/reference-get-async-task-result) 以获取生成结果
