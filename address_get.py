# -*- coding: UTF-8 -*-
import requests
import re
import json



def address(name_code):
    url = 'https://www.bilibili.com/video/{}'.format(name_code)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'

    }
    response = requests.get(url=url,headers=headers)
    file_name = re.findall(r'"part":"(.*?)","duration"',response.content.decode())
    content = re.findall(r'<script>window.__playinfo__=(.*?)</script>',response.content.decode())
    cont = json.loads(content[0])
    video_url = cont['data']['dash']['video'][0]['backupUrl'][0]
    audio_url = cont['data']['dash']['audio'][0]['baseUrl']
    return(file_name,video_url,audio_url)


# model = address('BV1Ft411s7Xa')
# print(model)
