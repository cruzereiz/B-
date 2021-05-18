# -*- coding: UTF-8 -*-
import subprocess


# 可以合成
# COMMAND = f'ffmpeg -i 合并分割ori.mp4 -i 合并分割ori.mp3 -c:v copy -c:a aac -strict experimental 02下载、配置.mp4'
# subprocess.Popen(COMMAND,shell=True)


p1 = r'F:\bili\download\【FFmpeg分P教学】转码、压制、录屏、裁切、合并、提取…统统不是问题。\合并分割ori'
p2 = r'F:\bili\download\【FFmpeg分P教学】转码、压制、录屏、裁切、合并、提取…统统不是问题。\合并分割ori'
p3 = r'F:\bili\download\【FFmpeg分P教学】转码、压制、录屏、裁切、合并、提取…统统不是问题。\合并分割'

COMMAND = f'ffmpeg -i {p1}.mp4 -i {p2}.mp3 -c:v copy -c:a aac -strict experimental {p3}.mp4'
subprocess.Popen(COMMAND,shell=True)
