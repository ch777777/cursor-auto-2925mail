import requests
import re
import datetime
from typing import Optional
from .email_tab_interface import EmailTabInterface

class TempMailPlusTab(EmailTabInterface):
    """Implementation of EmailTabInterface for tempmail.plus"""
    
    def __init__(self, email: str, epin: str, translator=None):
        """Initialize TempMailPlusTab
        
        Args:
            email: The email address to check
            epin: The epin token for authentication
            translator: Optional translator for internationalization
        """
        self.email = email
        self.epin = epin
        self.translator = translator
        self.base_url = "https://tempmail.plus/api"
        self.headers = {
            'accept': 'application/json',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://tempmail.plus/zh/',
            'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        self.cookies = {'email': email}
        self._cached_mail_id = None  # 缓存mail_id
        self._cached_verification_code = None  # 缓存验证码
        
    def refresh_inbox(self) -> None:
        """Refresh the email inbox"""
        pass
            
    def check_for_cursor_email(self) -> bool:
        """Check if there is a new email and immediately retrieve verification code
        
        Returns:
            bool: True if new email found and verification code retrieved, False otherwise
        """
        try:
            params = {
                'email': self.email,
                'epin': self.epin
            }
            response = requests.get(
                f"{self.base_url}/mails",
                params=params,
                headers=self.headers,
                cookies=self.cookies
            )
            response.raise_for_status()
            
            data = response.json()
            if data.get('result') and data.get('mail_list'):
                # 检查邮件列表中的第一个邮件是否为新邮件
                if data['mail_list'][0].get('is_new') == True:
                    self._cached_mail_id = data['mail_list'][0].get('mail_id')  # 缓存mail_id
                    
                    # 立即获取验证码
                    verification_code = self._extract_verification_code()
                    if verification_code:
                        self._cached_verification_code = verification_code
                        return True
            return False
        except Exception as e:
            print(f"{self.translator.get('tempmail.check_email_failed', error=str(e)) if self.translator else f'Check email failed: {str(e)}'}")
            return False
    
    def _extract_verification_code(self) -> str:
        """Extract verification code from email content
        
        Returns:
            str: The verification code if found, empty string otherwise
        """
        try:
            if not self._cached_mail_id:
                return ""
                
            params = {
                'email': self.email,
                'epin': self.epin
            }
            response = requests.get(
                f"{self.base_url}/mails/{self._cached_mail_id}",
                params=params,
                headers=self.headers,
                cookies=self.cookies
            )
            response.raise_for_status()
            
            data = response.json()
            if not data.get('result'):
                return ""
                
            # 验证发件人邮箱是否包含cursor字符串
            from_mail = data.get('from_mail', '')
            if 'cursor' not in from_mail.lower():
                return ""
                
            # Extract verification code from text content using regex
            text = data.get('text', '')
            match = re.search(r'\n\n(\d{6})\n\n', text)
            if match:
                return match.group(1)
                
            return ""
        except Exception as e:
            print(f"{self.translator.get('tempmail.extract_code_failed', error=str(e)) if self.translator else f'Extract verification code failed: {str(e)}'}")
            return ""
            
    def get_verification_code(self) -> str:
        """Get the verification code from cache
        
        Returns:
            str: The cached verification code if available, empty string otherwise
        """
        return self._cached_verification_code or ""

if __name__ == "__main__":
    import os
    import time
    import sys
    import configparser
    
    from config import get_config
    
    # 尝试导入 translator
    try:
        from main import Translator
        translator = Translator()
    except ImportError:
        translator = None
    
    config = get_config(translator)
    
    try:
        email = config.get('TempMailPlus', 'email')
        epin = config.get('TempMailPlus', 'epin')
        
        print(f"{translator.get('tempmail.configured_email', email=email) if translator else f'Configured email: {email}'}")
        
        # 初始化TempMailPlusTab，传递 translator
        mail_tab = TempMailPlusTab(email, epin, translator)
        
        # 检查是否有Cursor的邮件
        print(f"{translator.get('tempmail.checking_email') if translator else 'Checking for Cursor verification email...'}")
        if mail_tab.check_for_cursor_email():
            print(f"{translator.get('tempmail.email_found') if translator else 'Found Cursor verification email'}")
            
            # 获取验证码
            verification_code = mail_tab.get_verification_code()
            if verification_code:
                print(f"{translator.get('tempmail.verification_code', code=verification_code) if translator else f'Verification code: {verification_code}'}")
            else:
                print(f"{translator.get('tempmail.no_code') if translator else 'Could not get verification code'}")
        else:
            print(f"{translator.get('tempmail.no_email') if translator else 'No Cursor verification email found'}")
            
    except configparser.Error as e:
        print(f"{translator.get('tempmail.config_error', error=str(e)) if translator else f'Config file error: {str(e)}'}")
    except Exception as e:
        print(f"{translator.get('tempmail.general_error', error=str(e)) if translator else f'An error occurred: {str(e)}'}") 