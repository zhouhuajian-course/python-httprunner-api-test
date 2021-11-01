"""
测试PyTest对测试用例标准输出和标准错误的捕获
测试PyTest参数化

@author  : zhouhuajian
@version : v1.0
"""

import sys
import pytest
import csv


# def test_add():
#     """测试加法"""
#     print("这是标准输出", file=sys.stdout)
#     print("这是标准错误", file=sys.stderr)
#     assert 1 + 2 == 3

# def test_add():
#     assert 1 + 2 == 3
# #
# def test_add2():
#     assert 2 + 3 == 5
# #
# def test_add3():
#     assert 3 + 4 == 7





# @pytest.mark.parametrize("num1, num2, sum", [
#     (1, 2, 3), (2, 3, 5), (3, 4, 7)
# ])
# def test_add(num1, num2, sum):
#     assert num1 + num2 == sum


@pytest.mark.parametrize("param", [
    {"num1": 1, "num2": 2, "sum": 3},
    {"num1": 2, "num2": 3, "sum": 5},
    {"num1": 3, "num2": 4, "sum": 7}
])
def test_add(param):
    assert param['num1'] + param['num2'] == param['sum']

#
# with open("test_add.csv", mode="r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     data = list(reader)
# @pytest.mark.parametrize("param", data)
# def test_add(param):
#     assert int(param['num1']) + int(param['num2']) == int(param['sum'])

