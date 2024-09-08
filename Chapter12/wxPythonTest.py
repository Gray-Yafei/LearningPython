import wx

def onClick(event):
    print("按钮被点击了")

# 创建应用程序的对象
app = wx.App()
# 创建窗口（最底层，so None）
# size:宽，高  pos:(左上角)x坐标，y坐标
frame = wx.Frame(None,size=(600,800),pos=(0,0),title='Hello World')
# 显示窗口
frame.Show()

# 创建面板(在窗口上面创建)
panel = wx.Panel(frame,size=(400,400),pos=(10,10))
# 显示面板
panel.Show()

# 创建一个静态文本
staticText = wx.StaticText(panel,label='欢迎学习python',pos=(200,200))
# 显示静态文本
staticText.Show()

# 创建按钮
button = wx.Button(panel, label = '测试')
# 显示按钮
button.Show()
# 给按钮绑定事件
frame.Bind(wx.EVT_BUTTON, onClick, button)

# 进入主循环，让窗口一直显示
app.MainLoop()