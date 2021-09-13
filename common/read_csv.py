# -*- coding:utf-8 -*-
# @Time    : 2021/9/9 14:05
# @Author  : Wei Yu  J
# @File    : read_csv.py
# ***********************
def read_csv_data(csv_file):
    """
    读取yaml文件数据
    :param csv_file:yaml文件地址
    :return:
    """
    import csv
    with open(csv_file,'r',encoding="UTF-8") as f:
        reader = csv.reader(f)
        data = list(reader)
        return data


