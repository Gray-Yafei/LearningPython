import wx
class MyFrame(wx.Frame):
    # 构造方法
    def __init__(self):
        wx.Frame.__init__(self, None, title="My Frame", size=(500, 400))
        # 创建面板
        panel = wx.Panel(self)
        # 创建静态文本
        staticText = wx.StaticText(panel, label="Hello World")
        # 创建按钮
        button = wx.Button(panel, label="Click Me!", pos=(100, 100))

# 创建应用程序对象
app = wx.App()
# 创建窗口
frame = MyFrame()
# 显示窗口
frame.Show()
# 让窗口一直显示
app.MainLoop()
