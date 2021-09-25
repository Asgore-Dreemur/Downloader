import os
import sys
import tkinter as tk
from tkinter import filedialog as fd

import requests
import win32api
import win32con
from threading import Thread


class PyWinDesign:
    def __init__(self, startwin):
        def download():
            self.bq3btx2x = tk.StringVar()
            self.bq3btx2x.set('正在连接,请稍后...')
            self.bq3x2x = tk.Label(self.startwin, textvariable=self.bq3btx2x, anchor=tk.W)
            self.bq3x2x.place(x=25, y=105, width=100, height=22)
            self.bt2.config(state="disabled")
            self.bq1.config(state="disabled")
            chunk_size = 1024
            bj1get = self.bj1.get()
            bj2get = self.bj2.get()
            bj3get = self.bj3.get()
            if len(bj1get) == 0:
                win32api.MessageBox(0, "URL不能为空!", "提示", win32con.MB_ICONWARNING)
                self.bt2.config(state="normal")
                self.bq1.config(state="normal")
                self.bq3x2x.destroy()
                return 0
            elif len(bj2get) == 0:
                win32api.MessageBox(0, "保存路径不能为空!", "提示", win32con.MB_ICONWARNING)
                self.bt2.config(state="normal")
                self.bq1.config(state="normal")
                self.bq3x2x.destroy()
                return 0
            elif len(bj3get) == 0:
                win32api.MessageBox(0, "保存文件名不能为空!", "提示", win32con.MB_ICONWARNING)
                self.bt2.config(state="normal")
                self.bq1.config(state="normal")
                self.bq3x2x.destroy()
                return 0
            else:
                pass
            save = os.path.exists(bj2get)
            if not save:
                win32api.MessageBox(0, "指定的目录不存在!", "提示", win32con.MB_ICONWARNING)
                self.bt2.config(state="normal")
                self.bq1.config(state="normal")
                self.bq3x2x.destroy()
                return 0
            else:
                pass
            if bj1get[0:5] == "http:":
                pass
            else:
                print(bj1get[0:5])
                win32api.MessageBox(0, "链接错误!", "提示", win32con.MB_ICONWARNING)
                self.bt2.config(state="normal")
                self.bq1.config(state="normal")
                self.bq3x2x.destroy()
                return 0
            try:
                requests.get(bj1get)
            except:
                win32api.MessageBox(0, "无法访问这个网站!", "提示", win32con.MB_ICONWARNING)
                self.bt2.config(state="normal")
                self.bq1.config(state="normal")
                self.bq3x2x.destroy()
                return 0
            fileexits = os.path.exists(bj2get + "/" + bj3get)
            if fileexits:
                win32api.MessageBox(0, "目录下包含同名文件!", "提示", win32con.MB_ICONWARNING)
                self.bt2.config(state="normal")
                self.bq1.config(state="normal")
                self.bq3x2x.destroy()
                return 0
            # 请求头
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE '
            }
            file_name = bj2get + "/" + bj3get
            # 发起 head 请求，即只会获取响应头部信息
            head = requests.head(bj1get, headers=headers, stream=True)
            # 文件大小，以 B 为单位
            try:
                file_size = head.headers['Content-Length']
                file_size = int(file_size)
                filezize = file_size / 1024 / 1024
                self.bq3btx2 = tk.StringVar()
                self.bq3btx2.set('文件大小:%dM' % filezize)
                self.bq3x2 = tk.Label(self.startwin, textvariable=self.bq3btx2, anchor=tk.W)
                self.bq3x2.place(x=25, y=105, width=100, height=22)
            except:
                win32api.MessageBox(0, "无法下载这个文件!", "提示", win32con.MB_ICONWARNING)
                self.bq3x2x.destroy()
                self.bt2.config(state="normal")
                self.bq1.config(state="normal")
                return 0
            fill_line = self.jd1.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            raise_data = 200 / (file_size / chunk_size)
            if file_size is not None:
                int(file_size)
            response = requests.get(bj1get, headers=headers, stream=True)
            # 一块文件的大小
            try:
                with open(file_name, mode='wb') as f:
                    self.bq3x2x.destroy()
                    n = 0
                    # 写入分块文件
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        f.write(chunk)
                        n = n + raise_data
                        self.jd1.coords(fill_line, (0, 0, n, 60))
                        self.startwin.update()
            except PermissionError:
                win32api.MessageBox(0, "权限不足!", "提示", win32con.MB_ICONWARNING)
                self.bq3x2x.destroy()
                self.bt2.config(state="normal")
                self.bq1.config(state="normal")
                return 0

            fill_line = self.jd1.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
            x = 500
            n = 600 / x
            for t in range(x):
                n = n + 600 / x
                self.jd1.coords(fill_line, (0, 0, n, 60))
                self.startwin.update()
            self.bt2.config(state="normal")
            self.bq1.config(state="normal")
            self.bq3x2.destroy()
            win32api.MessageBox(0, "下载完成!", "提示", win32con.MB_ICONQUESTION)

        def resource_path(relative_path):
            if getattr(sys, 'frozen', False):  # 是否Bundle Resource
                base_path = sys._MEIPASS
            else:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)

        root.iconphoto(False, tk.PhotoImage(file=resource_path(os.path.join("config", "Download.png"))))

        def browserfile():
            path = fd.askdirectory(title="选择下载路径")
            self.bj2nr.set(path)

        def downloadfile():
            th1 = Thread(target=download, args=())
            th1.start()

        self.startwin = startwin
        self.startwin.title('O5-3下载器')
        self.startwin.resizable(width=False, height=False)
        screenwidth = self.startwin.winfo_screenwidth()
        screenheight = self.startwin.winfo_screenheight()
        size = '%dx%d+%d+%d' % (333, 208, (screenwidth - 333) / 2, (screenheight - 208) / 2)
        self.startwin.geometry(size)

        self.bq1bt = tk.StringVar()
        self.bq1bt.set('下载URL:')
        self.bq1 = tk.Label(self.startwin, textvariable=self.bq1bt, anchor=tk.W)
        self.bq1.place(x=10, y=16, width=50, height=19)

        self.bj1nr = tk.StringVar()
        self.bj1nr.set("")
        self.bj1 = tk.Entry(self.startwin, textvariable=self.bj1nr, justify=tk.LEFT)
        self.bj1.place(x=66, y=15, width=172, height=20)

        self.bq2bt = tk.StringVar()
        self.bq2bt.set('保存路径:')
        self.bq2 = tk.Label(self.startwin, textvariable=self.bq2bt, anchor=tk.W)
        self.bq2.place(x=10, y=44, width=54, height=22)

        self.bj2nr = tk.StringVar()
        self.bj2nr.set("")
        self.bj2 = tk.Entry(self.startwin, textvariable=self.bj2nr, justify=tk.LEFT)
        self.bj2.place(x=73, y=46, width=163, height=20)

        self.bq1bt = tk.StringVar()
        self.bq1bt.set('浏览')
        self.bq1 = tk.Button(self.startwin, textvariable=self.bq1bt, command=browserfile)
        self.bq1.place(x=244, y=42, width=56, height=27)

        self.bq3bt = tk.StringVar()
        self.bq3bt.set('保存的文件名:')
        self.bq3 = tk.Label(self.startwin, textvariable=self.bq3bt, anchor=tk.W)
        self.bq3.place(x=7, y=77, width=79, height=22)

        self.bj3nr = tk.StringVar()
        self.bj3nr.set("")
        self.bj3 = tk.Entry(self.startwin, textvariable=self.bj3nr, justify=tk.LEFT)
        self.bj3.place(x=97, y=77, width=117, height=20)

        self.bt2bt = tk.StringVar()
        self.bt2bt.set('下载')
        self.bt2 = tk.Button(self.startwin, textvariable=self.bt2bt, command=downloadfile)
        self.bt2.place(x=233, y=172, width=83, height=27)

        self.jd1 = tk.Canvas(startwin, width=200, height=16, bg="white")
        self.jd1.place(x=70, y=130)

        self.bq3btx = tk.StringVar()
        self.bq3btx.set('进度:')
        self.bq3x = tk.Label(self.startwin, textvariable=self.bq3btx, anchor=tk.W)
        self.bq3x.place(x=25, y=130, width=50, height=22)

        self.bq3btxx = tk.StringVar()
        self.bq3btxx.set('不支持https下载,请将https改成http')
        self.bq3xx = tk.Label(self.startwin, textvariable=self.bq3btxx, anchor=tk.W)
        self.bq3xx.place(x=25, y=170, width=200, height=22)


if __name__ == '__main__':
    root = tk.Tk()
    app = PyWinDesign(root)
    root.mainloop()
