import os
from common.readyaml import read_yaml_data


# 获取主目录路径
ROOT_DIR = str(os.path.realpath(__file__)).split('config')[0].replace('\\', '/')

# 获取配置文件路径
API_CONFIG = ROOT_DIR+'config/apiConfig.yaml'
RUN_CONFIG = ROOT_DIR+'config/runConfig.yaml'


# 获取运行配置信息
RC = read_yaml_data(RUN_CONFIG)
INTERVAL = RC['interval']
PROJECT_NAME = RC['project_name']

# 获取项目信息配置
AC =  read_yaml_data(API_CONFIG)
HOST = AC[PROJECT_NAME]['host']
HEADER = AC[PROJECT_NAME]['header']
COOKIES = AC[PROJECT_NAME]['cookies']




# 测试数据目录(test.yaml)
PAGE_DIR = ROOT_DIR+PROJECT_NAME+'/page'
# 测试脚本目录(test.py)
TEST_DIR = ROOT_DIR+PROJECT_NAME+'/testcase'
# 测试报告目录(xml|html)
REPORT_DIR = ROOT_DIR+PROJECT_NAME+'/report'
# 参数化数据目录
PARAM_DIR = ROOT_DIR+PROJECT_NAME +'/contract'