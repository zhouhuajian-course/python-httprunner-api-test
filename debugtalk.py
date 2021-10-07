"""
自定义Python函数

@author  : zhouhuajian
@version : v1.0
"""

import sys

# 假设Windows下运行测试环境
# 在Linux下运行生产环境
if sys.platform == "win32":
    base_url = "http://127.0.0.1:5000"
    # base_url = "http://localhost:5000"
else:
    base_url = "https://zhouhuajian.com"


def get_base_url():
    """获取基础URL"""
    return base_url


if __name__ == '__main__':
    print(get_base_url())