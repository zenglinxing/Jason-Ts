from tkinter import *
import psutil
import os
import signal

def kill():
    sign=text.get(1.0,END)[:-1]
    i=0
    pids=psutil.pids()
    for pid in pids:
        if sign in psutil.Process(pid).name():
            os.kill(pid,signal.SIGABRT)
            i=i+1
            label2.config(text=str(i)+' of the \"'+sign+'\" had been killed')
    if i==0:
        label2.config(text='None of the \"'+sign+'\" was killed')

top=Tk()

top.withdraw()

top.title('Kill Process')

width=400
height=120
top.geometry('%dx%d+%d+%d' % (width,height,(top.winfo_screenwidth()-width)/2,(top.winfo_screenheight()-height)/2))

top.resizable(width=False,height=False)

top.deiconify()

Canvas(top,height=800,width=900,bg='white').pack(expand=YES,fill=BOTH)

label1=Label(top,
             text='Input the sign that is included in the process\'s name',
             bg='white')
text=Text(top,width=42,height=1)
label2=Label(top,bg='white')
button=Button(top,
       text='kill',
       bg='white',
       relief=RIDGE,
       overrelief=RAISED,
       command=kill)

label1.place(x=5,y=5)
text.place(x=5,y=31)
button.place(x=5,y=60)
label2.place(x=5,y=86)

top.mainloop()
