# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:29:52 2022

@author: 78033
"""
import os
import you_get
import time
import threading

def down_bilibili(save_dir, url, episode_start, episode_end):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    try:
        for i in range(episode_start, episode_end+1):
            os.system("you-get -o "+save_dir+" "+url + str(i))
        print("视频下载成功")
    except Exception as e:
        print("视频下载失败")

def down_bilibili1(save_dir, url, num):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    os.system("you-get -o "+save_dir+" "+url + str(num))

if __name__ =="__main__":
    #down_bilibili("F:\视频", "https://www.bilibili.com/video/BV1DW411x7GB?p=", 1, 5)
    url=input("请输入视频地址：")
    url=url[0:url.index("?")]
    #print(url)
    #time.sleep(3)
    url_num_start = int(input("请输入开始集数："))
    url_num_stop=int(input("请输入结束集数："))
    directory=input("请输入视频保存路径：")
    thread_num = 8
    thread_list = []
    for i in range(url_num_start,url_num_stop+1):
        #为每个新URL创建下载线程
        #url = url_seed + str(i)
        t = threading.Thread(target=down_bilibili1, args=(directory,url+"?p=", i))
        #加入线程池并启动
        thread_list.append(t)
        t.start()
        
        #print(thread_list[0])

        #当线程池满时，等待线程结束
        while len(thread_list)>thread_num:  
            #移除已结束线程
            thread_list = [x for x in thread_list if x.is_alive()]
            time.sleep(1)
            # print("running threads_________" + str(thread_list))

        pass
    
#you_get.common.main()