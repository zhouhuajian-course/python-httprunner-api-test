"""
自定义Python函数

@author  : zhouhuajian
@version : v1.0
"""

import sys
import requests

# 假设Windows下运行测试环境
# 在Linux下运行生产环境
if sys.platform == "win32":
    base_url = "http://127.0.0.1:5000"
    # base_url = "http://localhost:5000"
    user = "zhouhuajian"
    pwd = "123456"
else:
    base_url = "https://zhouhuajian.com"
    user = "zhouhuajian"
    pwd = "!@#$%^"

response = requests.post(f"{base_url}/api/login", data={"user": user, "pwd": pwd})
# print(response.json())
# print(response.cookies.get("session"))
session_id = response.cookies.get("session")


def get_base_url():
    """获取基础URL"""
    return base_url


def get_session_id():
    """获取SESSION ID"""
    return session_id


if __name__ == '__main__':
    print(get_base_url())
    print(get_session_id())
