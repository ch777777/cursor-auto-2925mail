# -*- mode: python ; coding: utf-8 -*-
import os
import platform
from dotenv import load_dotenv

# 加載環境變量獲取版本號
load_dotenv()
version = os.getenv('VERSION', '1.0.0')

# 根据系统类型设置输出名称
system = platform.system().lower()
if system == "windows":
    os_type = "windows"
elif system == "linux":
    os_type = "linux"
else:  # Darwin
    os_type = "mac"

output_name = f"CursorFreeVIP_{version}_{os_type}"

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('locales', 'locales'),
        ('images', 'images'),
        ('config.ini', '.'),
        ('README.md', '.'),
        ('LICENSE.md', '.'),
        ('block_domain.txt', '.'),
        ('requirements.txt', '.'),
        ('.env', '.'),
    ],
    hiddenimports=[
        'faker',
        'colorama',
        'DrissionPage',
        'selenium',
        'selenium.webdriver',
        'selenium.webdriver.chrome.service',
        'selenium.webdriver.common.by',
        'selenium.webdriver.support.ui',
        'selenium.webdriver.support.expected_conditions',
        'selenium.webdriver.chrome.options',
        'selenium.webdriver.common.keys',
        'configparser',
        'json',
        'random',
        'time',
        'os',
        'sys',
        'PIL',
        'PIL.Image',
        'PIL.ImageDraw',
        'PIL.ImageFont',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# 添加额外的二进制文件
a.binaries += [
    ('chrome_100_percent.pak', 'chrome_100_percent.pak', 'DATA'),
    ('chrome_200_percent.pak', 'chrome_200_percent.pak', 'DATA'),
    ('resources.pak', 'resources.pak', 'DATA'),
]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Cursor注册工具_最终版',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='images/logo.png'
)

# 创建收集器
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Cursor注册工具_最终版'
)