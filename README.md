# EasyClaw技能：日本不动产与文旅数据分析师

## 功能简介

日本不动产与文旅数据分析师技能包，为海汇日投智库提供专业的市场分析服务，包含三大核心功能：

### 1. 市场咨询简报生成
将日本文旅和地产资讯转化为符合【海汇日投·每日快讯】模板的专业简报，支持Markdown格式输出和高清图片生成。

### 2. 播客音频生成
将简报内容转化为高质量播客音频，支持男女双音色对话模式，输出MP3格式，码率不低于64kbps。

### 3. 知识漫画创作
将资讯内容转化为四格分镜漫画，采用刀盾狗柴犬IP形象，保持专业商务风格和视觉一致性。

## 使用方法

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

## 技术栈
- Python 3.8+
- edge-tts (音频生成)
- imgkit (图片生成)
- ffmpeg (音频处理)
- markdown (格式处理)

## 安装依赖
```bash
pip install -r requirements.txt
```

## 版权声明
本技能包为海汇日投智库专属，仅限内部使用和授权分享。