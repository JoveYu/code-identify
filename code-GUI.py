#!/usr/bin/env python2
# −*− coding: UTF−8 −*−
#
# Author:   Jove Yu <yushijun110@gmail.com>
#

import wx, code, os
dir='./tmp/'
class Main(wx.Frame):
    def __init__(self, *args,**kwargs):
        super(Main,self).__init__(*args,**kwargs)
        self.SetSize((560,430))
        self.SetTitle('江汉大学验证码识别系统')
        self.Center()
        #放置按钮
        self.buttondown=wx.Button(self,-1,'在线下载',pos=(30,40),size=(90,25))
        self.buttonopen=wx.Button(self,-1,'本地打开',pos=(30,70),size=(90,25))
        self.button1=wx.Button(self,-1,'灰度化',pos=(30,100),size=(90,25))
        self.button2=wx.Button(self,-1,'二值化',pos=(30,130),size=(90,25))
        self.button3=wx.Button(self,-1,'去噪点',pos=(30,160),size=(90,25))
        self.button4=wx.Button(self,-1,'围点填充',pos=(30,190),size=(90,25))
        self.button5=wx.Button(self,-1,'直线填充',pos=(30,220),size=(90,25))
        self.button6=wx.Button(self,-1,'图像分割',pos=(30,250),size=(90,25))
        self.button7=wx.Button(self,-1,'统一大小',pos=(30,280),size=(90,25))
        self.button8=wx.Button(self,-1,'图像匹配',pos=(30,310),size=(90,25))
        self.buttonopendb=wx.Button(self,-1,'选择字库',pos=(30,340),size=(90,25))
        self.buttononekey=wx.Button(self,-1,'一键识别',pos=(30,370),size=(90,25))
        self.buttonsavechar1=wx.Button(self,-1,'存',pos=(170,340),size=(25,25))
        self.buttonsavechar2=wx.Button(self,-1,'存',pos=(254,340),size=(25,25))
        self.buttonsavechar3=wx.Button(self,-1,'存',pos=(338,340),size=(25,25))
        self.buttonsavechar4=wx.Button(self,-1,'存',pos=(422,340),size=(25,25))
        self.buttonsavechar5=wx.Button(self,-1,'存',pos=(503,340),size=(25,25))
        self.buttonopt=wx.ToggleButton(self,-1,'高级模式',pos=(450,370),size=(80,25))
        self.Bind(wx.EVT_BUTTON,self.Onbuttondown,self.buttondown)
        self.Bind(wx.EVT_BUTTON,self.Onbuttonopen,self.buttonopen)
        self.Bind(wx.EVT_BUTTON,self.Onbutton1,self.button1)
        self.Bind(wx.EVT_BUTTON,self.Onbutton2,self.button2)
        self.Bind(wx.EVT_BUTTON,self.Onbutton3,self.button3)
        self.Bind(wx.EVT_BUTTON,self.Onbutton4,self.button4)
        self.Bind(wx.EVT_BUTTON,self.Onbutton5,self.button5)
        self.Bind(wx.EVT_BUTTON,self.Onbutton6,self.button6)
        self.Bind(wx.EVT_BUTTON,self.Onbutton7,self.button7)
        self.Bind(wx.EVT_BUTTON,self.Onbutton8,self.button8)
        self.Bind(wx.EVT_BUTTON,self.Onbuttonopendb,self.buttonopendb)
        self.Bind(wx.EVT_BUTTON,self.Onbuttononekey,self.buttononekey)
        self.Bind(wx.EVT_BUTTON,self.Onbuttonsavechar1,self.buttonsavechar1)
        self.Bind(wx.EVT_BUTTON,self.Onbuttonsavechar2,self.buttonsavechar2)
        self.Bind(wx.EVT_BUTTON,self.Onbuttonsavechar3,self.buttonsavechar3)
        self.Bind(wx.EVT_BUTTON,self.Onbuttonsavechar4,self.buttonsavechar4)
        self.Bind(wx.EVT_BUTTON,self.Onbuttonsavechar5,self.buttonsavechar5)
        self.Bind(wx.EVT_TOGGLEBUTTON,self.Onbuttonopt,self.buttonopt)

        #静态文字
        text_url=wx.StaticText(self,-1,'网络地址：',pos=(130,43))
        text_before=wx.StaticText(self,-1,'处理前：',pos=(130,73))
        text_after=wx.StaticText(self,-1,'处理后：',pos=(330,73))
        text_db=wx.StaticText(self,-1,'字库路径：',pos=(130,373))
        text_copyright=wx.StaticText(self,-1,'Copyright © 2012 - 2013 江汉大学',pos=(278,400),size=(300,20))
        text_2=wx.StaticText(self,-1,'二值阀值：',pos=(560,130))
        text_2r=wx.StaticText(self,-1,'R',pos=(630,130))
        text_2g=wx.StaticText(self,-1,'G',pos=(680,130))
        text_2b=wx.StaticText(self,-1,'B',pos=(730,130))
        text_3=wx.StaticText(self,-1,'噪点阀值(0-5)：',pos=(560,160))
        text_6=wx.StaticText(self,-1,'分割模式',pos=(560,250))

        #文本框
        self.url=wx.TextCtrl(self,-1,'http://www.ruanko.com/validateImage.jsp',pos=(200,40),size=(330,25))
        self.db=wx.TextCtrl(self,-1,'显示字库路径',pos=(200,370),size=(250,25))
        self.char1=wx.TextCtrl(self,-1,'?',pos=(130,340),size=(25,25))
        self.char2=wx.TextCtrl(self,-1,'?',pos=(214,340),size=(25,25))
        self.char3=wx.TextCtrl(self,-1,'?',pos=(298,340),size=(25,25))
        self.char4=wx.TextCtrl(self,-1,'?',pos=(382,340),size=(25,25))
        self.char5=wx.TextCtrl(self,-1,'?',pos=(467,340),size=(25,25))
        self.opt2r=wx.TextCtrl(self,-1,'90',pos=(640,130),size=(40,25))
        self.opt2g=wx.TextCtrl(self,-1,'130',pos=(690,130),size=(40,25))
        self.opt2b=wx.TextCtrl(self,-1,'0',pos=(740,130),size=(40,25))
        self.opt3=wx.TextCtrl(self,-1,'0',pos=(670,160),size=(25,25))
        #图片
        self.image_before=wx.StaticBitmap(self,-1,pos=(200,70),size=(75,25))
        self.image_after=wx.StaticBitmap(self,-1,pos=(400,70),size=(75,25))
        self.image_big=wx.StaticBitmap(self,-1,pos=(130,100),size=(400,175))
        self.image_char1=wx.StaticBitmap(self,-1,pos=(130,280),size=(65,60))
        self.image_char2=wx.StaticBitmap(self,-1,pos=(214,280),size=(65,60))
        self.image_char3=wx.StaticBitmap(self,-1,pos=(298,280),size=(65,60))
        self.image_char4=wx.StaticBitmap(self,-1,pos=(382,280),size=(65,60))
        self.image_char5=wx.StaticBitmap(self,-1,pos=(467,280),size=(65,60))

        #选择
        self.opt6=wx.Choice(self,-1,pos=(650,250),
                choices=['混合选取','连通分割','投影分割'])

        #
        self.opt=0

    def Onbuttondown(self,event):
        text=self.url.GetValue()
        code.downcode(text)
        self.Showmes('下载完毕')
        self.Showimage('tmp.jpg','tmp.jpg')

    def Onbuttonopen(self,event):
        dlg=wx.FileDialog(
            self,message='选择一个图像文件',
            defaultDir=os.getcwd(),
            )
        if dlg.ShowModal()==wx.ID_OK:
            path=dlg.GetPath()
            code.movecode(path)
        self.Showimage('tmp.jpg','tmp.jpg')
    def Onbutton1(self,event):
        code.grey()
        self.Showimage('tmp.jpg','1.jpg')

    def Onbutton2(self,event):
        r=int(self.opt2r.GetValue())
        g=int(self.opt2g.GetValue())
        b=int(self.opt2b.GetValue())
        code.binary(r,g,b)
        self.Showimage('1.jpg','2.jpg')

    def Onbutton3(self,event):
        opt_point=int(self.opt3.GetValue())
        (num,point)=code.denoisepoint(90,opt_point)
        self.Showimage('2.jpg','3.jpg')
        self.Showmes('共扫描%d点,处理噪点%d个！'%(num,point))
    def Onbutton4(self,event):
        pass
    def Onbutton5(self,event):
        pass

    def Onbutton6(self,event):
        code.devide(0)
        if os.path.exists(dir+'char1.jpg'):
            char=wx.Bitmap(dir+'char1.jpg',wx.BITMAP_TYPE_JPEG)
            self.image_char1.SetBitmap(char)
        if os.path.exists(dir+'char2.jpg'):
            char=wx.Bitmap(dir+'char2.jpg',wx.BITMAP_TYPE_JPEG)
            self.image_char2.SetBitmap(char)
        if os.path.exists(dir+'char3.jpg'):
            char=wx.Bitmap(dir+'char3.jpg',wx.BITMAP_TYPE_JPEG)
            self.image_char3.SetBitmap(char)
        if os.path.exists(dir+'char4.jpg'):
            char=wx.Bitmap(dir+'char4.jpg',wx.BITMAP_TYPE_JPEG)
            self.image_char4.SetBitmap(char)
        if os.path.exists(dir+'char5.jpg'):
            char=wx.Bitmap(dir+'char5.jpg',wx.BITMAP_TYPE_JPEG)
            self.image_char5.SetBitmap(char)


    def Onbutton7(self,event):
        code.enlargechar()
        char1=wx.Bitmap(dir+'char1-big.jpg',wx.BITMAP_TYPE_JPEG)
        self.image_char1.SetBitmap(char1)
        char2=wx.Bitmap(dir+'char2-big.jpg',wx.BITMAP_TYPE_JPEG)
        self.image_char2.SetBitmap(char2)
        char3=wx.Bitmap(dir+'char3-big.jpg',wx.BITMAP_TYPE_JPEG)
        self.image_char3.SetBitmap(char3)
        if os.path.exists(dir+'char4-big.jpg'):
            char4=wx.Bitmap(dir+'char4-big.jpg',wx.BITMAP_TYPE_JPEG)
            self.image_char4.SetBitmap(char4)
        if os.path.exists(dir+'char5-big.jpg'):
            char5=wx.Bitmap(dir+'char5-big.jpg',wx.BITMAP_TYPE_JPEG)
            self.image_char5.SetBitmap(char5)


    def Onbutton8(self,event):
        self.char1.SetValue(code.recognize(1))
        self.char2.SetValue(code.recognize(2))
        self.char3.SetValue(code.recognize(3))
        if os.path.exists(dir+'char4.jpg'):
            self.char4.SetValue(code.recognize(4))
        if os.path.exists(dir+'char5.jpg'):
            self.char5.SetValue(code.recognize(5))

    def Onbuttonopendb(self,event):
        pass

    def Onbuttononekey(self,event):
        pass

    def Onbuttonsavechar1(self,event):
        code.fontsave(1,self.char1.GetValue())

    def Onbuttonsavechar2(self,event):
        code.fontsave(2,self.char2.GetValue())

    def Onbuttonsavechar3(self,event):
        code.fontsave(3,self.char3.GetValue())

    def Onbuttonsavechar4(self,event):
        code.fontsave(4,self.char4.GetValue())

    def Onbuttonsavechar5(self,event):
        code.fontsave(5,self.char5.GetValue())

    def Onbuttonopt(self,event):
        if(self.opt==0):
            self.SetSize((900,430))
            self.opt=1
        else:
            self.SetSize((560,430))
            self.opt=0

    def Showmes(self,mes):
        dlg=wx.MessageDialog(self,mes,'提示信息',wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()

    def Showimage(self,before,after):
        b=wx.Bitmap(dir+before,wx.BITMAP_TYPE_JPEG)
        a=wx.Bitmap(dir+after,wx.BITMAP_TYPE_JPEG)
        self.image_before.SetBitmap(b)
        self.image_after.SetBitmap(a)
        code.enlargeimage(after)
        big=wx.Bitmap(dir+'big.jpg',wx.BITMAP_TYPE_JPEG)
        self.image_big.SetBitmap(big)


if __name__ == '__main__':
    #code.init()
    app=wx.App()
    Main(None).Show()
    app.MainLoop()
