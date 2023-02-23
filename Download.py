import tkinter as tk
import os
import you_get
from tkinter import filedialog

class basedesk:
    def __init__(self, master):
        self.root = master
        self.root.title('Download')
        self.root.geometry('300x200')

        self.initface = tk.Frame(self.root)
        self.initface.pack()
        bilibili = tk.Button(self.initface, text='Bilibili', command=self.bilibili_callback).grid(row=0, column=0)

        Tencent = tk.Button(self.initface, text='腾讯视频', command=self.bilibili_callback).grid(row=0, column=1)

    def bilibili_callback(self):
        self.initface.destroy()
        Bilibili(self.root)

class Bilibili:
    def __init__(self, master):
        self.master = master

        self.face = tk.Frame(self.master)
        self.createWidgets()
        # bilibili = tk.Button(self.master, text='abababa', ).grid(row=0, column=0)

    def createWidgets(self):
        label = tk.Label(self.master)
        label['text'] = '视频地址'
        label['font'] = 14
        label.grid(row=0, column=0)
        self.entry_name = tk.Entry(self.master)
        self.entry_name.grid(row=0, column=1)

        label = tk.Label(self.master)
        label['text'] = '开始集数'
        label['font'] = 14
        label.grid(row=1, column=0)
        self.entry_start = tk.Entry(self.master)
        self.entry_start.grid(row=1, column=1)

        label = tk.Label(self.master)
        label['text'] = '结束集数'
        label['font'] = 14
        label.grid(row=2, column=0)
        self.entry_stop = tk.Entry(self.master)
        self.entry_stop.grid(row=2, column=1)

        label = tk.Label(self.master)
        label['text'] = '保存地址'
        label['font'] = 14
        label.grid(row=3, column=0)
        self.entry_directory = tk.Entry(self.master)
        self.entry_directory.grid(row=3, column=1)

        btn_reset = tk.Button(self.master)
        btn_reset['text'] = '浏览'
        # btn_reset['font']=125
        # btn_reset['padx']=15
        btn_reset['fg'] = 'black'
        btn_reset['bg'] = 'white'
        btn_reset['command'] = self.folder
        btn_reset.grid(row=3, column=2)

        btn_log = tk.Button(self.master)
        btn_log['text'] = '下载'
        btn_log['font'] = 14
        btn_log['fg'] = 'yellow'
        btn_log['bg'] = 'green'
        btn_log['padx'] = 15
        btn_log['command'] = self.toLogin
        btn_log.grid(row=4, column=0)

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
        root1 = tk.Tk()
        root1.withdraw()
        Folderpath = tk.filedialog.askdirectory()
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



if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()
