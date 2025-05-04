import os
import sys
import subprocess
import traceback
from colorama import Fore, Style, init

# 初始化colorama
init()

# emoji常量
EMOJI = {
    'START': '🚀',
    'ERROR': '❌',
    'INFO': 'ℹ️',
    'SUCCESS': '✅',
}

def check_python_version():
    """检查Python版本"""
    if sys.version_info < (3, 7):
        print(f"{Fore.RED}{EMOJI['ERROR']} 需要Python 3.7或更高版本{Style.RESET_ALL}")
        return False
    return True

def check_dependencies():
    """检查并安装依赖"""
    required_packages = [
        'colorama',
        'DrissionPage',
        'Faker',
    ]
    
    try:
        import pip
        for package in required_packages:
            try:
                __import__(package)
            except ImportError:
                print(f"{Fore.YELLOW}{EMOJI['INFO']} 正在安装 {package}...{Style.RESET_ALL}")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} 安装依赖失败: {str(e)}{Style.RESET_ALL}")
        return False

def main():
    """主函数"""
    try:
        print(f"\n{Fore.CYAN}{EMOJI['START']} 正在初始化环境...{Style.RESET_ALL}")
        
        # 检查Python版本
        if not check_python_version():
            return
        
        # 检查并安装依赖
        if not check_dependencies():
            return
        
        # 运行主程序
        print(f"\n{Fore.GREEN}{EMOJI['SUCCESS']} 环境初始化完成{Style.RESET_ALL}")
        from cursor_register_manual import main
        main()
        
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} 程序运行出错: {str(e)}{Style.RESET_ALL}")
        print(traceback.format_exc())
        input("\n按回车键退出...")
        sys.exit(1)

if __name__ == "__main__":
    main() 