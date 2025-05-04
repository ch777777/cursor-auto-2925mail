import os
import sys
from colorama import Fore, Style, init
import time
import random
from faker import Faker
from cursor_auth import CursorAuth
from reset_machine_manual import MachineIDResetter
from get_user_token import get_token_from_cookie
from config import get_config
from DrissionPage import ChromiumOptions, ChromiumPage
import traceback

os.environ["PYTHONVERBOSE"] = "0"
os.environ["PYINSTALLER_VERBOSE"] = "0"

# Initialize colorama
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
    'INFO': 'ℹ️',
    'WARN': '⚠️'
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

def save_2925_account(email_name, password):
    """Save 2925 email account information"""
    try:
        # 保存到单独的文件，每次覆盖而不是追加
        with open("2925_accounts.txt", "w", encoding="utf-8") as f:
            f.write(f"邮箱: {email_name}@2925.com\n")
            f.write(f"密码: {password}\n")
        print(f"{Fore.CYAN}{EMOJI['INFO']} 账号信息已保存到 2925_accounts.txt{Style.RESET_ALL}")
        return True
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} 保存账号信息失败: {str(e)}{Style.RESET_ALL}")
        return False

def setup_email(translator=None):
    """Setup email account on 2925.com"""
    try:
        # 获取用户输入
        print(f"{Fore.CYAN}{EMOJI['INFO']} 请输入注册信息（输入q退出）：{Style.RESET_ALL}")
        email_name = input(f"{Fore.CYAN}邮箱名 (9~12个字符，字母+数字) 或 q 退出: {Style.RESET_ALL}")
        if email_name.lower() == 'q':
            return None
            
        password = input(f"{Fore.CYAN}密码 (6~16个字符) 或 q 退出: {Style.RESET_ALL}")
        if password.lower() == 'q':
            return None
            
        phone = input(f"{Fore.CYAN}手机号码 或 q 退出: {Style.RESET_ALL}")
        if phone.lower() == 'q':
            return None

        # 生成1-1000之间的随机数（不包含1-7）
        valid_numbers = list(range(8, 1001))
        random_number = random.choice(valid_numbers)
        
        # 组合邮箱名 - 这个用于Cursor注册
        cursor_email_name = f"{email_name}{random_number}"
        print(f"{Fore.CYAN}{EMOJI['INFO']} Cursor将使用的邮箱名: {cursor_email_name}{Style.RESET_ALL}")
        
        # 创建浏览器选项
        co = ChromiumOptions()
        co.set_argument("--incognito")
        co.set_argument("--disable-gpu")
        co.set_argument("--no-sandbox")
        co.set_argument("--disable-dev-shm-usage")
        
        # 创建浏览器实例
        page = ChromiumPage(co)
        
        print(f"{Fore.CYAN}{EMOJI['INFO']} 正在访问2925.com...{Style.RESET_ALL}")
        page.get("https://www.2925.com/login/")
        time.sleep(3)  # 等待页面加载
        
        # 点击注册账号按钮
        register_button = page.ele("css:.btn-register")
        if register_button:
            register_button.click()
            time.sleep(2)
        
        # 输入邮箱名 - 使用原始邮箱名
        email_input = page.ele("#reg-account")
        if email_input:
            email_input.input(email_name)
            time.sleep(1)
        
        # 输入密码
        password_input = page.ele("#reg-pwd")
        if password_input:
            password_input.input(password)
            time.sleep(1)
        
        # 确认密码
        confirm_password_input = page.ele("#reg-confirm")
        if confirm_password_input:
            confirm_password_input.input(password)
            time.sleep(1)
        
        # 输入手机号码
        phone_input = page.ele("#reg-phone")
        if phone_input:
            phone_input.input(phone)
            time.sleep(1)
        
        # 点击用户同意框
        checkbox = page.ele("css:.register-checkbox")
        if checkbox:
            checkbox.click()
            time.sleep(1)
        
        # 点击获取验证码按钮
        code_button = page.ele("#codeBtn")
        if code_button:
            code_button.click()
            time.sleep(1)
        
        # 获取用户输入的验证码
        verification_code = input(f"{Fore.CYAN}请输入收到的手机验证码: {Style.RESET_ALL}")
        
        # 输入验证码
        code_input = page.ele("#reg-message")
        if code_input:
            code_input.input(verification_code)
            time.sleep(1)
        
        # 点击立即注册按钮
        submit_button = page.ele("//span[text()='立即注册']")
        if submit_button:
            submit_button.click()
            time.sleep(2)
        
        # 等待注册完成后，进行登录
        print(f"{Fore.CYAN}{EMOJI['INFO']} 正在登录邮箱...{Style.RESET_ALL}")
        page.get("https://www.2925.com/login/")
        time.sleep(3)
        
        # 输入账号 - 使用原始邮箱名
        account_input = page.ele("#ipt_account")
        if account_input:
            account_input.input(email_name)
            time.sleep(1)
        
        # 输入密码
        password_input = page.ele("#ipt_password")
        if password_input:
            password_input.input(password)
            time.sleep(1)
        
        # 勾选用户协议
        try:
            checkboxes = page.eles("css:ins.iCheck-helper")
            for checkbox in checkboxes:
                checkbox.click()
                time.sleep(0.5)
        except Exception as e:
            print(f"{Fore.YELLOW}{EMOJI['WARN']} 勾选协议失败，尝试其他方式: {str(e)}")
            try:
                checkboxes = page.eles("css:div.icheckbox_minimal-grey")
                for checkbox in checkboxes:
                    checkbox.click()
                    time.sleep(0.5)
            except:
                pass
        
        # 点击登录按钮
        login_button = page.ele("#btn_login")
        if login_button:
            login_button.click()
            time.sleep(3)
        
        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 注册并登录成功！{Style.RESET_ALL}")
        print(f"{Fore.GREEN}邮箱地址: {email_name}@2925.com{Style.RESET_ALL}")
        print(f"{Fore.GREEN}密码: {password}{Style.RESET_ALL}")
        
        # 保存账号信息
        save_2925_account(email_name, password)
        
        return True
        
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} 注册失败: {str(e)}{Style.RESET_ALL}")
        return False
    finally:
        if 'page' in locals():
            page.quit()

def custom_2925_email(translator=None):
    """Login with existing 2925.com email account"""
    try:
        # 获取用户输入
        print(f"{Fore.CYAN}{EMOJI['INFO']} 请输入已有的@2925邮箱账号信息：{Style.RESET_ALL}")
        while True:
            email_name = input(f"{Fore.CYAN}邮箱名 (不需要输入@2925.com): {Style.RESET_ALL}")
            if not email_name:
                print(f"{Fore.RED}{EMOJI['ERROR']} 邮箱名不能为空{Style.RESET_ALL}")
                continue
            if not all(c.isalnum() for c in email_name):
                print(f"{Fore.RED}{EMOJI['ERROR']} 邮箱名只能包含字母和数字{Style.RESET_ALL}")
                continue
            break

        while True:
            password = input(f"{Fore.CYAN}密码: {Style.RESET_ALL}")
            if not password:
                print(f"{Fore.RED}{EMOJI['ERROR']} 密码不能为空{Style.RESET_ALL}")
                continue
            break

        # 创建浏览器选项
        co = ChromiumOptions()
        co.set_argument("--incognito")
        co.set_argument("--disable-gpu")
        co.set_argument("--no-sandbox")
        co.set_argument("--disable-dev-shm-usage")
        
        # 创建浏览器实例
        page = ChromiumPage(co)
        
        print(f"{Fore.CYAN}{EMOJI['INFO']} 正在访问2925.com...{Style.RESET_ALL}")
        page.get("https://www.2925.com/login/")
        time.sleep(3)  # 等待页面加载
        
        # 输入账号
        account_input = page.ele("#ipt_account")
        if account_input:
            account_input.input(email_name)
            time.sleep(1)
        
        # 输入密码
        password_input = page.ele("#ipt_password")
        if password_input:
            password_input.input(password)
            time.sleep(1)
        
        # 勾选用户协议
        try:
            checkboxes = page.eles("css:ins.iCheck-helper")
            for checkbox in checkboxes:
                checkbox.click()
                time.sleep(0.5)
        except Exception as e:
            print(f"{Fore.YELLOW}{EMOJI['WARN']} 勾选协议失败，尝试其他方式: {str(e)}")
            try:
                checkboxes = page.eles("css:div.icheckbox_minimal-grey")
                for checkbox in checkboxes:
                    checkbox.click()
                    time.sleep(0.5)
            except:  # noqa: E722
                pass
        
        # 点击登录按钮
        login_button = page.ele("#btn_login")
        if login_button:
            login_button.click()
            time.sleep(3)
        
        # 检查是否登录成功
        try:
            # 尝试访问邮件列表页面
            page.get("https://www.2925.com/#/mailList")
            time.sleep(3)
            
            # 如果能访问到邮件列表，说明登录成功
            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 登录成功！{Style.RESET_ALL}")
            print(f"{Fore.GREEN}邮箱地址: {email_name}@2925.com{Style.RESET_ALL}")
            
            # 保存账号信息（覆盖之前的信息）
            save_2925_account(email_name, password)
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} 登录失败，请检查账号密码是否正确{Style.RESET_ALL}")
            raise e
        
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} 登记失败: {str(e)}{Style.RESET_ALL}")
        return False
    finally:
        if 'page' in locals():
            page.quit()

def read_2925_account():
    """Read 2925 email account information"""
    try:
        if not os.path.exists("2925_accounts.txt"):
            return None, None
            
        with open("2925_accounts.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) < 2:
                return None, None
                
            email = lines[0].strip().split(": ")[1].replace("@2925.com", "")
            password = lines[1].strip().split(": ")[1]
            return email, password
    except Exception:
        return None, None

def save_auto_use_setting(use_auto=True):
    """Save auto-use setting"""
    try:
        with open("auto_use_2925.txt", "w", encoding="utf-8") as f:
            f.write("yes" if use_auto else "no")
    except Exception:
        pass

def check_auto_use_setting():
    """Check if auto-use is enabled"""
    try:
        if not os.path.exists("auto_use_2925.txt"):
            return None
        with open("auto_use_2925.txt", "r", encoding="utf-8") as f:
            content = f.read().strip()
            return content == "yes"
    except Exception:
        return None

class CursorRegistration:
    def __init__(self, translator=None):
        self.translator = translator
        self.auth = CursorAuth()
        self.faker = Faker()
        self.config = get_config()
        
        # 创建必要的目录
        create_required_directories()
        
        # 检查Chrome安装
        chrome_path = check_chrome_installation()
        if not chrome_path:
            print(f"{Fore.RED}{EMOJI['ERROR']} Chrome浏览器未安装或未找到，请安装Chrome后重试{Style.RESET_ALL}")
            sys.exit(1)
            
        # 设置配置文件
        if not self.config.has_section('Browser'):
            self.config.add_section('Browser')
            self.config.set('Browser', 'chrome_path', chrome_path)
            self.config.set('Browser', 'download_path', 'downloads')
            self.config.set('Browser', 'user_data_path', 'user_data')
            self.config.set('Browser', 'cache_path', 'cache')
            with open('config.ini', 'w') as f:
                self.config.write(f)
        
        # Set to display mode
        os.environ['BROWSER_HEADLESS'] = 'False'
        self.browser = None
        self.controller = None
        self.sign_up_url = "https://authenticator.cursor.sh/sign-up"
        self.settings_url = "https://www.cursor.com/settings"
        self.email_address = None
        self.signup_tab = None
        self.email_tab = None
        
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
            
            # 先登录邮箱
            print(f"{Fore.CYAN}{EMOJI['INFO']} 正在登录邮箱...{Style.RESET_ALL}")
            verification_page.get("https://www.2925.com/login/")
            time.sleep(3)  # 等待页面加载
            
            # 输入账号
            account_input = verification_page.ele("#ipt_account")
            if account_input:
                account_input.input("chnanan72")
                time.sleep(1)
            
            # 输入密码
            password_input = verification_page.ele("#ipt_password")
            if password_input:
                password_input.input("mzxgfwlpt00")
                time.sleep(1)
            
            # 勾选用户协议
            try:
                checkboxes = verification_page.eles("css:ins.iCheck-helper")
                for checkbox in checkboxes:
                    checkbox.click()
                    time.sleep(0.5)
            except Exception as e:
                print(f"{Fore.YELLOW}{EMOJI['WARN']} 勾选协议失败，尝试其他方式: {str(e)}")
                try:
                    # 尝试直接点击包含复选框的div
                    checkboxes = verification_page.eles("css:div.icheckbox_minimal-grey")
                    for checkbox in checkboxes:
                        checkbox.click()
                        time.sleep(0.5)
                except:  # noqa: E722
                    pass
            
            # 点击登录按钮
            login_button = verification_page.ele("#btn_login")
            if login_button:
                login_button.click()
                time.sleep(3)
            
            # 访问邮件列表
            print(f"{Fore.CYAN}{EMOJI['INFO']} 正在访问邮件列表...{Style.RESET_ALL}")
            verification_page.get("https://www.2925.com/#/mailList")
            time.sleep(5)  # 增加等待时间确保页面加载完成
            
            # 查找并点击验证邮件
            max_attempts = 10
            verification_code = None
            
            for attempt in range(max_attempts):
                print(f"{Fore.CYAN}{EMOJI['INFO']} 正在查找验证邮件，第 {attempt + 1} 次尝试...{Style.RESET_ALL}")
                
                try:
                    # 直接查找验证邮件标题
                    verify_emails = verification_page.eles("css:.mail-content-title")
                    for email in verify_emails:
                        if "Verify your email address" in email.text:
                            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 找到验证邮件{Style.RESET_ALL}")
                            email.click()
                            time.sleep(3)
                            
                            # 提取验证码
                            code_element = verification_page.ele("css:div[style*='font-family:-apple-system'][style*='font-size:28px']")
                            if code_element:
                                code = code_element.text.strip()
                                if code.isdigit() and len(code) == 6:
                                    verification_code = code
                                    print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 验证码获取成功: {code}{Style.RESET_ALL}")
                                    return verification_code
                            break
                
                except Exception as e:
                    print(f"{Fore.YELLOW}{EMOJI['WARN']} 查找邮件时出错: {str(e)}")
                
                if not verification_code:
                    print(f"{Fore.YELLOW}{EMOJI['WAIT']} 未找到验证邮件，等待刷新...{Style.RESET_ALL}")
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
                verification_page.quit()

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
                    except:  # noqa: E722
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
                except:  # noqa: E722
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

    def handle_2925_email_setup(self):
        """Handle 2925 email setup process"""
        # 检查是否启用了自动使用
        auto_use = check_auto_use_setting()
        
        # 读取已保存的账号信息
        email, password = read_2925_account()
        
        if email and password:
            if auto_use is None:
                # 首次发现账号信息，询问是否自动使用
                print(f"{Fore.CYAN}{EMOJI['INFO']} 发现已保存的2925邮箱账号：{email}@2925.com{Style.RESET_ALL}")
                while True:
                    choice = input(f"{Fore.CYAN}是否自动使用此账号？(y/n): {Style.RESET_ALL}").lower()
                    if choice in ['y', 'n']:
                        save_auto_use_setting(choice == 'y')
                        if choice == 'y':
                            print(f"{Fore.CYAN}{EMOJI['INFO']} 已设置自动使用此账号{Style.RESET_ALL}")
                            return self.verify_and_setup_email(email, password)
                        break
                    print(f"{Fore.RED}{EMOJI['ERROR']} 请输入 y 或 n{Style.RESET_ALL}")
            elif auto_use:
                # 已启用自动使用
                print(f"{Fore.CYAN}{EMOJI['INFO']} 自动使用已保存的账号：{email}@2925.com{Style.RESET_ALL}")
                return self.verify_and_setup_email(email, password)
        
        # 如果没有账号信息或选择不自动使用，让用户选择操作
        print(f"{Fore.CYAN}{EMOJI['INFO']} 请选择操作：{Style.RESET_ALL}")
        print("1. 注册新的2925邮箱 (第18项功能)")
        print("2. 登录已有2925邮箱 (第19项功能)")
        
        while True:
            choice = input(f"{Fore.CYAN}请输入选项 (1/2): {Style.RESET_ALL}")
            if choice == "1":
                return setup_email(self.translator)
            elif choice == "2":
                return custom_2925_email(self.translator)
            print(f"{Fore.RED}{EMOJI['ERROR']} 请输入 1 或 2{Style.RESET_ALL}")

    def verify_and_setup_email(self, email, password):
        """Verify and setup email for Cursor registration"""
        try:
            # 创建浏览器选项
            co = ChromiumOptions()
            co.set_argument("--incognito")
            co.set_argument("--disable-gpu")
            co.set_argument("--no-sandbox")
            co.set_argument("--disable-dev-shm-usage")
            
            # 创建浏览器实例
            page = ChromiumPage(co)
            
            print(f"{Fore.CYAN}{EMOJI['INFO']} 正在验证2925邮箱...{Style.RESET_ALL}")
            page.get("https://www.2925.com/login/")
            time.sleep(3)
            
            # 输入账号
            account_input = page.ele("#ipt_account")
            if account_input:
                account_input.input(email)
                time.sleep(1)
            
            # 输入密码
            password_input = page.ele("#ipt_password")
            if password_input:
                password_input.input(password)
                time.sleep(1)
            
            # 勾选用户协议
            try:
                checkboxes = page.eles("css:ins.iCheck-helper")
                for checkbox in checkboxes:
                    checkbox.click()
                    time.sleep(0.5)
            except Exception as e:
                print(f"{Fore.YELLOW}{EMOJI['WARN']} 勾选协议失败，尝试其他方式: {str(e)}")
                try:
                    checkboxes = page.eles("css:div.icheckbox_minimal-grey")
                    for checkbox in checkboxes:
                        checkbox.click()
                        time.sleep(0.5)
                except:
                    pass
            
            # 点击登录按钮
            login_button = page.ele("#btn_login")
            if login_button:
                login_button.click()
                time.sleep(3)
            
            # 检查是否登录成功
            try:
                # 尝试访问邮件列表页面
                page.get("https://www.2925.com/#/mailList")
                time.sleep(3)
                
                # 生成1-1000之间的随机数（不包含1-7）
                valid_numbers = list(range(8, 1001))
                random_number = random.choice(valid_numbers)
                
                # 组合邮箱名 - 这个用于Cursor注册
                cursor_email_name = f"{email}{random_number}"
                
                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 2925邮箱验证成功！{Style.RESET_ALL}")
                print(f"{Fore.GREEN}2925邮箱地址: {email}@2925.com{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Cursor将使用的邮箱地址: {cursor_email_name}@2925.com{Style.RESET_ALL}")
                
                # 设置邮箱地址用于后续注册
                self.email_address = f"{cursor_email_name}@2925.com"
                return True
                
            except Exception as e:
                print(f"{Fore.RED}{EMOJI['ERROR']} 登录失败，请检查账号密码是否正确: {str(e)}{Style.RESET_ALL}")
                # 登录失败时删除自动使用设置
                if os.path.exists("auto_use_2925.txt"):
                    os.remove("auto_use_2925.txt")
                return False
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} 验证失败: {str(e)}{Style.RESET_ALL}")
            return False
        finally:
            if 'page' in locals():
                page.quit()

    def start(self):
        """Start Registration Process"""
        try:
            if self.handle_2925_email_setup():
                if self.register_cursor():
                    print(f"\n{Fore.GREEN}{EMOJI['DONE']} {self.translator.get('register.cursor_registration_completed')}...{Style.RESET_ALL}")
                    return True
            return False
        finally:
            if hasattr(self, 'temp_email'):
                try:
                    self.temp_email.close()
                except:
                    pass

    def update_cursor_auth(self, email=None, access_token=None, refresh_token=None, auth_type="Auth_0"):
        """Convenient function to update Cursor authentication information"""
        auth_manager = CursorAuth(translator=self.translator)
        return auth_manager.update_auth(email, access_token, refresh_token, auth_type)

def main(translator=None):
    """Main function to be called from main.py"""
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{EMOJI['START']} {translator.get('register.title')}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

    registration = CursorRegistration(translator)
    registration.start()

    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    input(f"{EMOJI['INFO']} {translator.get('register.press_enter')}...")

if __name__ == "__main__":
    from main import translator as main_translator
    main(main_translator) 