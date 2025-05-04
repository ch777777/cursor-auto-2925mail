import os
import sys
import time
import random
import json
import traceback
from colorama import Fore, Style, init
from faker import Faker
from cursor_auth import CursorAuth
from reset_machine_manual import MachineIDResetter
from get_user_token import get_token_from_cookie
from config import get_config
from DrissionPage import ChromiumOptions, ChromiumPage

# 初始化colorama
init()

# Define emoji constants
EMOJI = {
    'START': '🚀',
    'FORM': '📝',
    'VERIFY': '🔄',
    'PASSWORD': '🔑',
    'CODE': '📱',
    'DONE': '✨',
    'ERROR': '❌',
    'WAIT': '⏳',
    'SUCCESS': '✅',
    'MAIL': '📧',
    'KEY': '🔐',
    'UPDATE': '🔄',
    'INFO': 'ℹ️'
}

def check_chrome_installation():
    """检查Chrome是否已安装"""
    default_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    
    for path in default_paths:
        if os.path.exists(path):
            return path
    return None

def create_required_directories():
    """创建必要的目录"""
    dirs = ['downloads', 'user_data', 'cache']
    for dir_name in dirs:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

class NumberManager:
    def __init__(self):
        self.used_numbers_file = "used_numbers.json"
        self.used_numbers = self.load_used_numbers()
        
    def load_used_numbers(self):
        """加载已使用的数字"""
        try:
            if os.path.exists(self.used_numbers_file):
                with open(self.used_numbers_file, 'r') as f:
                    return set(json.load(f))
            return set()
        except Exception:
            return set()
            
    def save_used_numbers(self):
        """保存已使用的数字"""
        try:
            with open(self.used_numbers_file, 'w') as f:
                json.dump(list(self.used_numbers), f)
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} 保存已使用数字失败: {str(e)}{Style.RESET_ALL}")
            
    def get_unused_number(self):
        """获取一个未使用的数字（7-1000范围）"""
        available_numbers = set(range(7, 1001)) - self.used_numbers
        if not available_numbers:
            print(f"{Fore.RED}{EMOJI['ERROR']} 所有可用数字已用完！{Style.RESET_ALL}")
            return None
            
        number = random.choice(list(available_numbers))
        self.used_numbers.add(number)
        self.save_used_numbers()
        return number

# 创建NumberManager实例
number_manager = NumberManager()

class CursorRegistration:
    def __init__(self, translator=None):
        self.translator = translator
        
        # Set to display mode
        os.environ['BROWSER_HEADLESS'] = 'False'
        self.browser = None
        self.controller = None
        self.sign_up_url = "https://authenticator.cursor.sh/sign-up"
        self.settings_url = "https://www.cursor.com/settings"
        self.email_address = None
        self.signup_tab = None
        self.email_tab = None
        
        # initialize Faker instance
        self.faker = Faker()
        
        # generate account information
        self.password = self._generate_password()
        self.first_name = self.faker.first_name()
        self.last_name = self.faker.last_name()
        
        # modify the first letter of the first name
        new_first_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.first_name = new_first_letter + self.first_name[1:]
        
        print(f"\n{Fore.CYAN}{EMOJI['PASSWORD']} 密码: {self.password} {Style.RESET_ALL}")
        print(f"{Fore.CYAN}{EMOJI['FORM']} 名字: {self.first_name} {Style.RESET_ALL}")
        print(f"{Fore.CYAN}{EMOJI['FORM']} 姓氏: {self.last_name} {Style.RESET_ALL}")

    def _generate_password(self, length=12):
        """Generate password"""
        return self.faker.password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)

    def setup_email(self):
        """Setup Email"""
        try:
            # 获取未使用的数字
            random_number = number_manager.get_unused_number()
            if random_number is None:
                return False
            
            # Generate email in required format
            self.email_address = f"chnanan72{random_number}@2925.com"
            
            print(f"{Fore.CYAN}{EMOJI['MAIL']} 邮箱地址: {self.email_address}" + "\n" + f"{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} 邮箱设置失败: {str(e)}{Style.RESET_ALL}")
            print(traceback.format_exc())
            return False

    def get_verification_code(self):
        """Automatically Get Verification Code from 2925.com"""
        verification_page = None
        try:
            # 创建浏览器选项
            co = ChromiumOptions()
            co.set_argument("--incognito")
            co.set_argument("--disable-gpu")
            co.set_argument("--no-sandbox")
            co.set_argument("--disable-dev-shm-usage")
            
            # 创建浏览器实例
            verification_page = ChromiumPage(co)
            
            # 访问登录页面
            print(f"{Fore.CYAN}{EMOJI['INFO']} 正在访问登录页面...{Style.RESET_ALL}")
            verification_page.get("https://www.2925.com/login/")
            time.sleep(3)  # 等待页面加载
            
            # 输入账号
            print(f"{Fore.CYAN}{EMOJI['INFO']} 正在输入账号...{Style.RESET_ALL}")
            account_input = verification_page.ele("#ipt_account")
            if account_input:
                account_input.input("chanan72")
                time.sleep(1)
            
            # 输入密码
            print(f"{Fore.CYAN}{EMOJI['INFO']} 正在输入密码...{Style.RESET_ALL}")
            password_input = verification_page.ele("#ipt_password")
            if password_input:
                password_input.input("mzxgfwlpt00")
                time.sleep(1)
            
            # 点击所有复选框
            print(f"{Fore.CYAN}{EMOJI['INFO']} 正在勾选协议...{Style.RESET_ALL}")
            checkboxes = verification_page.eles("css:.iCheck-helper")
            for checkbox in checkboxes:
                try:
                    checkbox.click()
                    time.sleep(0.5)
                except:
                    continue
            
            # 点击登录按钮
            print(f"{Fore.CYAN}{EMOJI['INFO']} 正在登录...{Style.RESET_ALL}")
            login_button = verification_page.ele("#btn_login")
            if login_button:
                login_button.click()
                time.sleep(3)
            
            # 访问邮件列表页面
            print(f"{Fore.CYAN}{EMOJI['INFO']} 正在访问邮件列表...{Style.RESET_ALL}")
            verification_page.get("https://www.2925.com/#/mailList")
            time.sleep(3)
            
            # 查找并点击最新的验证邮件
            max_attempts = 10
            for attempt in range(max_attempts):
                # 查找"刚刚"发送的邮件
                recent_emails = verification_page.eles("css:.date-time-text")
                verify_titles = verification_page.eles("css:.mail-content-title")
                
                for i, (time_text, title) in enumerate(zip(recent_emails, verify_titles)):
                    if time_text.text == "刚刚" and "Verify your email address" in title.text:
                        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 找到验证邮件{Style.RESET_ALL}")
                        title.click()
                        time.sleep(3)
                        
                        # 提取验证码
                        code_element = verification_page.ele("css:div[style*='font-family:-apple-system']")
                        if code_element:
                            code = code_element.text.strip()
                            if code.isdigit() and len(code) == 6:
                                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 验证码获取成功: {code}{Style.RESET_ALL}")
                                return code
                
                if attempt < max_attempts - 1:
                    print(f"{Fore.YELLOW}{EMOJI['WAIT']} 等待验证邮件，尝试次数: {attempt + 1}/{max_attempts}{Style.RESET_ALL}")
                    time.sleep(3)
                    verification_page.refresh()
            
            print(f"{Fore.RED}{EMOJI['ERROR']} 未找到验证码{Style.RESET_ALL}")
            return None
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} 获取验证码失败: {str(e)}{Style.RESET_ALL}")
            print(traceback.format_exc())
            return None
        finally:
            if verification_page:
                try:
                    verification_page.quit()
                except:
                    pass

    def register_cursor(self):
        """Register Cursor"""
        browser_tab = None
        try:
            print(f"{Fore.CYAN}{EMOJI['START']} {self.translator.get('register.register_start')}...{Style.RESET_ALL}")
            
            # Check if tempmail_plus is enabled
            config = get_config(self.translator)
            email_tab = None
            if config and config.has_section('TempMailPlus'):
                if config.getboolean('TempMailPlus', 'enabled'):
                    email = config.get('TempMailPlus', 'email')
                    epin = config.get('TempMailPlus', 'epin')
                    if email and epin:
                        from email_tabs.tempmail_plus_tab import TempMailPlusTab
                        email_tab = TempMailPlusTab(email, epin, self.translator)
                        print(f"{Fore.CYAN}{EMOJI['MAIL']} {self.translator.get('register.using_tempmail_plus')}{Style.RESET_ALL}")
            
            # Use new_signup.py directly for registration
            from new_signup import main as new_signup_main
            
            # Execute new registration process, passing translator
            result, browser_tab = new_signup_main(
                email=self.email_address,
                password=self.password,
                first_name=self.first_name,
                last_name=self.last_name,
                email_tab=email_tab,  # Pass email_tab if tempmail_plus is enabled
                controller=self,  # Pass self instead of self.controller
                translator=self.translator
            )
            
            if result:
                # Use the returned browser instance to get account information
                self.signup_tab = browser_tab  # Save browser instance
                success = self._get_account_info()
                
                # Close browser after getting information
                if browser_tab:
                    try:
                        browser_tab.quit()
                    except:
                        pass
                
                return success
            
            return False
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} {self.translator.get('register.register_process_error', error=str(e))}{Style.RESET_ALL}")
            return False
        finally:
            # Ensure browser is closed in any case
            if browser_tab:
                try:
                    browser_tab.quit()
                except:
                    pass
                
    def _get_account_info(self):
        """Get Account Information and Token"""
        try:
            self.signup_tab.get(self.settings_url)
            time.sleep(2)
            
            usage_selector = (
                "css:div.col-span-2 > div > div > div > div > "
                "div:nth-child(1) > div.flex.items-center.justify-between.gap-2 > "
                "span.font-mono.text-sm\\/\\[0\\.875rem\\]"
            )
            usage_ele = self.signup_tab.ele(usage_selector)
            total_usage = "未知"
            if usage_ele:
                total_usage = usage_ele.text.split("/")[-1].strip()

            print(f"Total Usage: {total_usage}\n")
            print(f"{Fore.CYAN}{EMOJI['WAIT']} {self.translator.get('register.get_token')}...{Style.RESET_ALL}")
            max_attempts = 30
            retry_interval = 2
            attempts = 0

            while attempts < max_attempts:
                try:
                    cookies = self.signup_tab.cookies()
                    for cookie in cookies:
                        if cookie.get("name") == "WorkosCursorSessionToken":
                            token = get_token_from_cookie(cookie["value"], self.translator)
                            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} {self.translator.get('register.token_success')}{Style.RESET_ALL}")
                            self._save_account_info(token, total_usage)
                            return True

                    attempts += 1
                    if attempts < max_attempts:
                        print(f"{Fore.YELLOW}{EMOJI['WAIT']} {self.translator.get('register.token_attempt', attempt=attempts, time=retry_interval)}{Style.RESET_ALL}")
                        time.sleep(retry_interval)
                    else:
                        print(f"{Fore.RED}{EMOJI['ERROR']} {self.translator.get('register.token_max_attempts', max=max_attempts)}{Style.RESET_ALL}")

                except Exception as e:
                    print(f"{Fore.RED}{EMOJI['ERROR']} {self.translator.get('register.token_failed', error=str(e))}{Style.RESET_ALL}")
                    attempts += 1
                    if attempts < max_attempts:
                        print(f"{Fore.YELLOW}{EMOJI['WAIT']} {self.translator.get('register.token_attempt', attempt=attempts, time=retry_interval)}{Style.RESET_ALL}")
                        time.sleep(retry_interval)

            return False

        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} {self.translator.get('register.account_error', error=str(e))}{Style.RESET_ALL}")
            return False

    def _save_account_info(self, token, total_usage):
        """Save Account Information to File"""
        try:
            # Update authentication information first
            print(f"{Fore.CYAN}{EMOJI['KEY']} {self.translator.get('register.update_cursor_auth_info')}...{Style.RESET_ALL}")
            if self.update_cursor_auth(email=self.email_address, access_token=token, refresh_token=token, auth_type="Auth_0"):
                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} {self.translator.get('register.cursor_auth_info_updated')}...{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}{EMOJI['ERROR']} {self.translator.get('register.cursor_auth_info_update_failed')}...{Style.RESET_ALL}")

            # Reset machine ID
            print(f"{Fore.CYAN}{EMOJI['UPDATE']} {self.translator.get('register.reset_machine_id')}...{Style.RESET_ALL}")
            resetter = MachineIDResetter(self.translator)  # Create instance with translator
            if not resetter.reset_machine_ids():  # Call reset_machine_ids method directly
                raise Exception("Failed to reset machine ID")
            
            # Save account information to file
            with open('cursor_accounts.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n{'='*50}\n")
                f.write(f"Email: {self.email_address}\n")
                f.write(f"Password: {self.password}\n")
                f.write(f"Token: {token}\n")
                f.write(f"Usage Limit: {total_usage}\n")
                f.write(f"{'='*50}\n")
                
            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} {self.translator.get('register.account_info_saved')}...{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} {self.translator.get('register.save_account_info_failed', error=str(e))}{Style.RESET_ALL}")
            return False

    def start(self):
        """Start Registration Process"""
        try:
            if self.setup_email():
                if self.register_cursor():
                    print(f"\n{Fore.GREEN}{EMOJI['DONE']} {self.translator.get('register.cursor_registration_completed')}...{Style.RESET_ALL}")
                    return True
            return False
        finally:
            # Close email tab
            if hasattr(self, 'temp_email'):
                try:
                    self.temp_email.close()
                except:
                    pass

    def update_cursor_auth(self, email=None, access_token=None, refresh_token=None, auth_type="Auth_0"):
        """Convenient function to update Cursor authentication information"""
        auth_manager = CursorAuth(translator=self.translator)
        return auth_manager.update_auth(email, access_token, refresh_token, auth_type)

def main():
    """主函数"""
    try:
        # 创建必要的目录
        create_required_directories()
        
        # 检查Chrome安装
        chrome_path = check_chrome_installation()
        if not chrome_path:
            print(f"{Fore.RED}{EMOJI['ERROR']} Chrome浏览器未安装或未找到，请安装Chrome后重试{Style.RESET_ALL}")
            return
            
        print(f"{Fore.CYAN}{EMOJI['INFO']} 正在使用 chrome 浏览器: {chrome_path}{Style.RESET_ALL}")
        
        # 初始化注册对象
        registration = CursorRegistration()
        
        # 开始注册流程
        if registration.start():
            print(f"\n{Fore.GREEN}{EMOJI['DONE']} 注册完成！{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}{EMOJI['ERROR']} 注册失败，请重试{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} 程序运行出错: {str(e)}{Style.RESET_ALL}")
        print(traceback.format_exc())
    finally:
        input(f"\n{EMOJI['INFO']} 按回车键退出...")

if __name__ == "__main__":
    main() 