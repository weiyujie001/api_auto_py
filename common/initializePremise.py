import json
import logging
from json import JSONDecodeError
from api.BaseApi import global_variable
import re

from common.read_csv import read_csv_data


def read_json(summary,json_obj,case_path):
    """
    校验内容读取
    :param summary: 用例名称
    :param json_obj: json 文件或数据对象
    :param case_path: case路径
    :return:
    """
    if isinstance(json_obj, dict):
        return json_obj
    else:
        try:
            # 读取json文件制定用例数据
            with open (case_path+'/'+json_obj,'r',encoding="utf-8") as js:
                data_list = json.load(js)
                for data in data_list:
                    if data['summary'] == summary:
                        return data['body']
        except FileNotFoundError:
            raise Exception("用例关联文件不在\n文件路径： %s" % json_obj)
        except JSONDecodeError:
            raise Exception("用例关联的文件有误\n文件路径： %s" % json_obj)

def init_premise(test_info, case_data, case_path):
    """
    用例前提条件执行，提取关键值
    :param test_info: 测试信息
    :param case_data: 用例数据
    :param case_path: 用例路径
    :return:
    """

    # 处理当前接口入参：获取入参-获取关联值-替换关联值
    parameter = case_data['request']
    # 判断
    try:
        if test_info["variables"]:
            variables = test_info["variables"]
            for key,value in variables.items():
                if value in global_variable.global_dict:
                    parameters = re.sub("\$\{"+key+"\}",global_variable.get_value(value),parameter)
    except Exception as e:
        logging.error("替换参数处理结果：{}".format(e))


    parameters = replaceRelevance.replace(parameter, __relevance)
    case_data['parameter'] = parameter
    logging.debug("请求参数处理结果：{}".format(parameter))

    # 获取当前接口期望结果：获取期望结果-获取关联值-替换关联值
    expected_rs = read_json(case_data['summary'], case_data['check_body']['expected_result'], case_path)
    __relevance = readRelevance.get_relevance(parameter, expected_rs, __relevance)
    expected_rs = replaceRelevance.replace(expected_rs, __relevance)
    case_data['check_body']['expected_result'] = expected_rs
    logging.debug("期望返回处理结果：{}".format(case_data))


    return test_info, case_data



def  Param_Action(case_dict, case_csv_path):
    if "parameters" in case_dict["test_info"]:
        test_data = case_dict["test_info"]
        print(test_data)
        parameters = test_data["parameters"]
        print(parameters)
        for key in parameters.keys():
            print(key)
            var = key.split("-")
            print(var)
            data = read_csv_data(case_csv_path)
            print(data)
            data = data[1:]
            print(data)
            print("--------------------")

    return data