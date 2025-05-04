import json
import os

class Translator:
    def __init__(self):
        self.translations = {}
        self.load_translations()
        
    def load_translations(self):
        """加载翻译文件"""
        try:
            locale_path = os.path.join('locales', 'zh_cn.json')
            if os.path.exists(locale_path):
                with open(locale_path, 'r', encoding='utf-8') as f:
                    self.translations = json.load(f)
        except Exception as e:
            print(f"Warning: Failed to load translations: {e}")
            
    def get(self, key, **kwargs):
        """获取翻译文本"""
        try:
            # 按点分割键
            parts = key.split('.')
            value = self.translations
            
            # 遍历字典层级
            for part in parts:
                value = value[part]
                
            # 如果是字符串，进行格式化
            if isinstance(value, str):
                return value.format(**kwargs)
            return value
        except (KeyError, AttributeError):
            return key  # 如果找不到翻译，返回原始键 