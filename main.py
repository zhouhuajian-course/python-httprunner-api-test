"""
运行所有测试用例

@author  : zhouhuajian
@version : v1.0
"""

import pytest
import time
import os

if __name__ == '__main__':
    # 根目录
    root_dir = os.path.dirname(__file__)
    # 年月日_时分秒
    datetime = time.strftime("%Y%m%d_%H%M%S")
    # 测试报告目录
    report_dir = f"{root_dir}/reports/{datetime}"
    # print(datetime, root_dir, report_dir)
    # exit()
    pytest.main([
        f'--html={report_dir}/report.html',
        '--self-contained-html',
        f'--alluredir={report_dir}/allure_result',
        f'{root_dir}/testcases'
    ])
    os.system(f"allure generate --report-dir {report_dir}/allure_report {report_dir}/allure_result")