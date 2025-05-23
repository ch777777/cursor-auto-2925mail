# Cursor PRO@2925mail Automation Tool

English | [įŽäŊä¸­æ](README.md)

## đ Project Overview

This project is a specialized automation tool for Cursor PRO, providing efficient account management and automatic permission updates based on 2925.com email. Developed based on [cursor-auto-free](https://github.com/chengazhen/cursor-auto-free) (Original Author: @chengazhen), with comprehensive 2925.com email support added by [@ch777777](https://github.com/ch777777).

## đĻ Version Information

- Current Version: v2.7.2
- Update Date: 2024-05-04
- Version History: [CHANGELOG.md](CHANGELOG.md)

### Version Notes
- v2.7.2 - 2925.com Email Support Version
  - 2925.com email auto-registration support
  - Complete account management functionality
  - Automated permission update system
  - Multi-language interface support

## â?Core Features

### đ Account Management
- Automatic registration with 2925.com email
- Smart verification code recognition
- Batch account management system
- Automated account information submission
- Automatic account validity detection
- Account data auto-backup
- Multi-threaded batch operation support

### đ Permission Management
- Automatic permission renewal
- Smart permission status monitoring
- Multi-account rotation mechanism
- Expiration alerts and auto-handling
- Real-time permission status detection
- Automatic fault recovery mechanism
- Intelligent exception handling

### đ System Compatibility
- Full Windows support
- Complete macOS adaptation
- Linux compatibility
- Docker container support
- Cloud server deployment support

### đ Multi-language Support
- English
- Simplified Chinese
- Traditional Chinese
- Japanese (Planned)
- Korean (Planned)

## đ Quick Start

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

## đ Main Menu

After running the program, you will see the following main menu options:

```
đ¯ Cursor PRO@2925mail Automation Tool Main Menu

1. â?Create New Account (2925.com email)
2. đ Reset Existing Account
3. đ Update Account Permissions
4. đ View Account Status
5. âī¸ System Settings
6. đ Switch Language
7. âšī¸ View Version Info
8. â?Exit Program

Please enter option number (1-8): 
```

### Menu Options Description

1. **Create New Account**
   - Automatic 2925.com email registration
   - Automatic verification and activation
   - Initial settings configuration
   - Custom email prefix option
   - Batch registration functionality
   - Real-time registration progress
   - Auto-save registration results

2. **Reset Existing Account**
   - Reset account status
   - Clear historical data
   - Restore initial settings
   - Account configuration reset
   - Permission status reset
   - Auto-backup of existing data
   - Reset logging

3. **Update Account Permissions**
   - Automatic permission updates
   - Batch permission updates
   - Permission status check
   - Update progress display
   - Automatic retry on failure
   - Update logging
   - Permission validity management

4. **View Account Status**
   - Display all account information
   - Check permission status
   - Export account report
   - Account usage statistics
   - Permission expiration alerts
   - Abnormal status marking
   - Detailed log viewing

5. **System Settings**
   - Configure proxy settings
   - Adjust auto-update interval
   - Set backup options
   - Thread count adjustment
   - Log level configuration
   - Network parameter settings
   - System performance optimization

6. **Switch Language**
   - Support Simplified Chinese
   - Support Traditional Chinese
   - Support English
   - Real-time switching without restart
   - Custom language packs
   - Language setting persistence
   - Instant UI updates

7. **Version Information**
   - Show current version
   - Check for updates
   - View changelog
   - Version comparison
   - New feature descriptions
   - Bug fix records
   - Update recommendations

8. **Exit Program**
   - Save data safely
   - Clean temporary files
   - Exit application
   - Save current settings
   - Close background processes
   - Disconnect network
   - Integrity check

## đ Usage Guide

### đ° Basic Functions
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

### đ Advanced Features
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

### đĄ Usage Tips
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

### âī¸ Configuration
```ini
# .env configuration example
EMAIL_PREFIX=mycursor     # Email prefix
AUTO_RETRY=3             # Auto retry count
PROXY_ENABLED=true       # Enable proxy
THREAD_COUNT=5           # Thread count
LOG_LEVEL=INFO          # Log level
```

## đ ī¸?Development

### Tech Stack
- Python
- Selenium
- requests
- SQLite

### Project Structure
```
cursor-auto-2925mail/
âââ main.py              # Main program entry
âââ config.py            # Configuration file
âââ utils/               # Utility functions
âââ modules/             # Function modules
âââ docs/               # Documentation
```

## â ī¸ Disclaimer

This project is for learning and research purposes only. Users bear all consequences of using this tool. Please comply with relevant laws and regulations and do not use for illegal purposes.

## đ License

This project is licensed under [CC BY-NC-ND 4.0](LICENSE.md).

## đ Acknowledgments

Thanks to the original project author [chengazhen](https://github.com/chengazhen) for the open source contribution.

## đ¤ Contributing

Welcome to submit Issues and Pull Requests to help improve the project. Before submitting, please ensure:
- Code complies with project standards
- Add necessary tests
- Update relevant documentation

## đ Project Status

![GitHub stars](https://img.shields.io/github/stars/ch777777/cursor-auto-2925mail)
![GitHub forks](https://img.shields.io/github/forks/ch777777/cursor-auto-2925mail)
![GitHub issues](https://img.shields.io/github/issues/ch777777/cursor-auto-2925mail)

### đ§ Advanced Features
- Proxy pool auto-management
- API interface support
- WebUI management interface
- Custom plugin system
- Data statistics and analysis
- Automated testing
- Performance monitoring and optimization 
