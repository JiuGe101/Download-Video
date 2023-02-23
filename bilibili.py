
#import sys
import you_get
import os
import time

url = input("请输入视频地址：")
directory=input("请输入视频保存路径：")

#sys.argv=["you-get", "-o",directory,url]
#print(directory)
print("you-get -o"+" "+directory +" --format=dash-flv"+" "+url)
os.system("you-get -o"+" "+directory +" --format=dash-flv"+" "+url)
time.sleep(5)