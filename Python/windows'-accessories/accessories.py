import os,shutil
import win32api
import getpass
from tkinter import *

path1='C:\\Windows\\System32\\'
path2='C:\\Windows\\'
path3='C:\\Program Files\\Common Files\\Microsoft Shared\\Ink\\'
path4='C:\\Program Files\\Windows NT\\Accessories\\'

def fsquirt():
    win32api.ShellExecute(0,'open',path1+'fsquirt.exe','','',1)

def mblctr():
    win32api.ShellExecute(0,'open',path1+'mblctr.exe','','',1)

def explorer():
    win32api.ShellExecute(0,'open',path2+'explorer.exe','','',1)

def stikynot():
    win32api.ShellExecute(0,'open',path1+'StikyNot.exe','','',1)

def mspaint():
    win32api.ShellExecute(0,'open',path1+'mspaint.exe','','',1)

def calc():
    win32api.ShellExecute(0,'open',path1+'calc.exe','','',1)

def notepad():
    win32api.ShellExecute(0,'open',path1+'notepad.exe','','',1)

def snippingtool():
    win32api.ShellExecute(0,'open',path1+'SnippingTool.exe','','',1)

def displayswitch():
    win32api.ShellExecute(0,'open',path1+'DisplaySwitch.exe','','',1)

def netproj():
    win32api.ShellExecute(0,'open',path1+'NetProj.exe','','',1)

def soundrecorder():
    win32api.ShellExecute(0,'open',path1+'SoundRecorder.exe','','',1)

def cmd():
    curpath=os.getcwd()
    try:
        os.chdir('C:\\Users\\'+getpass.getuser())
    finally:
        win32api.ShellExecute(0,'open',path1+'cmd.exe','','',1)
    os.chdir(curpath)

def rundll32():
    win32api.ShellExecute(0,'open',path1+'rundll32.exe','','',1)

def mip():
    win32api.ShellExecute(0,'open',path3+'mip.exe','','',1)

def mobsync():
    win32api.ShellExecute(0,'open',path1+'mobsync.exe','','',1)

def wordpad():
    win32api.ShellExecute(0,'open',path4+'wordpad.exe','','',1)

def mstsc():
    win32api.ShellExecute(0,'open',path1+'mstsc.exe','','',1)



top=Tk()

top.withdraw()

top.title('Windows Accessories')

if os.path.exists('ico\\win7.ico'):
    top.iconbitmap('ico\\win7.ico')

x=800
y=205
padx=(top.winfo_screenwidth()-x)/2
pady=(top.winfo_screenheight()-y)/2
top.geometry('%dx%d+%d+%d'%(x,y,padx,pady))

top.configure(bg='azure')

top.resizable(width=False,height=False)

top.deiconify()

#Bluetooth 文件传送

b1=Button(top,
          text='  Bluetooth 文件传送',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=fsquirt)
if os.path.exists('ico\\fsquirt.png'):
    p1=PhotoImage(file='ico\\fsquirt.png')
    b1.config(compound=LEFT,image=p1)
else:
    b1.config(width=20,height=1)
#Windows 移动中心
b2=Button(top,
          text='  Windows 移动中心',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=mblctr)
if os.path.exists('ico\\mblctr.png'):
    p2=PhotoImage(file='ico\\mblctr.png')
    b2.config(compound=LEFT,image=p2)
else:
    b2.config(width=20,height=1)
#Windows 资源管理器
b3=Button(top,
          text='  Windows 资源管理器',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=explorer)
if os.path.exists('ico\\explorer.png'):
    p3=PhotoImage(file='ico\\explorer.png')
    b3.config(compound=LEFT,image=p3)
else:
    b3.config(width=20,height=1)
#便笺
b4=Button(top,
          text='  便笺',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=stikynot)
if os.path.exists('ico\\StikyNot.png'):
    p4=PhotoImage(file='ico\\StikyNot.png')
    b4.config(compound=LEFT,image=p4)
else:
    b4.config(width=20,height=1)
#画图
b5=Button(top,
          text='  画图',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=mspaint)
if os.path.exists('ico\\mspaint.png'):
    p5=PhotoImage(file='ico\\mspaint.png')
    b5.config(compound=LEFT,image=p5)
else:
    b5.config(width=20,height=1)
#计算器
b6=Button(top,
          text='  计算器',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=calc)
if os.path.exists('ico\\calc.png'):
    p6=PhotoImage(file='ico\\calc.png')
    b6.config(compound=LEFT,image=p6)
else:
    b6.config(width=20,height=1)
#记事本
b7=Button(top,
          text='  记事本',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=notepad)
if os.path.exists('ico\\notepad.png'):
    p7=PhotoImage(file='ico\\notepad.png')
    b7.config(compound=LEFT,image=p7)
else:
    b7.config(width=20,height=1)
#截图工具
b8=Button(top,
          text='  截图工具',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=snippingtool)
if os.path.exists('ico\\SnippingTool.png'):
    p8=PhotoImage(file='ico\\SnippingTool.png')
    b8.config(compound=LEFT,image=p8)
else:
    b8.config(width=20,height=1)
#连接到投影仪
b9=Button(top,
          text='  连接到投影仪',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=displayswitch)
if os.path.exists('ico\\DisplaySwitch.png'):
    p9=PhotoImage(file='ico\\DisplaySwitch.png')
    b9.config(compound=LEFT,image=p9)
else:
    b9.config(width=20,height=1)
#连接到网络投影仪
b10=Button(top,
          text='  连接到网络投影仪',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=netproj)
if os.path.exists('ico\\NetProj.png'):
    p10=PhotoImage(file='ico\\NetProj.png')
    b10.config(compound=LEFT,image=p10)
else:
    b10.config(width=20,height=1)
#录音机
b11=Button(top,
          text='  录音机',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=soundrecorder)
if os.path.exists('ico\\SoundRecorder.png'):
    p11=PhotoImage(file='ico\\SoundRecorder.png')
    b11.config(compound=LEFT,image=p11)
else:
    b11.config(width=20,height=1)
#命令提示符
b12=Button(top,
          text='  命令提示符',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=cmd)
if os.path.exists('ico\\cmd.png'):
    p12=PhotoImage(file='ico\\cmd.png')
    b12.config(compound=LEFT,image=p12)
else:
    b12.config(width=20,height=1)
#入门
b13=Button(top,
          text='  入门',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=rundll32)
if os.path.exists('ico\\rundll32.png'):
    p13=PhotoImage(file='ico\\rundll32.png')
    b13.config(compound=LEFT,image=p13)
else:
    b13.config(width=20,height=1)
#数学输入面板
b14=Button(top,
          text='  数学输入面板',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=mip)
if os.path.exists('ico\\mip.png'):
    p14=PhotoImage(file='ico\\mip.png')
    b14.config(compound=LEFT,image=p14)
else:
    b14.config(width=20,height=1)
#同步中心
b15=Button(top,
          text='  同步中心',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=mobsync)
if os.path.exists('ico\\mobsync.png'):
    p15=PhotoImage(file='ico\\mobsync.png')
    b15.config(compound=LEFT,image=p15)
else:
    b15.config(width=20,height=1)
#写字板
b16=Button(top,
          text='  写字板',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=wordpad)
if os.path.exists('ico\\wordpad.png'):
    p16=PhotoImage(file='ico\\wordpad.png')
    b16.config(compound=LEFT,image=p16)
else:
    b16.config(width=20,height=1)
#远程桌面连接
b17=Button(top,
          text='  远程桌面连接',
          bg='aliceblue',
          width=182,
          height=27,
          cursor='hand2',
          relief=RIDGE,
          overrelief=RAISED,
          anchor=W,
          command=mstsc)
if os.path.exists('ico\\mstsc.png'):
    p17=PhotoImage(file='ico\\mstsc.png')
    b17.config(compound=LEFT,image=p17)
else:
    b17.config(width=20,height=1)


b1.place(x=5,y=5)
b2.place(x=205,y=5)
b3.place(x=405,y=5)
b4.place(x=605,y=5)
b5.place(x=5,y=45)
b6.place(x=205,y=45)
b7.place(x=405,y=45)
b8.place(x=605,y=45)
b9.place(x=5,y=85)
b10.place(x=205,y=85)
b11.place(x=405,y=85)
b12.place(x=605,y=85)
b13.place(x=5,y=125)
b14.place(x=205,y=125)
b15.place(x=405,y=125)
b16.place(x=605,y=125)
b17.place(x=5,y=165)

top.mainloop()
