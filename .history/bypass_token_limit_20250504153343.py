"""
Bypass token limit module for Cursor.

This module provides functionality to modify Cursor's workbench.desktop.main.js
to bypass token limits and customize the UI.

Author: Pin Studios
License: CC BY-NC-ND 4.0
"""

from __future__ import annotations

import configparser
import glob
import os
import platform
import shutil
import sys
import tempfile
from datetime import datetime
from typing import Dict, Optional

from colorama import Fore, Style, init

from config import get_config

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Define emoji constants for UI feedback
EMOJI: Dict[str, str] = {
    "FILE": "📄",
    "BACKUP": "💾",
    "SUCCESS": "✅",
    "ERROR": "❌",
    "INFO": "ℹ️",
    "RESET": "🔄",
    "WARNING": "⚠️",
}

def get_user_documents_path() -> str:
    """
    Get the path to the user's Documents folder.
    
    Returns:
        str: Absolute path to the user's Documents folder
    """
    home = os.path.expanduser("~")
    
    if sys.platform == "win32":
        try:
            import winreg
            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, 
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
            ) as key:
                documents_path, _ = winreg.QueryValueEx(key, "Personal")
                return os.path.normpath(documents_path)
        except (ImportError, WindowsError, OSError):
            return os.path.normpath(os.path.join(home, "Documents"))
    elif sys.platform == "darwin":
        return os.path.normpath(os.path.join(home, "Documents"))
    
    # Linux systems
    sudo_user = os.environ.get('SUDO_USER')
    if sudo_user:
        return os.path.normpath(os.path.join("/home", sudo_user, "Documents"))
    return os.path.normpath(os.path.join(home, "Documents"))

def load_config(config_file: str, translator: Optional[object] = None) -> Optional[configparser.ConfigParser]:
    """
    Safely load configuration from a file with proper error handling.
    
    Args:
        config_file: Path to the configuration file
        translator: Optional translator object for i18n support
        
    Returns:
        ConfigParser: Loaded configuration if successful, None otherwise
    """
    config = configparser.ConfigParser()
    
    try:
        if os.path.exists(config_file):
            config.read(config_file, encoding='utf-8')
        return config
    except (configparser.Error, OSError, IOError) as e:
        error_msg = (translator.get('config.load_failed', error=str(e))
                    if translator else f'Failed to load configuration: {str(e)}')
        print(f"{Fore.RED}{EMOJI['ERROR']} {error_msg}{Style.RESET_ALL}")
        return None

def get_config_value(
    config: configparser.ConfigParser,
    section: str,
    option: str,
    default: str = "",
    translator: Optional[object] = None
) -> str:
    """
    Safely get a configuration value with proper error handling and default value.
    
    Args:
        config: ConfigParser instance
        section: Configuration section name
        option: Configuration option name
        default: Default value if section/option not found
        translator: Optional translator object for i18n support
        
    Returns:
        str: Configuration value or default
    """
    try:
        return config.get(section, option, fallback=default)
    except (configparser.Error, ValueError) as e:
        error_msg = (translator.get('config.get_failed', section=section, option=option, error=str(e))
                    if translator else f'Failed to get config value [{section}]{option}: {str(e)}')
        print(f"{Fore.YELLOW}{EMOJI['WARNING']} {error_msg}{Style.RESET_ALL}")
        return default

def get_workbench_cursor_path(translator: Optional[object] = None) -> str:
    """
    Get the path to Cursor's workbench.desktop.main.js file.
    
    Args:
        translator: Optional translator object for i18n support
        
    Returns:
        str: Absolute path to the workbench.desktop.main.js file
        
    Raises:
        OSError: If the system is not supported or the file is not found
    """
    system = platform.system()
    config_dir = os.path.normpath(os.path.join(get_user_documents_path(), ".cursor-free-vip"))
    config_file = os.path.normpath(os.path.join(config_dir, "config.ini"))
    
    config = load_config(config_file, translator)
    if not config:
        return ""
    
    paths_map = {
        "Darwin": {
            "base": "/Applications/Cursor.app/Contents/Resources/app",
            "main": "out/vs/workbench/workbench.desktop.main.js"
        },
        "Windows": {
            "main": "out\\vs\\workbench\\workbench.desktop.main.js"
        },
        "Linux": {
            "bases": [
                "/opt/Cursor/resources/app",
                "/usr/share/cursor/resources/app",
                "/usr/lib/cursor/app/"
            ],
            "main": "out/vs/workbench/workbench.desktop.main.js"
        }
    }
    
    if system == "Linux":
        extracted_usr_paths = glob.glob(
            os.path.expanduser("~/squashfs-root/usr/share/cursor/resources/app")
        )
        paths_map["Linux"]["bases"].extend(extracted_usr_paths)

    if system not in paths_map:
        error_msg = (translator.get('reset.unsupported_os', system=system) 
                    if translator else f"Unsupported operating system: {system}")
        raise OSError(error_msg)

    if system == "Linux":
        for base in paths_map["Linux"]["bases"]:
            main_path = os.path.normpath(os.path.join(base, paths_map["Linux"]["main"]))
            print(f"{Fore.CYAN}{EMOJI['INFO']} Checking path: {main_path}{Style.RESET_ALL}")
            if os.path.exists(main_path):
                return main_path

    base_path = ""
    if system == "Windows":
        base_path = get_config_value(config, 'WindowsPaths', 'cursor_path', "", translator)
    elif system == "Darwin":
        base_path = get_config_value(config, 'MacPaths', 'cursor_path', paths_map[system]["base"], translator)
    else:  # Linux
        base_path = get_config_value(config, 'LinuxPaths', 'cursor_path', paths_map[system]["bases"][0], translator)

    main_path = os.path.normpath(os.path.join(base_path, paths_map[system]["main"]))
    
    if not os.path.exists(main_path):
        error_msg = (translator.get('reset.file_not_found', path=main_path)
                    if translator else f"Cursor main.js file not found: {main_path}")
        raise OSError(error_msg)
        
    return main_path

def read_file_safely(file_path: str, encoding: str = 'utf-8', errors: str = 'ignore') -> Optional[str]:
    """
    Safely read a file with proper encoding and error handling.
    
    Args:
        file_path: Path to the file to read
        encoding: File encoding to use
        errors: How to handle encoding errors
        
    Returns:
        str: File contents if successful, None otherwise
    """
    try:
        with open(file_path, "r", encoding=encoding, errors=errors) as f:
            return f.read()
    except (OSError, IOError) as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} Failed to read file {file_path}: {str(e)}{Style.RESET_ALL}")
        return None

def write_file_safely(file_path: str, content: str, encoding: str = 'utf-8') -> bool:
    """
    Safely write content to a file with proper encoding.
    
    Args:
        file_path: Path to the file to write
        content: Content to write
        encoding: File encoding to use
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, "w", encoding=encoding) as f:
            f.write(content)
        return True
    except (OSError, IOError) as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} Failed to write file {file_path}: {str(e)}{Style.RESET_ALL}")
        return False

def set_file_permissions(file_path: str, mode: int, translator: Optional[object] = None) -> bool:
    """
    Safely set file permissions with cross-platform support.
    
    Args:
        file_path: Path to the file
        mode: File mode to set
        translator: Optional translator object for i18n support
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        os.chmod(file_path, mode)
        return True
    except (OSError, IOError) as e:
        print(f"{Fore.YELLOW}{EMOJI['WARNING']} Failed to set file permissions for {file_path}: {str(e)}{Style.RESET_ALL}")
        return False

def remove_file_safely(file_path: str, translator: Optional[object] = None) -> bool:
    """
    Safely remove a file with proper error handling.
    
    Args:
        file_path: Path to the file to remove
        translator: Optional translator object for i18n support
        
    Returns:
        bool: True if successful, False otherwise
    """
    if not os.path.exists(file_path):
        return True
        
    try:
        os.remove(file_path)
        return True
    except (OSError, IOError) as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} Failed to remove file {file_path}: {str(e)}{Style.RESET_ALL}")
        return False

def modify_workbench_js(file_path: str, translator: Optional[object] = None) -> bool:
    """
    Modify the workbench.desktop.main.js file to bypass token limit and customize UI.
    
    Args:
        file_path: Path to the workbench.desktop.main.js file
        translator: Optional translator object for i18n support
        
    Returns:
        bool: True if modification was successful, False otherwise
    """
    tmp_path = None
    backup_path = None
    try:
        # Save original file permissions
        try:
            original_mode = os.stat(file_path).st_mode
        except (OSError, IOError) as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Failed to get file permissions: {str(e)}{Style.RESET_ALL}")
            return False

        # Read original content
        content = read_file_safely(file_path)
        if content is None:
            return False

        # Define replacement patterns
        patterns = {
            # Common button replacement patterns
            r'B(k,D(Ln,{title:"Upgrade to Pro",size:"small",get codicon(){return A.rocket},get onClick(){return t.pay}}),null)': 
                r'B(k,D(Ln,{title:"yeongpin GitHub",size:"small",get codicon(){return A.github},get onClick(){return function(){window.open("https://github.com/yeongpin/cursor-free-vip","_blank")}}}),null)',
            
            # Windows/Linux patterns
            r'M(x,I(as,{title:"Upgrade to Pro",size:"small",get codicon(){return $.rocket},get onClick(){return t.pay}}),null)': 
                r'M(x,I(as,{title:"yeongpin GitHub",size:"small",get codicon(){return $.github},get onClick(){return function(){window.open("https://github.com/yeongpin/cursor-free-vip","_blank")}}}),null)',
            
            # Mac patterns
            r'$(k,E(Ks,{title:"Upgrade to Pro",size:"small",get codicon(){return F.rocket},get onClick(){return t.pay}}),null)': 
                r'$(k,E(Ks,{title:"yeongpin GitHub",size:"small",get codicon(){return F.rocket},get onClick(){return function(){window.open("https://github.com/yeongpin/cursor-free-vip","_blank")}}}),null)',
            
            # UI text replacements
            r'<div>Pro Trial': r'<div>Pro',
            r'py-1">Auto-select': r'py-1">Bypass-Version-Pin',
            r'async getEffectiveTokenLimit(e){const n=e.modelName;if(!n)return 2e5;':
                r'async getEffectiveTokenLimit(e){return 9000000;const n=e.modelName;if(!n)return 9e5;',
            r'var DWr=ne("<div class=settings__item_description>You are currently signed in with <strong></strong>.");': 
                r'var DWr=ne("<div class=settings__item_description>You are currently signed in with <strong></strong>. <h1>Pro</h1>");',
            r'notifications-toasts': r'notifications-toasts hidden'
        }

        # Apply all replacements
        for old_pattern, new_pattern in patterns.items():
            content = content.replace(old_pattern, new_pattern)

        # Create temporary file
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            errors="ignore",
            delete=False
        ) as tmp_file:
            tmp_path = tmp_file.name
            if not write_file_safely(tmp_path, content):
                return False

        # Create backup with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{file_path}.backup.{timestamp}"
        
        # Create backup
        try:
            shutil.copy2(file_path, backup_path)
            backup_msg = (translator.get('reset.backup_created', path=backup_path)
                        if translator else f'Backup created: {backup_path}')
            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} {backup_msg}{Style.RESET_ALL}")
        except (OSError, IOError) as e:
            print(f"{Fore.YELLOW}{EMOJI['WARNING']} Failed to create backup: {str(e)}{Style.RESET_ALL}")
            if tmp_path:
                remove_file_safely(tmp_path)
            return False
        
        # Replace original file
        try:
            if not remove_file_safely(file_path):
                if tmp_path:
                    remove_file_safely(tmp_path)
                return False
                
            shutil.move(tmp_path, file_path)
        except (OSError, IOError) as e:
            # Try to restore from backup if replacement fails
            if backup_path and os.path.exists(backup_path):
                try:
                    shutil.copy2(backup_path, file_path)
                    print(f"{Fore.YELLOW}{EMOJI['WARNING']} Restored from backup after failed modification{Style.RESET_ALL}")
                except (OSError, IOError):
                    print(f"{Fore.RED}{EMOJI['ERROR']} Failed to restore from backup{Style.RESET_ALL}")
            if tmp_path:
                remove_file_safely(tmp_path)
            return False

        # Restore file permissions
        if not set_file_permissions(file_path, original_mode, translator):
            print(f"{Fore.YELLOW}{EMOJI['WARNING']} File modified but original permissions could not be restored{Style.RESET_ALL}")

        success_msg = (translator.get('reset.file_modified')
                      if translator else 'File modified successfully')
        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} {success_msg}{Style.RESET_ALL}")
        return True

    except (OSError, IOError, shutil.Error) as e:
        error_msg = (translator.get('reset.modify_file_failed', error=str(e))
                    if translator else f'Failed to modify file: {str(e)}')
        print(f"{Fore.RED}{EMOJI['ERROR']} {error_msg}{Style.RESET_ALL}")
        
        # Clean up temporary file
        if tmp_path and os.path.exists(tmp_path):
            remove_file_safely(tmp_path)
        return False

def run(translator: Optional[object] = None) -> bool:
    """
    Run the token limit bypass process.
    
    Args:
        translator: Optional translator object for i18n support
        
    Returns:
        bool: True if the process was successful, False otherwise
    """
    config = get_config(translator)
    if not config:
        return False

    separator = '=' * 50
    print(f"\n{Fore.CYAN}{separator}{Style.RESET_ALL}")
    
    title_msg = (translator.get('bypass_token_limit.title')
                 if translator else 'Bypass Token Limit')
    print(f"{Fore.CYAN}{EMOJI['RESET']} {title_msg}{Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}{separator}{Style.RESET_ALL}")

    result = modify_workbench_js(get_workbench_cursor_path(translator), translator)

    print(f"\n{Fore.CYAN}{separator}{Style.RESET_ALL}")
    
    prompt_msg = (translator.get('bypass_token_limit.press_enter')
                  if translator else 'Press Enter to continue...')
    input(f"{EMOJI['INFO']} {prompt_msg}")
    
    return result

if __name__ == "__main__":
    try:
        from main import translator as main_translator
        run(main_translator)
    except ImportError:
        run(None)