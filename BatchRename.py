#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "HQ"

import os,shutil,re

path_wav = "D:\Music\KuGou\wav"
path_mp3 = "D:\Music\KuGou\mp3"


wav_list = os.listdir(path_wav)
mp3_list = os.listdir(path_mp3)
mp3_dict = {}
replace_dict = {}


# 按照原文件名重命名目标文件
# for song_mp3 in mp3_list:
#     temp_list = song_mp3.split("_")
#     del temp_list[2]
#     temp_mp3 = "_".join(temp_list) + ".mp3"
#     mp3_dict[temp_mp3] = song_mp3
#
# for song_war in wav_list:
#     song_war1 = song_war.lower().replace('.wav', '.mp3')
#
#     if song_war1 in mp3_dict:
#         replace_dict[mp3_dict[song_war1]] = song_war.replace('.wav', '.mp3')
#     else:
#         print(song_war1)
# print(mp3_dict)
# print(replace_dict)


# 去掉文件名指定的前缀
prefix_str = "DY_"
for song_mp3 in mp3_list:
    if re.match(prefix_str, song_mp3):
        replace_dict[song_mp3] = song_mp3.replace(prefix_str, "")


for key in replace_dict.keys():
    # print("%s\%s" % (path_mp3, key), "%s\%s" % (path_mp3, replace_dict[key]))
    shutil.move("%s\%s" % (path_mp3, key), "%s\%s" % (path_mp3, replace_dict[key]))
