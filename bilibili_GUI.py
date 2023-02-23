from tkinter import *
import os
import you_get
# import time
# import threading
# from tkinter import filedialog
# from you_get import common
# import sys


# import jindutiao


class myWindow:
    # 定义构造函数，绘制窗体及控件
    def __init__(self, master=None):
        self.master = master
        self.master.wm_title('十元Download')
        self.master.geometry('300x200')
        self.createWidgets()

        # 定义绘制控件函数

    def createWidgets(self):
        label = Label(self.master)
        label['text'] = '视频地址'
        label['font'] = 14
        label.grid(row=0, column=0)
        self.entry_name = Entry(self.master)
        self.entry_name.grid(row=0, column=1)

        label = Label(self.master)
        label['text'] = '开始集数'
        label['font'] = 14
        label.grid(row=1, column=0)
        self.entry_start = Entry(self.master)
        self.entry_start.grid(row=1, column=1)

        label = Label(self.master)
        label['text'] = '结束集数'
        label['font'] = 14
        label.grid(row=2, column=0)
        self.entry_stop = Entry(self.master)
        self.entry_stop.grid(row=2, column=1)

        label = Label(self.master)
        label['text'] = '保存地址'
        label['font'] = 14
        label.grid(row=3, column=0)
        self.entry_directory = Entry(self.master)
        self.entry_directory.grid(row=3, column=1)

        btn_reset = Button(self.master)
        btn_reset['text'] = '浏览'
        # btn_reset['font']=125
        # btn_reset['padx']=15
        btn_reset['fg'] = 'black'
        btn_reset['bg'] = 'white'
        btn_reset['command'] = self.folder
        btn_reset.grid(row=3, column=2)

        btn_log = Button(self.master)
        btn_log['text'] = '下载'
        btn_log['font'] = 14
        btn_log['fg'] = 'yellow'
        btn_log['bg'] = 'green'
        btn_log['padx'] = 15
        btn_log['command'] = self.toLogin
        btn_log.grid(row=4, column=0)
        '''
        btn_reset=Button(self.master)
        btn_reset['text']='下载进程'
        btn_reset['font']=14
        btn_reset['padx']=15
        btn_reset['fg']='white'
        btn_reset['bg']='green'
        btn_reset['command']=self.toReset
        btn_reset.grid(row=4,column=1)
        '''

    # 定义点击按钮回调函数
    def toLogin(self):
        self.name = self.entry_name.get()  # 获取文本输入框的get方法
        # return name
        self.url_num_start = self.entry_start.get()
        self.url_num_stop = self.entry_stop.get()
        self.directory = self.entry_directory.get()
        print("调用了toLogin")
        download(self.name, self.url_num_start, self.url_num_stop, self.directory)
        '''
        if self.name=='admin' and self.pwd=='admin':
            print('welcome to my app, dear'+self.name)
        else:
            print('your information is error!')
        '''

    def toReset(self):
        print(you_get.jindutiao.get_date)
        '''
        self.entry_name.delete(0,END)  #清空输入框内容使用delete方法
        self.entry_pwd.delete(0,END)
        '''

    def folder(self):
        root1 = Tk()
        root1.withdraw()
        Folderpath = filedialog.askdirectory()
        print(Folderpath)
        self.entry_directory.delete(0, "end")
        self.entry_directory.insert(0, Folderpath)


class download:
    # print("111")
    def __init__(self, name, url_num_start, url_num_stop, directory):
        self.url = name
        self.url_num_start = url_num_start
        self.url_num_stop = url_num_stop
        self.directory = directory
        self.bilibili()
        print("成功调用download")
        print(self.url_num_start)

    def down_bilibili(self, save_dir, url, num):
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        os.system("you-get --no-caption -o " + save_dir + " " + url + str(num))

    def bilibili(self):
        print("调用bilibili")
        # url=name
        url = self.url[0:self.url.index("?")]
        for i in range(int(self.url_num_start), int(self.url_num_stop) + 1):
            self.down_bilibili(self.directory, f'{url}?p=', i)
        # print(url)
        # time.sleep(3)
        # url_num_start = int(input("请输入开始集数："))
        # url_num_stop=int(input("请输入结束集数："))
        # directory=input("请输入视频保存路径：")
        '''
        #多线程下载
        thread_num = 8
        thread_list = []
        thread_list1 = []
        for i in range(int(self.url_num_start), int(self.url_num_stop) + 1):
            # 为每个新URL创建下载线程
            # url = url_seed + str(i)
            t = threading.Thread(target=self.down_bilibili, args=(self.directory, url + "?p=", i))
            # 加入线程池并启动
            thread_list.append(t)
            thread_list1.append(t)
            t.start()

            # print(thread_list[0])

            # 当线程池满时，等待线程结束
            while len(thread_list) > thread_num:
                # 移除已结束线程
                thread_list = [x for x in thread_list if x.is_alive()]
                # print("下载完成")
                time.sleep(1)
                # print("running threads_________" + str(thread_list))

            pass
        '''


# 实例化一个窗体及控件组合
if __name__ == "__main__":
    root = Tk()
    UserLogWindow = myWindow(root)
    root.mainloop()
