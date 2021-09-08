import string
import random
import datetime
from dateutil.relativedelta import relativedelta
from faker import Faker



def random_str(str_len):
    """
    从a-zA-Z0-9生成指定数量的随机字符
    :param str_len: 字符串长度
    :return:
    """
    try:
        str_len = int(str_len)
    except ValueError:
        raise Exception("调用随机字符失败，[ %s ]长度，参数有误" %str_len)
    strings = ''.join(random.sample(string.hexdigits,+str_len))
    return strings

def random_int(scope):
    """
    获取所及整数数据
    :param scope: 数据范围
    :return:
    """
    # try:
    #     start_num, end_num =scope.split(",")
    #     start_num = int(start_num)
    #     end_num = int(end_num)
    # except ValueError:
    #     raise Exception("调用随机整数失败，[ %s ]范围参数有误" %scope)
    # if start_num <= end_num:
    #     number = random.randint(start_num, end_num)
    # else:
    #     number = random.randint(end_num, start_num)
    # return number
    fake = Faker("zh_CN")
    try:
        start_num, end_num =scope.split(",")
        start_num = int(start_num)
        end_num = int(end_num)
    except ValueError:
        raise Exception("调用随机整数失败，[ %s ]范围参数有误" %scope)
    if start_num <= end_num:
        number = fake.random_int(min=start_num,max=end_num)
    else:
        number = fake.random_int(min=end_num,max=start_num)
    return number



def random_float(data):
    """
    获取随机浮点数据
    :param data: 数组
    :return:
    """
    try:
        start_num, end_num, accuracy = data.split(",")
        start_num = int(start_num)
        end_num = int(end_num)
        accuracy = int(accuracy)
    except ValueError:
        raise Exception("调用随机浮点数失败，[%s]范围参数或精度有无" %data)
    if start_num <= end_num:
        number = random.uniform(start_num, end_num)
    else:
        number = random.uniform(end_num, start_num)
    number = round(number, accuracy)
    return number

def random_choice(data):
    """
    获取数组随机值
    :param data: 数组
    :return:
    """
    _list = data.split(",")
    ench = random.choice(_list)
    return ench

def get_date_mark(now, mark, num):
    if 'y' == mark:
        return now + relativedelta(years=num)
    elif 'm' == mark:
        return now + relativedelta(months=num)
    elif 'd' == mark:
        return now + relativedelta(days=num)
    elif 'h' == mark:
        return now + relativedelta(hours=num)
    elif 'M' == mark:
        return now + relativedelta(minutes=num)
    elif 's' == mark:
        return now + relativedelta(seconds=num)
    else:
        raise Exception("日期字段标识错误[%s],请使用[年y,月m,日d,时h,分M,秒s]标识"%mark)

def generate_date(expr=''):
    """
    生成日期对象（不含时分秒）
    :param expr: 日期表达式，如"d-1"代表日期减1
    :return:
    """
    today = datetime.date.today()
    if expr:
        try:
            mark = expr[:1]
            num = int(expr[1:])
        except (TypeError, NameError):
            raise Exception("调用生成日期失败，日期表达式[ %s ]有误" %expr)
        return get_date_mark(today, mark, num)
    else:
        return today

def genrate_datetime(expr=''):
    """
    生成日期时间对象（含时分秒）
    :param expr: 日期表达式，如"d-1"代表日期减1
    :return:
    """
    now = datetime.datetime.now().replace(microsecond=0)
    if expr:
        try:
            mark = expr[:1]
            num = expr[1:]
        except (TypeError, NameError):
            raise Exception("调用生成日期失败，日期表达式[%s]有无"%expr)
        return get_date_mark(now,mark,num)
    else:
        return now

def generate_timestamp(expr=''):
    """
    生成时间戳
    :param expr: 日期表达式。如“d-1”代表日期减1
    :return:
    """
    datatime_obj = generate_timestamp(expr)
    return int(datetime.datetime.timestamp(datatime_obj)) * 1000

def genrate_guid():
    """
    基于MAC地址+时间戳+随机数来生成GUID
    :return:
    """
    import uuid
    return str(uuid.uuid1()).upper()

def generate_wxid():
    """
    基于AUTO标识+26位英文字母大小写+ 数字生成伪微信ID
    :return:
    """
    return 'AUTO' + ''.join(random.sample(string.ascii_letters + string.digits,24))

def genrate_noid(expr=''):
    """
    基于6位随机数字+出生日期+4位随机数生成伪身份证
    :param expr:
    :return:
    """
    # birthday = generate_date(expr)
    # birthday = str(birthday).replace('-','')
    # return int(str(random.randint(100000, 999999)) + birthday + str(random.randint(1000,9999)))

    fake = Faker("zh_CN")
    return fake.ssn(min_age=18, max_age=90)

def generate_phone():
    """
    基于三大运营商号段+随机数生成伪手机号
    :return:
    """
    fake = Faker("zh_CN")
    return  fake.phone_number()


if __name__ == '__main__':
    print(generate_phone())
    print(random_int("100,200"))
    print(random_int("200,100"))
