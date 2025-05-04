import os
import shutil
from pathlib import Path

def find_chrome_path():
    possible_paths = [
        r"C:\Program Files\Google\Chrome\Application",
        r"C:\Program Files (x86)\Google\Chrome\Application",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application"),
        os.path.expandvars(r"%PROGRAMFILES%\Google\Chrome\Application"),
        os.path.expandvars(r"%PROGRAMFILES(X86)%\Google\Chrome\Application"),
    ]
    
    # 遍历所有可能的路径
    for base_path in possible_paths:
        if os.path.exists(base_path):
            # 检查是否直接包含所需文件
            if any(os.path.exists(os.path.join(base_path, f)) for f in ['chrome_100_percent.pak']):
                return base_path
            
            # 检查子目录
            for dir_name in os.listdir(base_path):
                full_path = os.path.join(base_path, dir_name)
                if os.path.isdir(full_path) and any(os.path.exists(os.path.join(full_path, f)) for f in ['chrome_100_percent.pak']):
                    return full_path
    
    return None

def copy_chrome_resources():
    # 获取Chrome资源文件的路径
    chrome_path = find_chrome_path()
    
    if not chrome_path:
        print("未找到Chrome安装目录")
        return False
    
    print(f"找到Chrome目录: {chrome_path}")
    
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
    success_count = 0
    for file in files_to_copy:
        src = os.path.join(chrome_path, file)
        dst = os.path.join(target_dir, file)
        
        try:
            if os.path.exists(src):
                if os.path.isdir(src):
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                    print(f"已复制目录: {file}")
                    success_count += 1
                else:
                    shutil.copy2(src, dst)
                    print(f"已复制文件: {file}")
                    success_count += 1
            else:
                print(f"未找到文件: {file}")
        except Exception as e:
            print(f"复制 {file} 时出错: {str(e)}")
    
    return success_count > 0

if __name__ == '__main__':
    if copy_chrome_resources():
        print("Chrome资源文件复制完成！")
    else:
        print("Chrome资源文件复制失败！") 