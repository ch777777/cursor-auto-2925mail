# Cursor Pro 自动化工具

[English](README.EN.md) | 简体中文

## 📌 项目简介

本项目是一个强大的 Cursor Pro 自动化工具，专注于提供高效的账号管理和权限自动更新功能。基于 [cursor-auto-free](https://github.com/chengazhen/cursor-auto-free) 开发，增加了对2925.com邮箱的全面支持。

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

## 📚 使用指南

### 基础功能
- 账号注册
- 验证码处理
- 权限更新
- 状态监控

### 高级功能
- 批量操作
- 自动化管理
- 异常处理
- 数据备份

## 🛠️ 开发相关

### 技术栈
- Python
- Selenium
- requests
- SQLite

### 项目结构
```
cursor-auto-2925mail/
├── main.py              # 主程序入口
├── config.py            # 配置文件
├── utils/               # 工具函数
├── modules/             # 功能模块
└── docs/               # 文档
```

## ⚠️ 免责声明

本项目仅供学习和研究使用，使用本工具所产生的任何后果由使用者自行承担。请遵守相关法律法规，不要用于非法用途。

## 📝 许可证

本项目采用 [CC BY-NC-ND 4.0](LICENSE.md) 许可证。

## 🙏 致谢

感谢原项目作者 [chengazhen](https://github.com/chengazhen) 的开源贡献。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。在提交之前，请确保：
- 代码符合项目规范
- 添加必要的测试
- 更新相关文档

## 📊 项目状态

![GitHub stars](https://img.shields.io/github/stars/ch777777/cursor-auto-2925mail)
![GitHub forks](https://img.shields.io/github/forks/ch777777/cursor-auto-2925mail)
![GitHub issues](https://img.shields.io/github/issues/ch777777/cursor-auto-2925mail)
