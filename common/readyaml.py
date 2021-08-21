
def read_yaml_data(yaml_file):
    """
    读取yaml文件数据
    :param yaml_file:yaml文件地址
    :return:
    """
    import yaml
    with open(yaml_file,'r',encoding="UTF-8") as f:
        return yaml.load(f,Loader=yaml.SafeLoader)


def write_yaml_file(yaml_file,obj):
    """
    把对象写入yaml文件
    :param yaml_file: yaml文件地址
    :param obj: 数据对象
    :return:
    """
    from ruamel import yaml
    with open(yaml_file,'w',encoding='utf-8') as fw:
        yaml.dump(obj,fw,Dumper=yaml.RoundTripDumper,allow_unicode=True)