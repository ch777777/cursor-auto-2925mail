from setuptools import setup, find_packages

setup(
    name="cursor-register-tool",
    version="2.7.2",
    description="Cursor Registration Tool",
    author="Pin Studios",
    author_email="yeongpin@github.com",
    packages=find_packages(),
    install_requires=[
        'watchdog',
        'python-dotenv>=1.0.0',
        'colorama>=0.4.6',
        'requests',
        'psutil>=5.8.0',
        'DrissionPage>=4.0.0',
        'selenium',
        'webdriver_manager',
        'arabic-reshaper',
        'python-bidi',
        'faker'
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'cursor-register=main:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.json', '*.ini', '*.md', 'locales/*', 'images/*'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: Microsoft :: Windows',
    ],
) 