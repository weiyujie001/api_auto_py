# -*- coding:utf-8 -*-
# @Time    : 2021/9/9 13:38
# @Author  : Wei Yu  J
# @File    : BaseApi.py
# ***********************

class global_variable():
    global_dict = {}

    @classmethod
    def set_value(cls,key,value):
        """
        设置全局变量
        :param key:
        :param value:
        :return:
        """
        cls.global_dict[key] = value

    @classmethod
    def get_value(cls,key,defValue=None):
        """ 获得一个全局变量,不存在则返回默认值 """
        if key  in cls.global_dict.keys():
            return cls.global_dict[key]
        else:
            return None