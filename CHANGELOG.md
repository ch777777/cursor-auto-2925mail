# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.11.02] - 2024-05-04 (Original Author: @chengazhen)

1. Fill: Missing Translations（ar, zh-cn, zh-tw, vi, nl, de, fr, pt, ru, tr, bg, es, ja, it） | 填補缺失的翻譯
2. Add: Japanese and Italian language support
3. Refactor: Account Generation with Faker and Update requirements.txt
4. Add: script to auto-translate missing keys in translation files | 增加 fill_missing_translations.py 自動翻譯缺失的翻譯鍵
5. Add: TempMailPlus Support, support temp email verification | 新增 TempMailPlus 配置，支持临时邮箱验证功能
6. Fix: Chrome user data directory permission problem on mac | 修復 Chrome 用戶數據目錄權限問題 on mac
7. Fix: Some Issues | 修復一些問題

## [1.2.0] - 2024-05-04 (Author: @ch777777)

### ✨ Core Features | 核心特性

#### 🔑 Account Management | 账号管理
- Added 2925.com email auto-registration support | 支持2925.com邮箱自动注册
- Intelligent verification code recognition and processing | 智能验证码识别和处理
- Batch account management system | 批量账号管理系统
- Automated account information submission | 自动化账号信息提交

#### 🔄 Permission Management | 权限管理
- Automatic permission update cycle | 自动循环更新使用权限
- Intelligent permission status monitoring | 智能化权限状态监控
- Multi-account rotation mechanism | 多账号轮换机制
- Expiration warning and automatic processing | 失效预警和自动处理

### Added | 新增
- 2925.com email integration and automation | 2925.com邮箱集成和自动化
- Complete account management functionality | 完整的账号管理功能
- Automated permission update system | 自动化权限更新系统
- Multi-language interface support | 多语言界面支持

## [1.11.01] - 2024-05-03

0. Must Update to this version to get full experience | 必須更新到此版本以獲取完整體驗
1. Restore: Some Main Code | 恢復一些主程式碼
2. Add: Arabic language | 增加阿拉伯語
3. Add: Language configuration saved setting | 增加語言配置保存設定
4. Add: Restore Machine ID from Backup | 增加從備份恢復機器ID
5. Add: Owned Website Check Version | 增加擁有網站檢查版本
6. Fix: use cursor_path from config_file | 修復使用 cursor_path 從 config_file
7. Fix: macOS 'bypass_version.py' get product_json_path from config_file | 修復 macOS 'bypass_version.py' 從 config_file 獲取 product_json_path
8. Fix: Some Issues | 修復一些問題

## [1.10.05] - 2024-05-02

1. Remove block_domain.txt | 移除 block_domain.txt
2. Original Code In Github , If u afraid of virus, please clone the code and run locally | 原始碼在 Github 上，如果怕病毒，請複製原始碼並在本機運行
3. All Action using github workflow , not build myself , so i cant place virus in the file | 所有 Action 使用 github workflow ，不是我自己 build 的，所以我不會在文件中放置病毒
4. Fix: Some Issues | 修復一些問題

## [1.10.04] - 2024-05-02

1. Hotfix: Reset Process Error: cannot access local variable 'main_path' where it is not associated with a value on windows & macos | 修復在 Windows 和 macOS 上無法訪問局部變量 'main_path' 的問題
2. Fix: Some Issues | 修復一些問題

## [1.10.03] - 2024-05-01

1. Add: Manual Registration | 增加手動註冊
2. Only support your own Email | 只支持自己的Email 請勿使用Temp Email 註冊 註冊假賬號
3. Fix: macOS 'bypass_version.py' get product_json_path from config_file | 修復 macOS 'bypass_version.py' 從 config_file 獲取 product_json_path
4. Fix: use cursor_path from config_file | 修復使用 cursor_path 從 config_file
5. Fix: Some Issues | 修復一些問題

## [1.10.02] - 2024-05-01

1. Remove: Remove All Auto generating fake Google email accounts and OAuth access | 移除所有自動生成假 Google 電子郵件帳戶和 OAuth 訪問
2. Follow GitHub Terms of Service | 遵守 GitHub Terms of Service
3. Follow Cursor Terms of Service | 遵守 Cursor Terms of Service
4. All are for educational purposes, currently the repo does not violate any laws | 全都是教育用途，目前 repo 沒有違反任何法律
5. This project adopts CC BY-NC-ND 4.0 , do not use for commercial purposes | 本專案採用 CC BY-NC-ND 4.0，拒絕任何商業用途
6. Use & Cherish | 切用且珍惜
7. Same as v1.10.01 | 與 v1.10.01 相同 
8. Fix: reset machine ID no module name 'new_signup' | 修復機器 ID 重置 no module name 'new_signup'
9. Fix: Some Issues | 修復一些問題

## [1.10.01] - 2024-04-30

1. Remove: Remove All Auto generating fake Google email accounts and OAuth access | 移除所有自動生成假 Google 電子郵件帳戶和 OAuth 訪問
2. Follow GitHub Terms of Service | 遵守 GitHub Terms of Service
3. Follow Cursor Terms of Service | 遵守 Cursor Terms of Service
4. All are for educational purposes, currently the repo does not violate any laws | 全都是教育用途，目前 repo 沒有違反任何法律
5. This project adopts CC BY-NC-ND 4.0 , do not use for commercial purposes | 本專案採用 CC BY-NC-ND 4.0，拒絕任何商業用途
6. Use & Cherish | 切用且珍惜
7. Fix: Some Issues | 修復一些問題

## [1.9.05] - 2024-04-29

1. Refactor: Using match-case to refactor language mapping and menu selection logic, making the code clearer and more maintainable. | 使用 match-case 重构语言映射和菜单选择逻辑，使代码更清晰、可维护性更高。
2. Ci: Update the Python version in the ARM64 Docker build container to 3.10, making it more compatible and easier to migrate in the future. | 更新 ARM64 Docker 构建容器中的 Python 版本至 3.10，兼容性更强，方便未来迁移。
3. Fix: f-string backslash expression errors in multiple files | 修復多個文件中的 f-string 反斜杠表達式錯誤
4. Sync AUR new version 1.9.04 | 同步 AUR 新版本 1.9.04
5. Fix: missing license install on pkgbuild @michaeldavis246611119 mention here | 修復 pkgbuild 中缺少授權安裝 @michaeldavis246611119 提到這裡
6. Fix: readme table | 修復 readme 表格
7. Fix: google-chrome package name problem, add "google-chrome-stable" | 修復 google-chrome 包名稱問題，添加 "google-chrome-stable"
8. Fix: exception error log | 修復異常錯誤日誌
9. Fix: github oauth error [Bug]: #564 | 修復 github oauth 錯誤 [Bug]: #564
10. Fix: ChromiumOptions.arguments type error: list object has no attribute 'get' | 修復 ChromiumOptions.arguments 類型錯誤：list 對象沒有屬性 'get'
11. Fix: Some Issues | 修復一些問題

## [1.9.04] - 2024-04-28

1. Add: Opera GX Support | 添加 Opera GX 支持
2. Same as v1.9.03 | 與 v1.9.03 相同
3. Hotfix: Some Issues | 修復一些問題
4. Add: Bypass Cursor JWT EXP Problem | 添加繞過 Cursor JWT EXP 問題
5. Fix: Cursor editor redirects to logout page and logout automatically | 修復 Cursor 編輯器重定向到登出頁面並自動登出
6. Fix: Some Issues | 修復一些問題

## [1.9.03] - 2024-04-28 [Skip & Merge to v1.9.04]

1. Hotfix: Some Issues | 修復一些問題
2. Add: Bypass Cursor JWT EXP Problem | 添加繞過 Cursor JWT EXP 問題
3. Fix: Cursor editor redirects to logout page and logout automatically | 修復 Cursor 編輯器重定向到登出頁面並自動登出
4. Fix: Some Issues | 修復一些問題

## [1.9.02] - 2024-04-27

1. Add: Bypass Token Limit | 添加繞過 Token 限制
2. Add: More Browser Support | 添加更多瀏覽器支持
3. Add: Bypass Cursor JWT EXP Problem | 添加繞過 Cursor JWT EXP 問題
4. Support: Add Opera, Brave, Edge, Firefox | 添加支持 Opera, Brave, Edge, Firefox
5. Add config manual browser path | 添加配置手動選擇遊覽器路徑
6. Fix: Browser Profile Selection | 修復瀏覽器配置文件選擇
7. Fix: Cursor editor redirects to logout page and logout automatically | 修復 Cursor 編輯器重定向到登出頁面並自動登出
8. Fix: Config File Path | 修復配置文件路徑
9. Fix: window user permission | 修復 window 用戶權限
10. Fix: Some Issues | 修復一些問題

## [1.9.01] - 2024-04-26

1. Add: Bypass Token Limit | 添加繞過 Token 限制
2. Add: More Browser Support | 添加更多瀏覽器支持
3. Support: Add Opera, Brave, Edge, Firefox | 添加支持 Opera, Brave, Edge, Firefox
4. Add config manual browser path | 添加配置手動選擇遊覽器路徑
5. Fix: Browser Profile Selection | 修復瀏覽器配置文件選擇
6. Fix: Some Issues | 修復一些問題

## [1.8.10] - 2024-04-25

1. Add: Check User Authorized | 添加檢查用戶授權
2. Fix: Linux Reset Process Error: 'base' | 修復 Linux 重置過程錯誤：'base'
3. Updated the get_workbench_cursor_path function to handle Linux systems more effectively. | 更新 get_workbench_cursor_path 函數以更有效地處理 Linux 系統
4. Added logic to use the first base path if no valid paths are found in the existing loop. | 添加邏輯以在找不到有效路徑時使用第一個基礎路徑
5. Improved maintainability and clarity of the code by explicitly handling different operating systems. | 通過明確處理不同的操作系統，顯著提高了代碼的可維護性和清晰性
6. Fix: Some Issues | 修復一些問題

## [1.8.09] - 2024-04-24

1. Add: Bypass Token Limit Check | 繞過 Token 使用限制檢查
2. Add：Bypass Claude Limit 30000 set to 900000(9e5) | 繞過 Claude 使用限制 30000 設置為 900000(9e5)
3. Add: Force Update Config | 添加強制更新配置
4. Add: Multilanguage support for force update | 添加強制更新功能的多語言支持
5. Fix: Reset break | 修復重置中斷
6. Fix: Some Issues | 修復一些問題

## [1.8.08] - 2024-04-23

1. Add: Force Update Config | 添加強制更新配置
2. Add: Multilanguage support for force update | 添加強制更新功能的多語言支持
3. Fix: Google Auth & Github Auth JWT Problem | 修復 Google Auth & Github Auth JWT 問題
4. Fix: Totally reset import & import * raw options problem | 修復 totally reset import & import * raw 選項問題
5. Fix: reset.file_not_found problem | 修復 reset.file_not_found 問題
6. Outdated: Bypass Cursor Version Check | 過期：繞過 Cursor 版本檢查
7. Document: i.header.set("x-cursor-config-version", "UUID4-xxxxxx-xxxxxx-xxxxxx-xxxxxx"); | 文檔：i.header.set("x-cursor-config-version", "UUID4-xxxxxx-xxxxxx-xxxxxx-xxxxxx");
8. Fix: Some Issues | 修復一些問題

## [1.8.07] - 2024-04-22

1. Add: Bypass Cursor Version Check | 添加繞過 Cursor 版本檢查
2. Add: Multilanguage support for bypass | 添加繞過的多語言支持
3. MSG: Free & free trial accounts can no longer use chat with premium models on Cursor Version 0.45 or less. Please upgrade to Pro or use Cursor Version 0.46 or later. Install Cursor at https://www.cursor.com/downloads or update from within the editor.
4. Fix: Some Issues | 修復一些問題

## [1.8.06] - 2024-04-21

1. Add: Google Account Deletion Feature | 添加 Google 账号删除功能
2. Update: Menu with new account deletion option | 更新菜单添加账号删除选项
3. Add: Multilanguage support for account deletion | 添加账号删除功能的多语言支持
4. Fix: Improve usage limits check and tuple index error | 修复使用限制检查和元组索引错误
5. Fix: bug in disable cursor auto update | 修复禁用 Cursor 自动更新的错误
6. Fix: Linux-appimage | 修复 Linux-appimage 问题
7. Add: Support for custom Cursor installation paths on Windows | 添加 Windows 系统下自定义 Cursor 安装路径支持
8. Add: Chrome profile selection feature | 添加 Chrome 配置文件选择功能
9. Fix: improve account usage limit detection | 修復賬號檢測
10. Fix: For custom Chrome Installations | 修復自定義chrome遊覽器安裝

## [1.8.05] - 2024-04-20

1. Fix: Linux Path Not Found ｜ 修復linuxpath問題
2. Add: support for detecting both 150/150 and 50/50 usage limits ｜ 添加偵測50 或者150的使用量
3. Improve: usage parsing and validation ｜ 檢測使用量

## [1.8.04] - 2024-04-19

1. Update totally_reset_cursor.py | 更新 totally_reset_cursor.py
2. Fix: improve Linux Chrome visibility and root user handling | 修復 Linux Chrome 可見性以及 root 用戶處理
3. Fix: improve Linux path handling and fix permission issues | 修復 Linux 路徑處理以及修復權限問題
4. Fix: Some Issues | 修復一些問題

## [1.0.0] - 2024-05-04

### Added
- Initial project setup based on cursor-auto-free
- 2925.com email support integration
  - Automated email registration system
  - Email verification code auto-retrieval
  - Account management automation
- Multi-language support (English, Simplified Chinese, Traditional Chinese)
- Cross-platform compatibility (Windows, macOS, Linux)

### Changed
- Enhanced email registration process
- Improved account management system
- Optimized automation workflows

### Documentation
- Created comprehensive README in both Chinese and English
- Added detailed usage documentation
- Included system requirements and quick start guide

## [0.1.0] - 2024-05-04

### Initial Features
- Basic project structure setup
- Core functionality implementation
- Initial documentation
