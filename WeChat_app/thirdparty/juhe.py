import json, time
import requests


def weather(CityName):
    """
    :param CityName: 城市名字
    :return: 返回实时天气
    """
    key = 'c8fc9a2cd8831b4b862c717064fbd79a'
    api = 'http://v.juhe.cn/weather/index'
    params = 'cityname=%s&key=%s' % (CityName, key)
    url = api + '?' + params
    # print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    # print(json_data)
    result = json_data.get('result')
    sk = result.get('sk')
    response = dict()
    response['temperature'] = sk.get('temp')  # 天气
    response['wind_direction'] = sk.get('wind_direction')  # 风向
    response['wind_strength'] = sk.get('wind_strength')  # 风的强度
    response['humidity'] = sk.get('humidity')  # 湿度
    response['time'] = sk.get('time')  # 当前时间
    print(response)
    return response


def joke(page, pagesize):
    """

    :param page: 返回几页
    :param pagesize: 返回几条
    :return: 返回笑话
    """
    key = 'f1956f725c237b265928531a3b0f416a'
    api = 'http://v.juhe.cn/joke/content/list.php'
    timestamp = '%.f' % time.time()

    pass


if __name__ == '__main__':
    data = weather('朝阳')
    # import time
    #
    # print('%.f' % time.time())
