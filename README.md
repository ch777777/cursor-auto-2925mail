# Cursor PRO@2925mail 自动化工具

[English](README.EN.md) | 简体中文

## 📌 项目简介

本项目是一个专注于 Cursor PRO 的自动化工具，提供基于2925.com邮箱的高效账号管理和权限自动更新功能。基于 [cursor-auto-free](https://github.com/chengazhen/cursor-auto-free) (原作者: @chengazhen) 开发，由 [@ch777777](https://github.com/ch777777) 增加了对2925.com邮箱的全面支持。

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
- 账号有效性自动检测
- 账号数据自动备份
- 多线程批量操作支持

### 🔄 权限管理
- 自动循环更新使用权限
- 智能化权限状态监控
- 多账号轮换机制
- 失效预警和自动处理
- 权限状态实时检测
- 自动故障恢复机制
- 异常情况智能处理

### 🌐 系统兼容
- Windows 系统全面支持
- macOS 完整适配
- Linux 系统兼容
- Docker 容器支持
- 云服务器部署支持

### 🌍 多语言支持
- 简体中文
- English
- 繁體中文
- 日本語 (计划中)
- 한국어 (计划中)

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
   - 自定义邮箱前缀选项
   - 批量注册功能
   - 注册进度实时显示
   - 注册结果自动保存

2. **重置现有账号**
   - 重置账号状态
   - 清除历史数据
   - 恢复初始设置
   - 账号配置重置
   - 权限状态重置
   - 自动备份原有数据
   - 重置日志记录

3. **更新账号权限**
   - 自动更新使用权限
   - 批量权限更新
   - 权限状态检查
   - 更新进度显示
   - 失败自动重试
   - 更新日志记录
   - 权限有效期管理

4. **查看账号状态**
   - 显示所有账号信息
   - 检查权限状态
   - 导出账号报告
   - 账号使用统计
   - 权限到期提醒
   - 异常状态标记
   - 详细日志查看

5. **系统设置**
   - 配置代理设置
   - 调整自动更新间隔
   - 设置备份选项
   - 线程数量调整
   - 日志级别设置
   - 网络参数配置
   - 系统性能优化

6. **切换语言**
   - 支持简体中文
   - 支持繁体中文
   - 支持英文
   - 实时切换无需重启
   - 自定义语言包
   - 语言设置保存
   - 界面即时更新

7. **版本信息**
   - 显示当前版本
   - 检查更新
   - 查看更新日志
   - 版本对比
   - 新功能说明
   - 问题修复记录
   - 更新建议提示

8. **退出程序**
   - 安全保存数据
   - 清理临时文件
   - 退出应用
   - 保存当前设置
   - 关闭后台进程
   - 断开网络连接
   - 完整性检查

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
- 批量更新
  ```bash
  python main.py --update-all
  ```
- 定时自动更新
  ```bash
  python main.py --auto-update --interval 24h
  ```

#### 4. 状态监控
- 查看账号状态
  ```bash
  python main.py --status
  ```
- 导出状态报告
  ```bash
  python main.py --export-report
  ```

### 🚀 高级功能
#### 1. 批量操作
- 账号导入导出
  ```bash
  # 导出账号列表
  python main.py --export accounts.csv
  # 导入账号
  python main.py --import accounts.csv
  ```
- 批量权限检查
- 批量状态更新

#### 2. 自动化管理
- 配置定时任务
  ```bash
  # 设置每6小时自动更新
  python main.py --schedule "0 */6 * * *"
  ```
- 失效预警设置
  ```bash
  # 设置到期提醒
  python main.py --alert-before 2d
  ```
- 自动备份数据

#### 3. 异常处理
- 网络异常重试
- 验证码识别失败处理
- 账号异常状态处理
- 自动故障恢复

#### 4. 数据管理
- 数据备份还原
  ```bash
  # 备份数据
  python main.py --backup
  # 还原数据
  python main.py --restore backup.zip
  ```
- 历史记录查询
- 使用统计分析

### 💡 使用技巧
1. **最佳实践**
   - 建议每次批量操作不超过10个账号
   - 定时任务间隔建议设置在4-6小时
   - 及时备份重要数据

2. **常见问题解决**
   - 注册失败：检查网络连接和邮箱配置
   - 验证码识别错误：尝试更换识别模式
   - 权限更新失败：检查账号状态和系统时间

3. **性能优化**
   - 使用代理池分散请求
   - 启用多线程处理
   - 配置本地缓存

### ⚙️ 配置说明
```ini
# .env 配置示例
EMAIL_PREFIX=mycursor     # 邮箱前缀
AUTO_RETRY=3             # 自动重试次数
PROXY_ENABLED=true       # 是否启用代理
THREAD_COUNT=5           # 线程数量
LOG_LEVEL=INFO          # 日志级别
```

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

### 🔧 高级功能
- 代理池自动管理
- API 接口支持
- WebUI 管理界面
- 自定义插件系统
- 数据统计分析
- 自动化测试
- 性能监控优化
