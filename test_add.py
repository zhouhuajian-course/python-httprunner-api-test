"""
测试Pytest对测试用例标准输出和标准错误的捕获

@author  : zhouhuajian
@version : v1.0
"""

import sys


def test_add():
    """测试加法"""
    print("这是标准输出", file=sys.stdout)
    print("这是标准错误", file=sys.stderr)
    assert 1 + 2 == 3
