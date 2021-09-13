# -*- coding:utf-8 -*-
# @Time    : 2021/2/1
# @Author  : Leo Zhang
# @File    : startup.py
# ***********************
import os
import sys
import pytest
import logging


if __name__ == '__main__':
    from common import writeLogs
    from config import *

    # 开启日志记录(默认logs目录)
    writeLogs.MyLogs(ROOT_DIR+'logs')

    # 定义运行参数
    args_list = ['-vs', TEST_DIR,
                 '-n', str(RC['process']),
                 '--reruns', str(RC['reruns']),
                 '--maxfail', str(RC['maxfail']),
                 '--alluredir', REPORT_DIR+'/xml',
                 '--clean-alluredir']
    # 判断是否开启用例匹配
    if RC['pattern']:
        args_list += ['-k ' + str(RC['pattern'])]
    test_result = pytest.main(args_list)

    # 生成allure报告
    cmd = 'allure generate --clean %s -o %s ' % (REPORT_DIR+'/xml', REPORT_DIR+'/html')
    os.system(cmd)
