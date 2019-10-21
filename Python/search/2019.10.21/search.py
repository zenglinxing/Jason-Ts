import os,shutil
import pyperclip as cp
from tkinter.ttk import *
from tkinter import *
from tkinter import scrolledtext

def all_file_path(path): # return file's name, with its path
    os.chdir(path)
    filess=[]
    filess_=[]
    files=os.listdir(path)
    for file in files:
        if os.path.isfile(file):
            filess.append(path+'\\'+file)
            filess_.append(file)
        else:
            filess_new,filess__new=all_file_path(path+'\\'+file)
            filess=filess+filess_new
            filess_=filess_+filess__new
            os.chdir(path)
    return filess,filess_

def Search():
    sign=st1.get(1.0,END)[:-1]
    i=0
    while i<len(sign): # delete '\n'
        if sign[i]=='\n':
            if i<len(sign)-1:
                sign=sign[:i]+' '+sign[i+1:]
            else:
                sign=sign[:i]
        else:
            i=i+1
    sign=sign.split()
    sign_=[] # lower case of sign
    for sig in sign:
        sign_.append(sig.lower())
    output=''
    output_=''
    files,files_=all_file_path(os.getcwd()) # files include its path
    os.chdir(os.getcwd())
    n=len(files)
    m=len(sign)
    i=0
    while i<n:
        j=0
        while j<m:
            if sign[j] in files_[i]:
                output=output+files[i]+'\n'
            elif sign_[j] in files_[i].lower():
                output_=output_+files[i]+'\n'
            j=j+1
        i=i+1
    if len(output)>=1:
        output=output[:-1]
    if len(output)>=1:
        output_=output_[:-1]
    st2.config(state=NORMAL)
    st3.config(state=NORMAL)
    st2.delete(1.0,END)
    st3.delete(1.0,END)
    st2.insert(END,output)
    st3.insert(END,output_)
    st2.config(state=DISABLED)
    st3.config(state=DISABLED)

def Copy():
    cp.copy(st2.get(1.0,END)[:-1])

def Copy1():
    cp.copy(st3.get(1.0,END)[:-1])

top=Tk()

top.withdraw()

top.title('File\'s Path Search')

x=620
y=440
padx=(top.winfo_screenwidth()-x)/2
pady=(top.winfo_screenheight()-y)/2
top.geometry('%dx%d+%d+%d'%(x,y,padx,pady))

top.configure(bg='azure')

top.resizable(width=False,height=False)

top.deiconify()

label0=Label(top,text='Input the sign',bg='azure')

button1=Button(top,
              text='Click to search',
              command=Search,
              bg='lightcyan',
              relief=RIDGE,
              overrelief=RAISED,
              cursor='hand2')

st1=scrolledtext.ScrolledText(top,
                              width=50,
                              height=7,
                              bg='aliceblue')
st2=scrolledtext.ScrolledText(top,
                              width=30,
                              height=10,
                              bg='aliceblue',
                              state=DISABLED)
st3=scrolledtext.ScrolledText(top,
                              width=30,
                              height=10,
                              bg='aliceblue',
                              state=DISABLED)

button2=Button(top,
               text='Copy to Clipboard',
               command=Copy,
               bg='lightcyan',
               relief=RIDGE,
               overrelief=RAISED,
               cursor='hand2')
button3=Button(top,
               text='Copy to Clipboard',
               command=Copy1,
               bg='lightcyan',
               relief=RIDGE,
               overrelief=RAISED,
               cursor='hand2')

# place
label0.place(x=5,y=5)
st1.place(x=5,y=40)
button1.place(x=5,y=165)
st2.place(x=5,y=210)
st3.place(x=320,y=210)
button2.place(x=5,y=400)
button3.place(x=320,y=400)

top.mainloop()
