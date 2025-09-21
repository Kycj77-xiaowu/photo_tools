import os
import re

# 系统常见模块，打包时不需要写入 requirements.txt
IGNORE_MODULES = {
    'sys', 'os', 're', 'csv', 'math', 'time', 'datetime',
    'json', 'tkinter', 'subprocess', 'pathlib', 'shutil'
}

def find_imports(py_file):
    """扫描单个 py 文件的 import 语句"""
    imports = set()
    with open(py_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = re.match(r'^\s*(?:from|import)\s+([a-zA-Z0-9_\.]+)', line)
            if match:
                mod = match.group(1).split('.')[0]
                if mod not in IGNORE_MODULES:
                    imports.add(mod)
    return imports

def get_all_imports():
    """扫描当前文件夹所有 py 文件，返回去重后的第三方模块集合"""
    all_imports = set()
    for file in os.listdir("."):
        if file.endswith(".py") and file != os.path.basename(__file__):
            all_imports.update(find_imports(file))
    return all_imports

def write_requirements(modules, filename="requirements.txt"):
    """写入 requirements.txt"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(modules)))
    print(f"[OK] 已生成 {filename}")

if __name__ == "__main__":
    modules = get_all_imports()

    # Pillow 特殊处理
    if 'PIL' in modules:
        modules.remove('PIL')
        modules.add('pillow')

    if not modules:
        print("[提示] 未检测到第三方库，无需生成 requirements.txt。")
    else:
        write_requirements(modules)