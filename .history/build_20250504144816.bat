@echo off
setlocal enabledelayedexpansion

echo ===================================
echo Cursor Registration Tool Build Script
echo ===================================

:: 检查Python环境
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    exit /b 1
)

:: 检查pip
pip --version >nul 2>&1
if errorlevel 1 (
    echo Error: pip is not installed or not in PATH
    exit /b 1
)

:: 创建并激活虚拟环境
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

:: 升级pip
python -m pip install --upgrade pip

:: 安装依赖
echo Installing dependencies...
pip install -r requirements.txt
pip install pyinstaller

:: 清理旧的构建文件
echo Cleaning old build files...
if exist "build" rd /s /q "build"
if exist "dist" rd /s /q "dist"

:: 运行PyInstaller
echo Building executable...
pyinstaller ^
    --noconfirm ^
    --onefile ^
    --windowed ^
    --icon="images/icon.ico" ^
    --add-data "locales;locales" ^
    --add-data "images;images" ^
    --add-data "email_tabs;email_tabs" ^
    --add-data "scripts;scripts" ^
    --add-data "config.ini;." ^
    --add-data "requirements.txt;." ^
    --add-data "LICENSE.md;." ^
    --add-data "README.md;." ^
    --name "Cursor注册工具_最终版" ^
    main.py

:: 检查构建是否成功
if exist "dist\Cursor注册工具_最终版.exe" (
    echo Build successful!
    echo Executable created at: dist\Cursor注册工具_最终版.exe
) else (
    echo Build failed!
    exit /b 1
)

:: 复制必要的文件到dist目录
echo Copying additional files...
copy "config.ini" "dist\"
copy "requirements.txt" "dist\"
copy "LICENSE.md" "dist\"
copy "README.md" "dist\"

:: 创建发布包
echo Creating release package...
if not exist "release" mkdir "release"
powershell Compress-Archive -Path "dist\*" -DestinationPath "release\Cursor注册工具_v1.11.02.zip" -Force

echo ===================================
echo Build process completed!
echo Release package created at: release\Cursor注册工具_v1.11.02.zip
echo ===================================

:: 清理虚拟环境
deactivate
rd /s /q venv

pause 