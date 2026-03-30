---
name: japan-real-estate-consultant
description: 日本不动产与文旅数据分析师，提供市场简报、播客生成和知识漫画创作服务
---

# 日本不动产与文旅数据分析师技能包

## 核心功能

### 1. 市场咨询简报生成
- 功能：将日本文旅和地产资讯转化为专业简报
- 模板：严格按照【海汇日投·每日快讯】模板生成
- 输出格式：Markdown + 高清图片

### 2. 播客音频生成
- 功能：将简报内容转化为高质量播客音频
- 特点：支持男女双音色对话，码率不低于64kbps
- 输出格式：MP3

### 3. 知识漫画创作
- 功能：将资讯内容转化为四格分镜漫画
- 主角：刀盾狗柴犬形象，手持长剑和樱花盾牌
- 风格：专业商务漫画，视觉一致性强

## 使用流程

### 生成市场简报
```bash
python scripts/generate_briefing.py --input "资讯内容" --output "简报文件.md"
```

### 生成播客音频
```bash
python scripts/generate_podcast.py --input "简报文件.md" --output "播客文件.mp3"
```

### 生成知识漫画
```bash
python scripts/generate_comic.py --input "简报文件.md" --output "漫画文件.jpg"
```

## 技能依赖
- Python 3.8+
- edge-tts
- imgkit
- ffmpeg
- markdown

## 注意事项
- 播客音频码率需不低于64kbps
- 漫画生成需保持视觉一致性
- 所有输出需符合平台上传要求