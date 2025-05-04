# Cursor PRO@2925mail 自动化工具

[English](README.EN.md) | 简体中文

## 📌 项目简介

本项目是一个专注于 Cursor PRO 的自动化工具，提供基于2925.com邮箱的高效账号管理和权限自动更新功能。基于 cursor-auto-free (原作者: @chengazhen) 开发，由 @ch777777 增加了对2925.com邮箱的全面支持。

GitHub 仓库地址: [https://github.com/ch777777/cursor-auto-2925mail?tab=readme-ov-file](https://github.com/ch777777/cursor-auto-2925mail?tab=readme-ov-file)

## 📦 版本信息

- 当前版本：v1.2.0
- 更新日期：2024-05-04
- 版本历史：[CHANGELOG.md](CHANGELOG.md)

### 版本说明
- v1.2.0 - 2925.com邮箱支持版本
  - 支持2925.com邮箱自动注册
  - 完整的账号管理功能
  - 自动化权限更新系统
  - 多语言界面支持

## ✨ 核心特性

### 🔑 账号管理
- 支持2925.com邮箱自动注册
- 智能验证码识别和处理
- 批量账号管理系统
- 自动化账号信息提交

### 🔄 权限管理
- 自动循环更新使用权限
- 智能化权限状态监控
- 多账号轮换机制
- 失效预警和自动处理

### 🌐 系统兼容
- Windows 系统全面支持
- macOS 完整适配
- Linux 系统兼容

### 🌍 多语言支持
- 简体中文
- English
- 繁體中文

## 🚀 快速开始

### 环境要求
- Python 3.7+
- 稳定的网络连接
- 系统权限要求

### 安装步骤
1. 克隆仓库
```bash
git clone https://github.com/ch777777/cursor-auto-2925mail.git
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置设置
```bash
cp .env.example .env
# 编辑 .env 文件，填入必要配置
```

4. 运行程序
```bash
python main.py
```

## 📋 主菜单功能

运行程序后，你将看到以下主菜单选项：

```
🎯 Cursor PRO@2925mail 自动化工具 主菜单

1. ✨ 创建新账号 (2925.com邮箱)
2. 🔄 重置现有账号
3. 🔑 更新账号权限
4. 📊 查看账号状态
5. ⚙️ 系统设置
6. 🌍 切换语言
7. ℹ️ 查看版本信息
8. ❌ 退出程序

请输入选项编号 (1-8): 
```

### 菜单选项说明

1. **创建新账号**
   - 自动注册2925.com邮箱
   - 自动验证和激活账号
   - 配置初始设置

2. **重置现有账号**
   - 重置账号状态
   - 清除历史数据
   - 恢复初始设置

3. **更新账号权限**
   - 自动更新使用权限
   - 批量权限更新
   - 权限状态检查

4. **查看账号状态**
   - 显示所有账号信息
   - 检查权限状态
   - 导出账号报告

5. **系统设置**
   - 配置代理设置
   - 调整自动更新间隔
   - 设置备份选项

6. **切换语言**
   - 支持简体中文
   - 支持繁体中文
   - 支持英文

7. **版本信息**
   - 显示当前版本
   - 检查更新
   - 查看更新日志

8. **退出程序**
   - 安全保存数据
   - 清理临时文件
   - 退出应用

## 📚 使用指南

### 🔰 基础功能
#### 1. 账号注册
- 自动注册流程
  ```bash
  python main.py --register
  ```
- 批量注册模式
  ```bash
  python main.py --register-batch --count 5
  ```
- 自定义邮箱前缀
  ```bash
  python main.py --register --prefix "mycursor"
  ```

#### 2. 验证码处理
- 自动获取验证码
- 智能识别与填充
- 失败重试机制
- 验证码日志记录

#### 3. 权限更新
- 单账号更新
  ```bash
  python main.py --update-permission --email "example@2925.com"
  ```