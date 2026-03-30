#!/usr/bin/env python3
"""
创建GitHub仓库并推送代码
需要提供GitHub个人访问令牌
"""

import os
import sys
import subprocess
from github import Github

def create_github_repo(token, repo_name, description="", private=False):
    """创建GitHub仓库"""
    try:
        from github import Auth
        auth = Auth.Token(token)
        g = Github(auth=auth)
        user = g.get_user()
        repo = user.create_repo(
            name=repo_name,
            description=description,
            private=private,
            auto_init=False
        )
        print(f"✅ 成功创建GitHub仓库: {repo.html_url}")
        return repo.html_url, repo.clone_url
    except Exception as e:
        print(f"❌ 创建仓库失败: {str(e)}")
        return None, None

def push_to_github(repo_path, clone_url, token):
    """推送代码到GitHub"""
    try:
        git_executable = "C:\\Program Files\\Git\\bin\\git.exe"
        
        # 替换URL为包含令牌的版本
        auth_url = clone_url.replace("https://", f"https://{token}@")
        
        # 执行Git命令
        subprocess.run([git_executable, "remote", "set-url", "origin", auth_url], cwd=repo_path, check=True)
        subprocess.run([git_executable, "add", "README.md"], cwd=repo_path, check=True)
        subprocess.run([git_executable, "commit", "-m", "docs: 添加README.md文档"], cwd=repo_path, check=True)
        subprocess.run([git_executable, "push", "-u", "origin", "main"], cwd=repo_path, check=True)
        
        print("✅ 代码推送成功!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 推送代码失败: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ 推送代码失败: {str(e)}")
        return False

def main():
    # 配置信息
    REPO_NAME = "easyclaw-skill-japan-real-estate-consultant"
    REPO_DESCRIPTION = "EasyClaw技能：日本不动产与文旅数据分析师，提供市场简报、播客生成和知识漫画创作服务"
    REPO_PATH = os.path.dirname(os.path.abspath(__file__))
    
    print("🎯 开始创建GitHub仓库...")
    print(f"📦 技能路径: {REPO_PATH}")
    print(f"📝 仓库名称: {REPO_NAME}")
    
    # 获取GitHub令牌
    token = input("请输入GitHub个人访问令牌: ").strip()
    if not token:
        print("❌ 令牌不能为空")
        sys.exit(1)
    
    # 创建仓库
    repo_url, clone_url = create_github_repo(token, REPO_NAME, REPO_DESCRIPTION, private=False)
    if not repo_url:
        sys.exit(1)
    
    # 推送代码
    if push_to_github(REPO_PATH, clone_url, token):
        print(f"\n🎉 发布完成!")
        print(f"🔗 仓库地址: {repo_url}")
        print(f"📖 可以分享这个链接到Datawhale社区啦!")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()