"""
运行所有测试用例

@author  : zhouhuajian
@version : v1.0
"""

import pytest
import time

if __name__ == '__main__':
    # 年月日_时分秒
    datetime = time.strftime("%Y%m%d_%H%M%S")
    # 测试报告目录
    report_dir = f"reports/{datetime}"
    # print(datetime, report_dir)
    # exit()
    pytest.main([
        f'--html={report_dir}/report.html',
        '--self-contained-html',
        'testcases'
    ])
