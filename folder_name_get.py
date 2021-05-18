import requests
import re



def folder_name(name_code):
    url = 'https://www.bilibili.com/video/{}'.format(name_code)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'

    }
    response = requests.get(url=url,headers=headers)
    name = re.findall(r'<h1 title="(.*?)" class="video-title">', response.content.decode())[0].replace(' ','')
    return name


# model = folder_name('BV17y4y127ZV')
# print(model)