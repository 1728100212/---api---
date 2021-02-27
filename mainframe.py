import telnetlib
import json
import urllib.request
import wx
from tkinter import *

from tkinter.messagebox import *

class LoginPage(Frame):

    def __init__(self):

        super().__init__()

        self.username = StringVar()

        self.password = StringVar()

        self.pack()

        self.createForm()

    def createForm(self):

        Label(self).grid(row=0, stick=W, pady=10)

        Label(self, text='账户: ').grid(row=1, stick=W, pady=10)

        Entry(self, textvariable=self.username).grid(row=1, column=1, stick=E)

        Label(self, text='密码: ').grid(row=2, stick=W, pady=10)

        Entry(self, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)

        Button(self, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)

        Button(self, text='退出', command=self.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):

        name = self.username.get()

        secret = self.password.get()

        if name == '123' and secret == '123':


            ChatFrame.zhu_fra(self)

            # MainPage()

        else:

            showinfo(title='错误', message='账号或密码错误！')

            # print('账号或密码错误！')
class ChatFrame(wx.Frame):
    """
    聊天窗口    """

    def __init__(self, parent, id, title, size):
        # 初始化，添加控件并绑定事件
        wx.Frame.__init__(self, parent, id, title)
        self.SetSize(size)
        self.Center()
        self.chatFrame = wx.TextCtrl(self, pos=(5, 5), size=(490, 310), style=wx.TE_MULTILINE | wx.TE_READONLY)
        #self.sayButton = wx.Button(self, label="Say", pos=(5, 320), size=(58, 25))
        self.message = wx.TextCtrl(self, pos=(5, 320), size=(298, 25), style=wx.TE_PROCESS_ENTER)
        self.sendButton = wx.Button(self, label="Send", pos=(310, 320), size=(58, 25))
        self.cleanButton = wx.Button(self, label="clean", pos=(373, 320), size=(58, 25))
        self.closeButton = wx.Button(self, label="Close", pos=(436, 320), size=(58, 25))
        self.sendButton.Bind(wx.EVT_BUTTON, self.send)  # 发送按钮绑定发送消息方法
        self.message.SetFocus()  # 输入框回车焦点
        #self.sayButton.Bind(wx.EVT_LEFT_DOWN, self.sayDown)  # SAY按钮按下
        # self.sayButton.Bind(wx.EVT_LEFT_UP, self.sayUp)  # Say按钮弹起
        self.Bind(wx.EVT_TEXT_ENTER, self.send, self.message)  # 回车发送消息
        self.cleanButton.Bind(wx.EVT_BUTTON, self.clean)  # Users按钮绑定获取在线用户数量方法
        self.closeButton.Bind(wx.EVT_BUTTON, self.close)  # 关闭按钮绑定关闭方法
        # treceive = threading.Thread(target=self.receive)  # 接收信息线程
        # treceive.start()
        # self.ShowFullScreen(True)  # 全屏
        self.Show()

    def sayDown(self, event):
    # trecording = threading.Thread(target=recording)
    # trecording.start()
        self.chatFrame.AppendText('系统提示：语音系统还在内测'+ '\n')
    # def sayUp(self, event):
    # sayText = getText(r"E:\Python_Doc\voice_say\say_voice.wav")
    # self.message.AppendText(str(sayText))
    # self.send(self)
    def send(self, event):
        message = str(self.message.GetLineText(0)).strip()
        self.chatFrame.AppendText('我：' + message + '\n')
        self.static_chat()
        self.chatFrame.AppendText('图灵：' +self.static_chat()+ '\n')
        self.message.Clear()
        return message
    def getit(self):
        return str(self.message.GetLineText(0)).strip()
    def clean(self, event):
        # 查看当前在线用户
        self.chatFrame.Clear()
    def close(self, event):
        con.close()
        self.Close()
    def static_chat(self):
        api_url = "http://openapi.tuling123.com/openapi/api/v2"
        text_input =self.getit()
        req = {
            "perception":
                {
                    "inputText":
                        {
                            "text": text_input
                        },

                    "selfInfo":
                        {
                            "location":
                                {
                                    "city": "南京",
                                    "province": "南京",
                                    "street": "栖霞区仙林街道"
                                }
                        }
                },

            "userInfo":
                {
                    "apiKey": "4086b58c01f94c3f99b219888b611b23",
                    "userId": "27853ac53e35fa01"
                }
        }
        # print(req)
        # 将字典格式的req编码为utf8
        req = json.dumps(req).encode('utf8')
        # print(req)

        http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)
        response_str = response.read()#.decode('utf8')
        # print(response_str)
        response_dic = json.loads(response_str)
        print(response_dic)

        intent_code = response_dic['intent']['code']
        results_text = response_dic['results'][0]['values']['text']
        print('Turing的回答：')
        print('code：' + str(intent_code))
        print('text：' + results_text)
        return results_text
    def zhu_fra(self):
        app = wx.App()
        con = telnetlib.Telnet()
        ChatFrame(None, -1, title="聊天室", size=(520, 390))
        app.MainLoop()
if __name__ == '__main__':
    root = Tk()

    root.title('登陆界面')

    width = 280

    height = 200

    screenwidth = root.winfo_screenwidth()

    screenheight = root.winfo_screenheight()

    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

    root.geometry(alignstr)  # 居中对齐

    page1 = LoginPage()

    root.mainloop()
