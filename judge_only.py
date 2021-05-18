# -*- coding: UTF-8 -*-
import requests
import re



def judge(name_code):
    url = 'https://www.bilibili.com/video/{}'.format(name_code)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'

    }
    response = requests.get(url=url,headers=headers)
    video_list = re.findall(r'"part":"(.*?)","duration"',response.content.decode())
    return video_list



# se = judge('BV17y4y127ZV')
# se = judge('BV1Ft411s7Xa')
# print(se)
