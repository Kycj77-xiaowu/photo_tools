 照片重命名与分类工具

一个基于 Python + Tkinter 的桌面工具，用于顺序处理照片、重命名并自动分类到调查点文件夹，可完全用键盘操作，适合快速整理现场拍摄的照片。

 ✨ 功能特性
 **顺序处理**：一次选择一个文件夹，按顺序查看和处理照片  
 **智能命名**：支持自定义命名规则（如 `D001 - 1`），自动分类到对应文件夹  
 **键盘快捷操作**：
   `↑ / ↓`：在输入框之间切换
   `← / →`：切换上一张 / 下一张照片
   `Enter`：保存并进入下一张
 **字段保留逻辑**：跳到下一张时保留第 1、3 输入框内容，清空第 2、4 个输入框
 **镜像和角度**可选，不填不会阻塞

 📦 安装方法
1. 克隆项目：
   ```bash
   git clone https://github.com/<你的用户名>/photo_tools.git
   cd photo_tools

2.创建虚拟环境并安装依赖：
  python -m venv venv
  venv\Scripts\activate  # Windows
  pip install -r requirements.txt

3.运行方法 
  python photo_tool.py

4.🛠 打包为 exe（可选）
本工具支持使用 pyinstaller 打包为 Windows 可执行文件：
pyinstaller --noconsole --onefile --icon=icon.ico photo_tool.py

📜 License
本项目仅供个人使用，禁止商用。

