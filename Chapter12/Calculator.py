import wx


class MyFrame(wx.Frame):
    # 构造方法
    pos_x = 10
    pos_y = 70
    button_w = 50
    button_h = 50
    def __init__(self):
        # 创建窗口
        wx.Frame.__init__(self, None, title="Calculator", pos=(100, 100), size=(400, 500))
        # 创建面板
        self.panel = wx.Panel(self,pos=(100, 100),size=(500, 800))
        # 创建文本框
        self.entry = wx.TextCtrl(self.panel, pos=(10, 10), size=(400, 50),style = wx.TE_RIGHT)
        # 创建按钮

        # 第一行
        self.button_clear = wx.Button(self.panel, label="C", pos=(self.pos_x, self.pos_y),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_div = wx.Button(self.panel, label="/", pos=(self.pos_x + 60, self.pos_y),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_mul = wx.Button(self.panel, label="*", pos=(self.pos_x + 120, self.pos_y),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_back = wx.Button(self.panel, label="<-", pos=(self.pos_x + 180, self.pos_y),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)


        # 第二行
        self.button_7 = wx.Button(self.panel, label="7", pos=(self.pos_x, self.pos_y + 60),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_8 = wx.Button(self.panel, label="8", pos=(self.pos_x + 60, self.pos_y + 60),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_9 = wx.Button(self.panel, label="9", pos=(self.pos_x + 120, self.pos_y + 60),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_sub = wx.Button(self.panel, label="-", pos=(self.pos_x + 180, self.pos_y + 60),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)


        # 第三行
        self.button_4 = wx.Button(self.panel, label="4", pos=(self.pos_x, self.pos_y + 120),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_5 = wx.Button(self.panel, label="5", pos=(self.pos_x + 60, self.pos_y + 120),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_6 = wx.Button(self.panel, label="6", pos=(self.pos_x + 120, self.pos_y + 120),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_add = wx.Button(self.panel, label="+", pos=(self.pos_x + 180, self.pos_y + 120),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)


        # 第四行
        self.button_1 = wx.Button(self.panel, label="1", pos=(self.pos_x, self.pos_y + 180),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_2 = wx.Button(self.panel, label="2", pos=(self.pos_x + 60, self.pos_y + 180),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_3 = wx.Button(self.panel, label="3", pos=(self.pos_x + 120, self.pos_y + 180),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)
        self.button_eq = wx.Button(self.panel, label="=", pos=(self.pos_x + 180, self.pos_y + 180),
                                    size=(self.button_w, self.button_h + 60), style=wx.BU_AUTODRAW)

        # 第五行
        self.button_0 = wx.Button(self.panel, label="0", pos=(self.pos_x, self.pos_y + 240),
                                  size=(self.button_w + 60, self.button_h), style=wx.BU_AUTODRAW)
        self.button_point = wx.Button(self.panel, label=".", pos=(self.pos_x + 120, self.pos_y + 240),
                                  size=(self.button_w, self.button_h), style=wx.BU_AUTODRAW)

        # 绑定按钮对应的事件
        self.Bind(wx.EVT_BUTTON, self.On_button_clear, self.button_clear)
        self.Bind(wx.EVT_BUTTON, self.On_button_eq, self.button_eq)
        self.Bind(wx.EVT_BUTTON, self.On_button_back, self.button_back)
        self.Bind(wx.EVT_BUTTON, self.On_button_sub, self.button_sub)
        self.Bind(wx.EVT_BUTTON, self.On_button_add, self.button_add)
        self.Bind(wx.EVT_BUTTON, self.On_button_mul, self.button_mul)
        self.Bind(wx.EVT_BUTTON, self.On_button_div, self.button_div)
        self.Bind(wx.EVT_BUTTON, self.On_button_9, self.button_9)
        self.Bind(wx.EVT_BUTTON, self.On_button_8, self.button_8)
        self.Bind(wx.EVT_BUTTON, self.On_button_7, self.button_7)
        self.Bind(wx.EVT_BUTTON, self.On_button_6, self.button_6)
        self.Bind(wx.EVT_BUTTON, self.On_button_5, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.On_button_4, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.On_button_3, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.On_button_2, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.On_button_1, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.On_button_0, self.button_0)
        self.Bind(wx.EVT_BUTTON, self.On_button_point, self.button_point)
    def On_button_clear(self, event):
        self.entry.Clear()
    def On_button_eq(self, event):
        text = self.entry.GetValue()
        result = eval(text)
        self.entry.SetValue(str(result))
    def On_button_back(self, event):
        text = self.entry.GetValue()
        self.entry.SetValue(text[:-1])
    def On_button_sub(self, event):
        self.entry.AppendText("-")
    def On_button_add(self, event):
        self.entry.AppendText("+")
    def On_button_mul(self, event):
        self.entry.AppendText("*")
    def On_button_div(self, event):
        self.entry.AppendText("/")
    def On_button_9(self, event):
        self.entry.AppendText("9")
    def On_button_8(self, event):
        self.entry.AppendText("8")
    def On_button_7(self, event):
        self.entry.AppendText("7")
    def On_button_6(self, event):
        self.entry.AppendText("6")
    def On_button_5(self, event):
        self.entry.AppendText("5")
    def On_button_4(self, event):
        self.entry.AppendText("4")
    def On_button_3(self, event):
        self.entry.AppendText("3")
    def On_button_2(self, event):
        self.entry.AppendText("2")
    def On_button_1(self, event):
        self.entry.AppendText("1")
    def On_button_0(self, event):
        self.entry.AppendText("0")
    def On_button_point(self, event):
        self.entry.AppendText(".")
if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()
    # 创建窗口
    frame = MyFrame()
    # 显示窗口
    frame.Show()
    # 一直显示
    app.MainLoop()
