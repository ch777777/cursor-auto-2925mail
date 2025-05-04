# Cursor PRO@2925mail Automation Tool

English | [简体中文](README.md)

## 📌 Project Overview

This project is a specialized automation tool for Cursor PRO, providing efficient account management and automatic permission updates based on 2925.com email. Developed based on [cursor-auto-free](https://github.com/chengazhen/cursor-auto-free) (Original Author: @chengazhen), with comprehensive 2925.com email support added by [@ch777777](https://github.com/ch777777).

## 📦 Version Information

- Current Version: v1.2.0
- Update Date: 2024-05-04
- Version History: [CHANGELOG.md](CHANGELOG.md)

### Version Notes
- v1.2.0 - 2925.com Email Support Version
  - 2925.com email auto-registration support
  - Complete account management functionality
  - Automated permission update system
  - Multi-language interface support

## ✨ Core Features

### 🔑 Account Management
- Automatic registration with 2925.com email
- Smart verification code recognition
- Batch account management system
- Automated account information submission

### 🔄 Permission Management
- Automatic permission renewal
- Smart permission status monitoring
- Multi-account rotation mechanism
- Expiration alerts and auto-handling

### 🌐 System Compatibility
- Full Windows support
- Complete macOS adaptation
- Linux compatibility

### 🌍 Multi-language Support
- English
- Simplified Chinese
- Traditional Chinese

## 🚀 Quick Start

### Requirements
- Python 3.7+
- Stable network connection
- System permissions

### Installation Steps
1. Clone repository
```bash
git clone https://github.com/ch777777/cursor-auto-2925mail.git
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure settings
```bash
cp .env.example .env
# Edit .env file with necessary configurations
```

4. Run program
```bash
python main.py
```

## 📋 Main Menu

After running the program, you will see the following main menu options:

```
🎯 Cursor PRO@2925mail Automation Tool Main Menu

1. ✨ Create New Account (2925.com email)
2. 🔄 Reset Existing Account
3. 🔑 Update Account Permissions
4. 📊 View Account Status
5. ⚙️ System Settings
6. 🌍 Switch Language
7. ℹ️ View Version Info
8. ❌ Exit Program

Please enter option number (1-8): 
```

### Menu Options Description

1. **Create New Account**
   - Automatic 2925.com email registration
   - Automatic verification and activation
   - Initial settings configuration

2. **Reset Existing Account**
   - Reset account status
   - Clear historical data
   - Restore initial settings

3. **Update Account Permissions**
   - Automatic permission updates
   - Batch permission updates
   - Permission status check

4. **View Account Status**
   - Display all account information
   - Check permission status
   - Export account report

5. **System Settings**
   - Configure proxy settings
   - Adjust auto-update interval
   - Set backup options

6. **Switch Language**
   - Support Simplified Chinese
   - Support Traditional Chinese
   - Support English

7. **Version Information**
   - Show current version
   - Check for updates
   - View changelog

8. **Exit Program**
   - Save data safely
   - Clean temporary files
   - Exit application

## 📚 Usage Guide

### 🔰 Basic Functions
#### 1. Account Registration
- Automatic Registration
  ```bash
  python main.py --register
  ```
- Batch Registration
  ```bash
  python main.py --register-batch --count 5
  ```
- Custom Email Prefix
  ```bash
  python main.py --register --prefix "mycursor"
  ```

#### 2. Verification Code Handling
- Automatic Code Retrieval
- Smart Recognition & Filling
- Failure Retry Mechanism
- Verification Code Logging

#### 3. Permission Updates
- Single Account Update
  ```bash
  python main.py --update-permission --email "example@2925.com"
  ```
- Batch Update
  ```bash
  python main.py --update-all
  ```
- Scheduled Auto Update
  ```bash
  python main.py --auto-update --interval 24h
  ```

#### 4. Status Monitoring
- Check Account Status
  ```bash
  python main.py --status
  ```
- Export Status Report
  ```bash
  python main.py --export-report
  ```

### 🚀 Advanced Features
#### 1. Batch Operations
- Account Import/Export
  ```bash
  # Export account list
  python main.py --export accounts.csv
  # Import accounts
  python main.py --import accounts.csv
  ```
- Batch Permission Check
- Batch Status Update

#### 2. Automated Management
- Configure Scheduled Tasks
  ```bash
  # Set auto-update every 6 hours
  python main.py --schedule "0 */6 * * *"
  ```
- Expiration Alert Settings
  ```bash
  # Set expiration reminder
  python main.py --alert-before 2d
  ```
- Automatic Data Backup

#### 3. Exception Handling
- Network Error Retry
- Verification Code Recognition Failure
- Account Exception Handling
- Automatic Fault Recovery

#### 4. Data Management
- Data Backup & Restore
  ```bash
  # Backup data
  python main.py --backup
  # Restore data
  python main.py --restore backup.zip
  ```
- History Query
- Usage Analytics

### 💡 Usage Tips
1. **Best Practices**
   - Recommended batch size: no more than 10 accounts
   - Suggested schedule interval: 4-6 hours
   - Regular data backup

2. **Common Issues**
   - Registration Failed: Check network and email configuration
   - Code Recognition Error: Try different recognition mode
   - Permission Update Failed: Check account status and system time

3. **Performance Optimization**
   - Use proxy pool for requests
   - Enable multi-threading
   - Configure local cache

### ⚙️ Configuration
```ini
# .env configuration example
EMAIL_PREFIX=mycursor     # Email prefix
AUTO_RETRY=3             # Auto retry count
PROXY_ENABLED=true       # Enable proxy
THREAD_COUNT=5           # Thread count
LOG_LEVEL=INFO          # Log level
```

## 🛠️ Development

### Tech Stack
- Python
- Selenium
- requests
- SQLite

### Project Structure
```
cursor-auto-2925mail/
├── main.py              # Main program entry
├── config.py            # Configuration file
├── utils/               # Utility functions
├── modules/             # Function modules
└── docs/               # Documentation
```

## ⚠️ Disclaimer

This project is for learning and research purposes only. Users bear all consequences of using this tool. Please comply with relevant laws and regulations and do not use for illegal purposes.

## 📝 License

This project is licensed under [CC BY-NC-ND 4.0](LICENSE.md).

## 🙏 Acknowledgments

Thanks to the original project author [chengazhen](https://github.com/chengazhen) for the open source contribution.

## 🤝 Contributing

Welcome to submit Issues and Pull Requests to help improve the project. Before submitting, please ensure:
- Code complies with project standards
- Add necessary tests
- Update relevant documentation

## 📊 Project Status

![GitHub stars](https://img.shields.io/github/stars/ch777777/cursor-auto-2925mail)
![GitHub forks](https://img.shields.io/github/forks/ch777777/cursor-auto-2925mail)
![GitHub issues](https://img.shields.io/github/issues/ch777777/cursor-auto-2925mail) 