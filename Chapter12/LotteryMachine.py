import wx
import random


class MyFrame(wx.Frame):
    # 抽奖列表
    Namelist = ['mia', 'tom', 'jack']

    # 构造方法
    def __init__(self):
        wx.Frame.__init__(self, None, title="抽奖器",pos=(200,100),size = (400,600))
        # 创建面板
        self.panel = wx.Panel(self,pos = (200,100),size=(400,600))
        # 设置背景颜色
        # self.SetBackgroundColour(wx.BLUE)
        # self.SetBackgroundColour('blue')
        # self.SetBackgroundStyle((255,255,0))
        self.SetBackgroundColour('#00FF00')
        # 创建静态文本
        self.staticText = wx.StaticText(self.panel, label="欢迎使用抽奖器",pos=(50,50),size=(30,30),style=wx.TE_CENTER)
        # 创建字体
        # 字体大小，字体包，字体风格，加粗
        font = wx.Font(30, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
        self.staticText.SetFont(font)
        # 设置静态文本字体
        # 创建按钮
        self.buttonStart = wx.Button(self.panel, label="开始抽奖", pos=(80, 300))
        self.buttonEnd = wx.Button(self.panel, label="结束抽奖", pos=(250, 300))
        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.onClick, self.buttonStart)
        self.Bind(wx.EVT_BUTTON, self.offClick, self.buttonEnd)

    def onClick(self, event):
        # self.staticText.SetLabelText(random.choice(MyFrame.Namelist))
        self.timer = wx.Timer(self)  # 创建一个定时器
        self.Bind(wx.EVT_TIMER, self.updateName, self.timer)
        self.timer.Start(10)

    def offClick(self, event):
        self.timer.Stop()

    def updateName(self, event):
        self.staticText.SetLabelText(random.choice(MyFrame.Namelist))


if __name__ == '__main__':  # python程序的主入口
    # 创建应用程序对象
    app = wx.App()
    # 创建窗口
    frame = MyFrame()
    # 显示窗口
    frame.Show()
    # 让窗口一直显示
    app.MainLoop()
