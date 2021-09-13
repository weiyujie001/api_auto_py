# -*- coding:utf-8 -*-
# @Time    : 2021/2/2
# @Author  : Leo Zhang
# @File    : test_Demo.py
# ****************************
import os
import allure
import pytest
from common.readyaml import read_yaml_data
from common.initializePremise import init_premise
# from common.apiSend import send_request
# from common.checkResult import check_result
case_yaml = os.path.realpath(__file__).replace('testcase', 'page').replace('.py', '.yaml')
case_path = os.path.dirname(case_yaml)
case_dict = read_yaml_data(case_yaml)
test_request = case_dict["test_case"]
print(test_request)
request_data = test_request['request']
print(request_data)

@allure.feature(case_dict["test_info"]["title"])
class TestPerrelated:

    @pytest.mark.parametrize("case_data", case_dict["test_case"])
    @allure.story("test_addAudltCard")
    def test_addAudltCard(self, case_data):
        # 初始化请求：执行前置接口+替换关联变量
        test_info, case_data = init_premise(case_dict["test_info"], case_data, case_path)
        # 发送当前接口
        # code, contract = send_request(test_info, case_data)
        # # 校验接口返回
        # check_result(case_data, code, contract)
