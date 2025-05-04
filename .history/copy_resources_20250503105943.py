import os
import shutil
from pathlib import Path

def copy_chrome_resources():
    # 获取Chrome资源文件的路径
    chrome_path = None
    possible_paths = [
        r"C:\Program Files\Google\Chrome\Application",
        r"C:\Program Files (x86)\Google\Chrome\Application",
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            chrome_path = path
            break
    
    if not chrome_path:
        print("未找到Chrome安装目录")
        return False
        
    # 需要复制的文件
    files_to_copy = [
        'chrome_100_percent.pak',
        'chrome_200_percent.pak',
        'resources.pak',
        'd3dcompiler_47.dll',
        'libEGL.dll',
        'libGLESv2.dll',
        'locales',
    ]
    
    # 目标目录
    target_dir = Path('dist/Cursor注册工具_最终版')
    
    # 确保目标目录存在
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # 复制文件
    for file in files_to_copy:
        src = os.path.join(chrome_path, file)
        dst = os.path.join(target_dir, file)
        
        if os.path.exists(src):
            if os.path.isdir(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
                print(f"已复制目录: {file}")
            else:
                shutil.copy2(src, dst)
                print(f"已复制文件: {file}")
        else:
            print(f"未找到文件: {file}")
    
    return True

if __name__ == '__main__':
    if copy_chrome_resources():
        print("Chrome资源文件复制完成！")
    else:
        print("Chrome资源文件复制失败！") 