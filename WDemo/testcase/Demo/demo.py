# -*- coding:utf-8 -*-
# @Time    : 2021/9/9 13:46
# @Author  : Wei Yu  J
# @File    : Demo.py
# ***********************
import os
from pprint import pprint

import allure
import pytest

from common.readyaml import read_yaml_data
from common.read_csv import read_csv_data
from config import PARAM_DIR

case_yaml = os.path.realpath(__file__).replace('testcase', 'page').replace('.py', '.yaml')
case_contract_path = os.path.dirname(__file__).replace('testcase', 'contract')
case_path = os.path.dirname(case_yaml)
case_dict = read_yaml_data(case_yaml)



def a(case_dict):
    # if "parameters" in case_dict["test_info"]:
    #     test_data = case_dict["test_info"]
    #     print(test_data)
    #     parameters = test_data["parameters"]
    #     print(parameters)
    #     for key  in parameters.keys():
    #         print(key)
    #         var = key.split("-")
    #         print(var)
    #         contract = read_csv_data(case_csv_path)
    #         print(contract)
    #         contract = contract[1:]
    #         print(contract)
    print(case_contract_path)
    print("--------------------")
    list_data = []
    test_request = case_dict["test_case"]
    print(test_request)
    for i in test_request:
        print(i)
        request_data = i['request']
        print(request_data)

        list_data.append(request_data)
        print(list_data)
        chck_body = i['check_body']
        print(chck_body)
        return list_data


if __name__ == '__main__':
    a(case_dict)



@allure.feature(case_dict["test_info"]["title"])
class TestPerrelated:

    @pytest.mark.parametrize("case_data", case_dict["test_case"])
    @allure.story("test_addAudltCard")
    def test_addAudltCard(self, case_data):
        # 初始化请求：执行前置接口+替换关联变量
        test_info, case_data = init_premise(case_dict["test_info"], case_data, case_path)
        # 发送当前接口
        code, contract = send_request(test_info, case_data)
        # 校验接口返回
        check_result(case_data, code, contract)



