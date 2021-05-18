# -*- coding: UTF-8 -*-
import requests
import subprocess
import os
import time



def download(folder_name,name,video_url,audio_url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'referer': 'https://www.bilibili.com/v/technology/finance/'
    }

    #判断存储路径是否存在
    path = 'F:/bili/download/'+folder_name
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)

    # 视频下载
    response_video = requests.get(url=video_url, headers=headers)
    name_video_ori = name + 'ori.mp4'
    name_video = path + '/' + name_video_ori
    with open(name_video, 'wb') as f:
        f.write(response_video.content)
        f.close()
        print(name_video_ori +'  下载完成')

    # 音频下载
    response_audio = requests.get(url=audio_url, headers=headers)
    name_audio_ori = name + 'ori.mp3'
    name_audio = path + '/' + name_audio_ori
    with open(name_audio, 'wb') as f:
        f.write(response_audio.content)
        f.close()
        print(name_audio_ori +'  下载完成')

    # 音、视频文件合成
    print('音、视频正在合成')
    path2 = path+'/'+name_video_ori
    path3 = path+'/'+name_audio_ori
    path4 = path+'/'+name
    COMMAND = f'ffmpeg -i {path2} -i {path3} -c:v copy -c:a aac -strict experimental {path4}.mp4'
    subprocess.Popen(COMMAND, shell=True)
    print(path4 +'   合成完成!')

    # 删除过程文件
    print('正在删除过程文件！！！')
    time.sleep(15)
    os.remove(path2)
    os.remove(path3)



# a = '【FFmpeg分P教学】转码、压制、录屏、裁切、合并、提取…统统不是问题。'
# b = '合并分割'
# c = 'https://upos-sz-mirrorkodo.bilivideo.com/upgcxcode/95/45/290474595/290474595_nb2-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1621310653&gen=playurlv2&os=kodobv&oi=3085305924&trid=e638eb8401e14ce1be87379740e54b7du&platform=pc&upsig=ca3427986ee88092a8d2aa3da4b61612&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&orderid=1,3&agrr=1&logo=40000000'
# d = 'https://upos-sz-mirrorkodo.bilivideo.com/upgcxcode/95/45/290474595/290474595_nb2-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1621310653&gen=playurlv2&os=kodobv&oi=3085305924&trid=e638eb8401e14ce1be87379740e54b7du&platform=pc&upsig=66d5de01ff274fda22e5357c3a0e8ba8&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&orderid=0,3&agrr=1&logo=80000000'
#
# download(a,b,c,d)










