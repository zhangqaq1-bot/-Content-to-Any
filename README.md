EasyClaw 技能：多模态内容自动化工作流 (Content-to-Any)
功能简介
本技能包提供了一套完整的自动化内容转化方案，能够将原始资讯深度加工为多种媒介形式，包含三大核心模块：

1. 结构化简报生成 (Text-to-Brief)
将碎片化的原始信息转化为结构清晰、逻辑严密的专业简报。支持自定义 Markdown 模板输出，并可同步生成高清长图，便于多平台分发。

2. 自动化播客创作 (Brief-to-Podcast)
基于简报内容自动构建对话脚本，利用高保真语音合成技术生成专业级播客音频。支持多音色对话模式，输出标准 MP3 格式。

3. 可视化知识漫画 (Brief-to-Comic)
利用 AI 绘图指令集，将核心观点转化为视觉化分镜漫画。支持指定 IP 形象（如柴犬/商务形象），确保品牌视觉的一致性与趣味性。

使用方法
生成结构化简报
Bash
python scripts/generate_briefing.py --input "原始资讯" --output "output/briefing.md"
生成播客音频
Bash
python scripts/generate_podcast.py --input "output/briefing.md" --output "output/podcast.mp3"
生成知识漫画
Bash
python scripts/generate_comic.py --input "output/briefing.md" --output "output/comic.jpg"
技术栈
Python 3.8+

Edge-TTS: 负责高质量语音合成

IMGKit: 负责 Markdown 转图片渲染

FFmpeg: 负责音频后期处理与封装

Markdown: 核心数据中转格式

安装依赖
Bash
pip install -r requirements.txt
维护说明
本项目由 Xiajie AI 开发者社区 驱动，旨在探索 AI Agent 在多模态内容生产中的边界。
