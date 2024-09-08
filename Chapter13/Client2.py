import wx
from socket import *
import threading
from faker import Faker

class Client(wx.Frame):
    def __init__(self):
        # 实例属性
        self.name = Faker('zh_CN').name()  # 客户端名字
        self.isConnected = False  # 客户端是否链接服务器
        self.client_socket = None

        # 界面布局
        wx.Frame.__init__(self, None, title=self.name + "聊天室客户端", pos=(100, 100), size=(450, 600))
        # 创建面板
        self.panel = wx.Panel(self)
        # 创建按钮
        # 加入聊天室
        self.conn_btn = wx.Button(self.panel, label='加入聊天室', pos=(10, 10), size=(200, 40))
        # 离开聊天室
        self.dis_conn_btn = wx.Button(self.panel, label='离开聊天室', pos=(220, 10), size=(200, 40))
        # 清空按钮
        self.clear_btn = wx.Button(self.panel, label='清空', pos=(10, 500), size=(200, 40))
        # 发送按钮
        self.send_btn = wx.Button(self.panel, label='发送', pos=(220, 500), size=(200, 40))
        # 创建聊天内容文本框
        self.text = wx.TextCtrl(self.panel, size=(420, 300), pos=(10, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        # 创建输入文本框
        self.input_text = wx.TextCtrl(self.panel,size=(420, 120), pos=(10, 370), style=wx.TE_MULTILINE)
        # 按钮的事件绑定
        self.Bind(wx.EVT_BUTTON, self.conn,self.conn_btn)
        self.Bind(wx.EVT_BUTTON, self.disConn, self.dis_conn_btn)
        self.Bind(wx.EVT_BUTTON, self.clear, self.clear_btn)
        self.Bind(wx.EVT_BUTTON, self.send, self.send_btn)
    # 点击 加入聊天室 按钮触发
    def conn(self, event):
        print("conn")
        if self.isConnected == False:
            self.isConnected = True
            self.client_socket = socket()
            self.client_socket.connect(('127.0.0.1',8080))
            # 发送用户名
            self.client_socket.send(self.name.encode('utf-8'))
            # 创建线程
            main_thread = threading.Thread(target=self.recv_data)
            # 设置为守护线程
            main_thread.daemon = True
            # 启动线程
            main_thread.start()

    def recv_data(self):
        while self.isConnected:
            text = self.client_socket.recv(1024).decode('utf-8')
            self.text.AppendText(text+'\n')

    # 点击 离开聊天室 按钮触发
    def disConn(self, event):
        print("disConn")
        self.client_socket.send('断开连接'.encode('utf-8'))
        self.isConnected = False
    # 点击 清空 按钮触发
    def clear(self, event):
        print("clear")
        self.input_text.Clear()
    # 点击 发送 按钮触发
    def send(self, event):
        print("send")
        if self.isConnected:
            text = self.input_text.GetValue()
            if text != '':
                self.client_socket.send(text.encode('utf-8'))
                self.input_text.Clear()


if __name__ == '__main__':
    # 创建应用程序的对象
    app = wx.App()
    # 创建客户端窗口
    client = Client()

    # 显示客户端窗口
    client.Show()

    # 一直循环显示
    app.MainLoop()
