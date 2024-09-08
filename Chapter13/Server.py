import wx
from socket import *
import threading
from concurrent.futures import ThreadPoolExecutor

class Server(wx.Frame):
    def __init__(self):
        # 实例属性
        self.isOn = False  # 服务器的启动状态
        # 创建socket对象
        self.server_socket = socket()
        # 绑定ip和端口号
        self.server_socket.bind(('0.0.0.0', 8080))
        # 监听
        self.server_socket.listen(5)
        # 保存所有的客户端
        self.client_thread_dict={}
        # 创建线程池
        self.pool = ThreadPoolExecutor(max_workers=10)

        # 界面布局
        # 调用父类的init()方法
        wx.Frame.__init__(self,None,title="多人聊天室",pos = (0,50),size = (450,600))
        # 创建面板
        self.panel = wx.Panel(self)
        # 创建按钮
        #启动服务器
        self.start_server_button = wx.Button(self.panel,pos=(10,10),size=(200,40),label = "启动服务器")
        #保存聊天记录
        self.save_text_button = wx.Button(self.panel, pos=(220, 10), size=(200, 40), label="保存聊天记录")
        # 创建聊天内容文本框
        self.text = wx.TextCtrl(self.panel, size=(420, 300), pos=(10, 60), style=wx.TE_READONLY | wx.TE_MULTILINE)
        # 按钮的事件绑定
        self.Bind(wx.EVT_BUTTON, self.start_server,self.start_server_button)
        self.Bind(wx.EVT_BUTTON, self.save_text, self.save_text_button)

    def start_server(self,event):
        print("start server")
        if self.isOn == False:
            self.isOn = True
            # 创建线程
            main_thread = threading.Thread(target=self.main_thread_fun)
            # 设置为守护线程
            main_thread.daemon = True
            # 启动线程
            main_thread.start()
    def main_thread_fun(self):
        while self.isOn:
            client_socket, client_addr = self.server_socket.accept()
            print(client_addr)
            client_name = client_socket.recv(1024).decode('utf-8')
            print(client_name)
            client_thread = ClientThread(client_socket, client_name,self)
            # 保存到客户端
            self.client_thread_dict[client_name] = client_thread
            self.pool.submit(client_thread.run)
            self.send('【服务器通知】欢迎%s进入聊天室'%client_name)
    def send(self,text):
        self.text.AppendText(text + '\n')
        for client in self.client_thread_dict.values():
            if client.isOn:
                client.client_socket.send(text.encode('utf-8'))
    def save_text(self,event):
        print("save text")
        record = self.text.GetValue()
        with open("record.log",'a+',encoding='GBK') as f:
            f.write(record)

class ClientThread(threading.Thread):
    def __init__(self,socket,name,server):
        threading.Thread.__init__(self)
        self.client_socket = socket
        self.client_name = name
        self.server = server
        self.isOn = True
    def run(self):
        while self.isOn:
            text = self.client_socket.recv(1024).decode('utf-8')
            if text == '断开连接':
                self.isOn = False
                self.server.send('【服务器通知】%s离开了聊天室' % self.client_name)
            else:
                self.server.send('【%s】%s'%(self.client_name,text))
        self.client_socket.close()

# 程序的入口
if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()
    # 创建服务器窗口
    server = Server()
    # 显示服务器窗口
    server.Show()
    # 循环显示
    app.MainLoop()
