from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import os
import clipboard as cp

try:
    fundamental=open('matrix\\fundamental')
    fundamental.close()
except FileNotFoundError:
    if not os.path.exists(os.getcwd()+'\\matrix\\'):
        os.makedirs(os.getcwd()+'\\matrix\\')
    fundamental=open('matrix\\fundamental','w')
    fundamental.write('1\n1 0 & 0 1\n1 0 0 & 0 1 0 & 0 0 1\n1 0 0 0 & 0 1 0 0 & 0 0 1 0 & 0 0 0 1\n1 0 0 0 0 & 0 1 0 0 0 & 0 0 1 0 0 & 0 0 0 1 0 & 0 0 0 0 1')
    fundamental.close()

try:
    matrix=open('matrix\\matrix')
    matrix.close()
except FileNotFoundError:
    if not os.path.exists(os.getcwd()+'\\matrix\\'):
        os.makedirs(os.getcwd()+'\\matrix\\')
    matrix=open('matrix\\matrix','w')
    matrix.close()

# calculation functions
def add(m1,m2):
    m3=[]
    m=len(m1)
    n=len(m1[0])
    for i in range(m):
        line=[]
        for j in range(n):
            line.append(m1[i][j]+m2[i][j])
        m3.append(line)
    return m3

def minor(m1,m2):
    m3=[]
    m=len(m1)
    n=len(m1[0])
    for i in range(m):
        line=[]
        for j in range(n):
            line.append(m1[i][j]-m2[i][j])
        m3.append(line)
    return m3

def multiply(m1,m2):
    m3=[]
    l=len(m1)
    m=len(m1[0])
    n=len(m2[0])
    i=0
    while i<l:
        line=[]
        k=0
        while k<n:
            a=0
            j=0
            while j<m:
                a=a+m1[i][j]*m2[j][k]
                j=j+1
            line.append(a)
            k=k+1
        m3.append(line)
        i=i+1
    return m3

def transpose(m):
    n1=len(m)
    n2=len(m[0])
    ans=[]
    i=0
    while i<n1:
        line=[]
        j=0
        while j<n2:
            line.append(m[j][i])
            j=j+1
        ans.append(line)
        i=i+1
    return ans

def copy(a):
    if isinstance(a,(int,float,complex,str,bool)):
        return a
    elif isinstance(a,dict):
        b={}
        for key in a.keys():
            b[copy(key)]=copy(a[key])
        return b
    elif isinstance(a,list):
        b=[]
        for element in a:
            b.append(copy(element))
        return b
    elif isinstance(a,tuple):
        if len(a)==0:
            return ()
        elif len(a)==1:
            return (copy(a[0]),)
        elif len(a)==2:
            b=copy(a[0])
            c=copy(a[1])
            d=(b,c)
            return d
        else:
            return (copy(a[0]),)+copy(a[1:])

def complement(matrix,i): # det(m_)*(-1)**(...) of (1,i+1)
    co=copy(matrix)
    j=0
    while j<len(matrix):
        if j!=i:
            del co[j][0]
        j=j+1
    del co[i]
    return (-1)**(2+i)*det(co)

def complement_(m,i,j): # det(m_)*(-1)**(...) of (i+1,j+1)
    m_=copy(m)
    l=len(m_)
    del m_[i]
    k=0
    while k<l-1:
        del m_[k][j]
        k=k+1
    return det(m_)*(-1)**(i+1+j+1)

def det(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix)==2:
        result=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return result
    else:
        result=0
        i=0
        while i<len(matrix):
            result=result+matrix[i][0]*complement(matrix,i)
            i=i+1
        return result

def inverse(m):
    d=det(m)
    n=len(m)
    new=[]
    i=0
    while i<n:
        line=[]
        j=0
        while j<n:
            line.append(complement_(m,j,i)/d)
            j=j+1
        new.append(line)
        i=i+1
    return new

def column_exchange(formation,k):# Cramer det, exchange column k+1
    form=copy(formation)
    n=len(form)
    i=0
    while i<n:
        form[i][k]=form[i].pop()
        i=i+1
    return form

def linear_equation(m):
    m_=copy(m)
    for i in m_:
        del i[-1]
    s=''
    n=len(m)
    i=0
    while i<n:
        a=det(column_exchange(m,i))/det(m_)
        s=s+str(a)+'\n'
        i=i+1
    s=s[:-1]
    return s

# functional def
def eval_matrix(m): # make the matrix(list) transfer from string to eval
    new=[]
    for i in m:
        line=[]
        for j in i:
            line.append(eval(j))
        new.append(line)
    return new

def return_matrix(m): # let the matrix(list) be in the form of string in order to print directly on Text
    length=0
    for i in m:
        for j in i:
            if len(str(j))>length:
                length=len(str(j))
    string=''
    for i in m:
        for j in i:
            string=string+str(j)+(length-len(str(j))+1)*' '
        string=string[:-1]+'\n'
    string=string[:-1]
    return string

def process():
    button_copy_3.config(state=NORMAL)
    v=var.get()
    warn=st_warn.get(1.0,END)[:-1]
    warn=warn!=''
    if input_valid():
        if v==1:
            m1=get_matrix_text(st_1)
            m2=get_matrix_text(st_2)
            m=add(m1,m2)
            st_3.config(state=NORMAL)
            st_3.delete(1.0,END)
            st_3.insert(END,return_matrix(m))
            st_3.config(state=DISABLED)
            button_save_3.config(state=NORMAL,cursor='hand2')
            if warn:
                st_warn.insert(END,'\n\nProcessed')
            else:
                st_warn.insert(END,'Processed')
        elif v==2:
            m1=get_matrix_text(st_1)
            m2=get_matrix_text(st_2)
            m=minor(m1,m2)
            st_3.config(state=NORMAL)
            st_3.delete(1.0,END)
            st_3.insert(END,return_matrix(m))
            st_3.config(state=DISABLED)
            button_save_3.config(state=NORMAL,cursor='hand2')
            if warn:
                st_warn.insert(END,'\n\nProcessed')
            else:
                st_warn.insert(END,'Processed')
        elif v==3:
            m1=get_matrix_text(st_1)
            m2=get_matrix_text(st_2)
            m=multiply(m1,m2)
            st_3.config(state=NORMAL)
            st_3.delete(1.0,END)
            st_3.insert(END,return_matrix(m))
            st_3.config(state=DISABLED)
            button_save_3.config(state=NORMAL,cursor='hand2')
            if warn:
                st_warn.insert(END,'\n\nProcessed')
            else:
                st_warn.insert(END,'Processed')
        elif v==4:
            m=get_matrix_text(st_1)
            m=transpose(m)
            st_3.config(state=NORMAL)
            st_3.delete(1.0,END)
            st_3.insert(END,return_matrix(m))
            st_3.config(state=DISABLED)
            button_save_3.config(state=NORMAL,cursor='hand2')
            if warn:
                st_warn.insert(END,'\n\nProcessed')
            else:
                st_warn.insert(END,'Processed')
        elif v==5:
            m=get_matrix_text(st_1)
            m=det(m)
            st_3.config(state=NORMAL)
            st_3.delete(1.0,END)
            st_3.insert(END,str(m))
            st_3.config(state=DISABLED)
            button_save_3.config(state=DISABLED,cursor='arrow')
            if warn:
                st_warn.insert(END,'\n\nProcessed')
            else:
                st_warn.insert(END,'Processed')
        elif v==6:
            m=get_matrix_text(st_1)
            m=inverse(m)
            st_3.config(state=NORMAL)
            st_3.delete(1.0,END)
            st_3.insert(END,return_matrix(m))
            st_3.config(state=DISABLED)
            button_save_3.config(state=NORMAL,cursor='hand2')
            if warn:
                st_warn.insert(END,'\n\nProcessed')
            else:
                st_warn.insert(END,'Processed')
        elif v==7:
            button_save_3.config(state=DISABLED,cursor='arrow')
            m=get_matrix_text(st_1)
            m=linear_equation(m)
            st_3.config(state=NORMAL)
            st_3.delete(1.0,END)
            st_3.insert(END,m)
            st_3.config(state=DISABLED)
            button_save_3.config(state=DISABLED,cursor='arrow')
            if warn:
                st_warn.insert(END,'\n\nProcessed')
            else:
                st_warn.insert(END,'Processed')
    st_warn.see(END)

def copy_to_clipboard(text):
    cp.copy(text.get(1.0,END)[:-1])

def get_matrix(path,n): # get matrix from matrix/matrix,fundamental
    text=open(path,'r+')
    i=0
    while i<n:
        line=text.readline()
        i=i+1
    if line[-1]=='\n':
        line=line[:-1]
    line=line.split()
    m=[]
    lin=[]
    for i in line:
        if i=='&':
            m.append(lin)
            lin=[]
        else:
            lin.append(i)
    m.append(lin)
    try:
        m=eval_matrix(m)
        return m
    except NameError:
        st_warn.insert(END,'\n\nIllegal character detected from the saved matrix!')
        st_warn.see(END)
        return None # illegal character may be saved

def get_matrix_text(text): # get matrix from the text
    s=text.get(1.0,END)
    while s!='': # eliminate '\n' and ' ' from the end, which are irrelevant
        if s[-1]=='\n' or s[-1]==' ':
            s=s[:-1]
        elif s[0]=='\n' or s[0]==' ':
            s=s[1:]
        else:
            break
    if s=='':
        return None # that means empty input, it will be checked in input_valid() from line 4
    else:
        m=[]
        n=len(s)
        begin=0
        i=0
        while i<n:
            if i==n-1: # it has been the last one
                m.append(s[begin:].split())
            elif s[i]=='\n':
                m.append(s[begin:i].split())
                begin=i
            else:
                i=i+1
                continue
            i=i+1
        try:
            m=eval_matrix(m)
            return m
            print(m)
        except NameError:
            return False # illegal character may be input

def save_matrix(m): # write matrix(eval) in txt
    f=open('matrix\\matrix','r+')
    c=f.read()
    s=''
    for i in m:
        for j in i:
            s=s+str(j)+' '
        s=s+'& '
    s=s[:-3]
    if c=='':
        f.write(s)
    else:
        f.write('\n'+s)
    f.close()
    cho_1['values']=save_list()
    cho_2['values']=save_list()
    cho_search['values']=save_list()[:-5]

def delete_matrix(n):
    i=0
    begin=0
    j=0 # count number of '\n'
    f=open('matrix\\matrix','r+')
    c='\n'+f.read()+'\n'
    l=len(c)
    f.close()
    f=open('matrix\\matrix','r+')
    m=c.count('\n')
    while i<l:
        if c[i]=='\n':
            j=j+1
        if j==n:
            begin=i
            i=i+1
            break
        i=i+1
    while i<l:
        if c[i]=='\n':
            j=j+1
        if j==n+1:
            end=i
            break
        i=i+1
    f.truncate() # clear 'matrix\matrix'
    c=c[:begin]+c[end:]
    f.write(c[2:-1])
    f.close()
    cho_1['values']=save_list()
    cho_2['values']=save_list()
    cho_search['values']=save_list()[:-5]

def input_valid():
    v=var.get()
    error_flag=0
    warn=st_warn.get(1.0,END)[:-1]
    warn=warn!='' # check whether warn had existed
    if v==1 or v==2: # check matrix plus and matrix minor
        m1=get_matrix_text(st_1)
        m2=get_matrix_text(st_2)
        if m1==None or m2==None or m1==False or m2==False:
            if m1==None:
                if warn:
                    st_warn.insert(END,'\n\nEmpty input in the first matrix!')
                    error_flag=1
                else:
                    st_warn.insert(END,'Empty input in the first matrix!')
                    error_flag=1
            if m2==None:
                if error_flag==1:
                    st_warn.insert(END,'\nEmpty input in the second matrix!')
                else:
                    if warn:
                        st_warn.insert(END,'\n\nEmpty input in the second matrix!')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Empty input in the second matrix!')
                        error_flag=1
            if m1==False:
                if error_flag==1:
                    st_warn.insert(END,'\nIllegal character may be in the first matrix.')
                else:
                    if warn:
                        st_warn.insert(END,'\n\nIllegal character may be in the first matrix.')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Illegal character may be in the first matrix.')
                        error_flag=1
            if m2==False:
                if error_flag==1:
                    st_warn.insert(END,'\nIllegal character may be in the second matrix.')
                else:
                    if warn:
                        st_warn.insert(END,'\n\nIllegal character may be in the second matrix.')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Illegal character may be in the second matrix.')
                        error_flag=1
        else:
            error1=0
            error2=0
            n1=len(m1)
            n2=len(m1[0])
            n3=len(m2)
            n4=len(m2[0])
            i=0
            while i<n1:
                if len(m1[i])!=n2:
                    error1=1
                    break
                i=i+1
            i=0
            while i<n3:
                if len(m2[i])!=n4:
                    error2=1
                    break
                i=i+1
            if error1==1 or error2==1 or n1!=n3 or n2!=n4:
                if error1==1:
                    if warn:
                        st_warn.insert(END,'\n\nUnorganized format for the first matrix!')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Unorganized format for the first matrix!')
                        error_flag=1
                if error2==1:
                    if error_flag==1:
                        st_warn.insert(END,'\nUnorganized format for the second matrix!')
                    else:
                        if warn:
                            st_warn.insert(END,'\n\nUnorganized format for the second matrix!')
                            error_flag=1
                        else:
                            st_warn.insert(END,'Unorganized format for the second matrix!')
                            error_flag=1
                if n1!=n3:
                    if error_flag==1:
                        st_warn.insert(END,'\nThe first and second matrices are not in the identical form for column!')
                    else:
                        if warn:
                            st_warn.insert(END,'\n\nThe first and second matrices are not in the identical form for column!')
                            error_flag=1
                        else:
                            st_warn.insert(END,'The first and second matrices are not in the identical form for column!')
                            error_flag=1
                if n2!=n4:
                    if error_flag==1:
                        st_warn.insert(END,'\nThe first and second matrices are not in the identical form for line!')
                    else:
                        if warn:
                            st_warn.insert(END,'\n\nThe first and second matrices are not in the identical form for line!')
                            error_flag=1
                        else:
                            st_warn.insert(END,'The first and second matrices are not in the identical form for line!')
                            error_flag=1
    elif v==3: # check matrix multiply
        m1=get_matrix_text(st_1)
        m2=get_matrix_text(st_2)
        if m1==None or m2==None or m1==False or m2==False:
            if m1==None:
                if warn:
                    st_warn.insert(END,'\n\nEmpty input in the first matrix!')
                    error_flag=1
                else:
                    st_warn.insert(END,'\n\nEmpty input in the first matrix!')
                    error_flag=1
            if m2==None:
                if error_flag==1:
                    st_warn.insert(END,'\nEmpty input in the second matrix!')
                else:
                    if warn:
                        st_warn.insert(END,'\n\nEmpty input in the second matrix!')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Empty input in the second matrix!')
                        error_flag=1
            if m1==False:
                if error_flag==1:
                    st_warn.insert(END,'\nIllegal character may be in the first matrix.')
                else:
                    if warn:
                        st_warn.insert(END,'\n\nIllegal character may be in the first matrix.')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Illegal character may be in the first matrix.')
                        error_flag=1
            if m2==False:
                if error_flag==1:
                    st_warn.insert(END,'\nIllegal character may be in the second matrix.')
                else:
                    if warn:
                        st_warn.insert(END,'\n\nIllegal character may be in the second matrix.')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Illegal character may be in the second matrix.')
                        error_flag=1
        else:
            error1=0
            error2=0
            n1=len(m1)
            n2=len(m1[0])
            n3=len(m2)
            n4=len(m2[0])
            i=0
            while i<n1:
                if len(m1[i])!=n2:
                    error1=1
                    break
                i=i+1
            i=0
            while i<n3:
                if len(m2[i])!=n4:
                    error2=1
                    break
                i=i+1
            if error1==1 or error2==1 or n2!=n3:
                if error1==1:
                    if warn:
                        st_warn.insert(END,'\n\nUnorganized format for the first matrix!')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Unorganized format for the first matrix!')
                        error_flag=1
                if error2==1:
                    if error_flag==1:
                        st_warn.insert(END,'\nUnorganized format for the second matrix!')
                    else:
                        if warn:
                            st_warn.insert(END,'\n\nUnorganized format for the second matrix!')
                            error_flag=1
                        else:
                            st_warn.insert(END,'Unorganized format for the second matrix!')
                            error_flag=1
                if n2!=n3:
                    if error_flag==1:
                        st_warn.insert(END,'\nThe first matrix\'s line is not the identical form as the second matrix\'s column!')
                    else:
                        if warn:
                            st_warn.insert(END,'\n\nThe first matrix\'s line is not the identical form as the second matrix\'s column!')
                            error_flag=1
                        else:
                            st_warn.insert(END,'The first matrix\'s line is not the identical form as the second matrix\'s column!')
                            error_flag=1
    if v==4: # check the form of transpose
        m=get_matrix_text(st_1)
        if m==None or m==False:
            if m==None:
                if warn:
                    st_warn.insert(END,'\n\nEmpty input in the matrix!')
                    error_flag=1
                else:
                    st_warn.insert(END,'Empty input in the matrix!')
                    error_flag=1
            if m==False:
                if error_flag==1:
                    st_warn.insert(END,'\nIllegal character may be in the matrix.')
                else:
                    if warn:
                        st_warn.insert(END,'\n\nIllegal character may be in the matrix.')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Illegal character may be in the matrix.')
                        error_flag=1
        else:
            error=0
            n1=len(m)
            n2=len(m[0])
            i=0
            while i<n1:
                if len(m[i])!=n2:
                    error=1
                    break
                i=i+1
            if error==1:
                if warn:
                    st_warn.insert(END,'\n\nUnorganized format for the matrix!')
                    error_flag=1
                else:
                    st_warn.insert(END,'Unorganized format for the matrix!')
                    error_flag=1
    if v==5: # check the form of determination
        m=get_matrix_text(st_1)
        if m==None or m==False:
            if m==None:
                if warn:
                    st_warn.insert(END,'\n\nEmpty input in the matrix!')
                    error_flag=1
                else:
                    st_warn.insert(END,'Empty input in the matrix!')
                    error_flag=1
            if m==False:
                if error_flag==1:
                    st_warn.insert(END,'\nIllegal character may be in the matrix.')
                else:
                    if warn:
                        st_warn.insert(END,'\n\nIllegal character may be in the matrix.')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Illegal character may be in the matrix.')
                        error_flag=1
        else:
            error=0
            n1=len(m)
            n2=len(m[0])
            i=0
            while i<n1:
                if len(m[i])!=n2:
                    error=1
                    break
                i=i+1
            if error==1 or n1!=n2:
                if error==1:
                    if warn:
                        st_warn.insert(END,'\n\nUnorganized format for the matrix!')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Unorganized format for the matrix!')
                        error_flag=1
                if n1!=n2:
                    if error_flag==1:
                        st_warn.insert(END,'\nColumn and line of matrix are not identical!')
                    else:
                        if warn:
                            st_warn.insert(END,'\n\nColumn and line of matrix are not identical!')
                            error_flag=1
                        else:
                            st_warn.insert(END,'Column and line of matrix are not identical!')
                            error_flag=1
    if v==6: # check the form of inverse matrix
        m=get_matrix_text(st_1)
        if m==None or m==False:
            if m==None:
                if warn:
                    st_warn.insert(END,'\n\nEmpty input in the matrix!')
                    error_flag=1
                else:
                    st_warn.insert(END,'Empty input in the matrix!')
                    error_flag=1
            if m==False:
                if error_flag==1:
                    st_warn.insert(END,'\nIllegal character may be in the matrix.')
                else:
                    if warn:
                        st_warn.insert(END,'\n\nIllegal character may be in the matrix.')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Illegal character may be in the matrix.')
                        error_flag=1
        else:
            error=0
            n1=len(m)
            n2=len(m[0])
            i=0
            while i<n1:
                if len(m[i])!=n2:
                    error=1
                    break
                i=i+1
            if error==1 or n1!=n2:
                if error==1:
                    if warn:
                        st_warn.insert(END,'\n\nUnorganized format for the matrix!')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Unorganized format for the matrix!')
                        error_flag=1
                if n1!=n2:
                    if error_flag==1:
                        st_warn.insert(END,'\nColumn and line of matrix are not identical!')
                    else:
                        if warn:
                            st_warn.insert(END,'\n\nColumn and line of matrix are not identical!')
                            error_flag=1
                        else:
                            st_warn.insert(END,'Column and line of matrix are not identical!')
                            error_flag=1
            else:
                if det(m)==0:
                    if warn:
                        st_warn.insert(END,'\n\nNot inverseable!')
                    else:
                        st_warn.insert(END,'Not inverseable!')
                    error_flag=1
    if v==7: # check the form of linear equation
        m=get_matrix_text(st_1)
        if m==None or m==False:
            if m==None:
                if warn:
                    st_warn.insert(END,'\n\nEmpty input in the matrix!')
                    error_flag=1
                else:
                    st_warn.insert(END,'Empty input in the matrix!')
                    error_flag=1
            if m==False:
                if error_flag==1:
                    st_warn.insert(END,'\nIllegal character may be in the matrix.')
                else:
                    if warn:
                        st_warn.insert(END,'\n\nIllegal character may be in the matrix.')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Illegal character may be in the matrix.')
                        error_flag=1
        else:
            error=0
            n1=len(m)
            n2=len(m[0])
            i=0
            while i<n1:
                if len(m[i])!=n2:
                    error=1
                    break
                i=i+1
            if error==1 or n1+1!=n2:
                if error==1:
                    if warn:
                        st_warn.insert(END,'\n\nUnorganized format for the matrix!')
                        error_flag=1
                    else:
                        st_warn.insert(END,'Unorganized format for the matrix!')
                        error_flag=1
                if n1+1!=n2:
                    if error_flag==1:
                        st_warn.insert(END,'\nColumn plus one and line of matrix are not equal!')
                    else:
                        if warn:
                            st_warn.insert(END,'\n\nColumn plus one and line of matrix are not equal!')
                            error_flag=1
                        else:
                            st_warn.insert(END,'Column plus one and line of matrix are not equal!')
                            error_flag=1
    st_warn.see(END)
    if error_flag==0:
        return True
    else:
        return False

def save_list():
    lis=[]
    lis_=['Identity-1','Identity-2','Identity-3','Identity-4','Identity-5']
    f=open('matrix\\matrix')
    c=f.read()
    n=c.count('\n')
    for i in range(n+1):
        lis.append('matrix '+str(i+1))
    if c=='':
        lis=lis_
    else:
        lis=lis+lis_
    return lis

def auto_1(event):
    a=cho_1.get()
    if 'matrix' in a:
        a=int(a[7:])
        m=get_matrix('matrix\\matrix',a)
    elif 'Identity' in a:
        a=int(a[9:])
        m=get_matrix('matrix\\fundamental',a)
    st_1.delete(1.0,END)
    st_1.insert(END,return_matrix(m))

def copy1():
    cp.copy(st_1.get(1.0,END)[:-1])
    if st_warn.get(1.0,END)[:-1]=='':
        st_warn.insert(END,'Copied to clipboard from the first input')
    else:
        st_warn.insert(END,'\n\nCopied to clipboard from the first input')
    st_warn.see(END)

def auto_2(event):
    a=cho_2.get()
    if 'matrix' in a:
        a=int(a[7:])
        m=get_matrix('matrix\\matrix',a)
    elif 'Identity' in a:
        a=int(a[9:])
        m=get_matrix('matrix\\fundamental',a)
    st_2.delete(1.0,END)
    st_2.insert(END,return_matrix(m))

def copy2():
    cp.copy(st_2.get(1.0,END)[:-1])
    if st_warn.get(1.0,END)[:-1]=='':
        st_warn.insert(END,'Copied to clipboard from the second input')
    else:
        st_warn.insert(END,'\n\nCopied to clipboard from the second input')
    st_warn.see(END)

def copy3():
    cp.copy(st_3.get(1.0,END)[:-1])
    if st_warn.get(1.0,END)[:-1]=='':
        st_warn.insert(END,'Copied to clipboard from the processed')
    else:
        st_warn.insert(END,'\n\nCopied to clipboard from the processed')
    st_warn.see(END)

def save3():
    m=get_matrix_text(st_3)
    save_matrix(m)
    if st_warn.get(1.0,END)[:-1]=='':
        st_warn.insert(END,'Processed has been saved')
    else:
        st_warn.insert(END,'\n\nProcessed has been saved')
    st_warn.see(END)

def auto_search(event):
    a=cho_search.get()
    if 'matrix' in a:
        m=get_matrix('matrix\\matrix',int(a[7:]))
    elif 'Identity' in a:
        m=get_matrix('matrix\\fundamental',int(a[9:]))
    st_search.delete(1.0,END)
    st_search.insert(END,return_matrix(m))

def copysearch():
    m=cp.copy(st_search.get(1.0,END)[:-1])
    if st_warn.get(1.0,END)[:-1]=='':
        st_warn.insert(END,'Copied to clipboard from the searched')
    else:
        st_warn.insert(END,'\n\nCopied to clipboard from the searched')
    st_warn.see(END)

def delete_matrix_():
    a=cho_search.get()
    if 'matrix' in a:
        delete_matrix(int(a[7:]))
        if st_warn.get(1.0,END)[:-1]=='':
            st_warn.insert(END,'Matrix '+a[7:]+' has been deleted')
        else:
            st_warn.insert(END,'\n\nMatrix '+a[7:]+' has been deleted')
    elif 'Identity' in a:
        if st_warn.get(1.0,END)[:-1]=='':
            st_warn.insert(END,'Matrix in fundamental could not be deleted!')
        else:
            st_warn.insert(END,'\n\nMatrix in fundamental could not be deleted!')
    st_warn.see(END)

mat=Tk()

mat.withdraw()

mat.title('matrix processing')

if os.path.exists('matrix.ico'):
    mat.iconbitmap('matrix.ico')

width=935
height=875
padx=(mat.winfo_screenwidth()-width)/2
pady=(mat.winfo_screenheight()-height)/2
mat.geometry('%dx%d+%d+%d'%(width,height,padx,pady))

mat.resizable(width=False,height=False)

mat.configure(bg='azure')

mat.deiconify()

var=IntVar()

label_0=Label(mat,text='Choose a function to process',bg='azure')
label_warn=Label(mat,text='Status and Warning',bg='azure')
st_warn=scrolledtext.ScrolledText(mat,width=100,height=8,bg='aliceblue')

r1=Radiobutton(mat,
               text='matrix plus',
               bg='azure',
               cursor='hand2',
               variable=var,
               value=1)
r2=Radiobutton(mat,
               text='matrix minor',
               bg='azure',
               cursor='hand2',
               variable=var,
               value=2)
r3=Radiobutton(mat,
               text='matrix multiply',
               bg='azure',
               cursor='hand2',
               variable=var,
               value=3)
r4=Radiobutton(mat,
               text='matrix transpose',
               bg='azure',
               cursor='hand2',
               variable=var,
               value=4)
r5=Radiobutton(mat,
               text='determination',
               bg='azure',
               cursor='hand2',
               variable=var,
               value=5)
r6=Radiobutton(mat,
               text='inverse matrix',
               bg='azure',
               cursor='hand2',
               variable=var,
               value=6)
r7=Radiobutton(mat,
               text='linear equation',
               bg='azure',
               cursor='hand2',
               variable=var,
               value=7)

#first input
label_1=Label(mat,text='Input the matrix',bg='azure')
st_1=scrolledtext.ScrolledText(mat,width=25,height=8,bg='aliceblue')
cho_1=ttk.Combobox(mat,width=15)
cho_1['values']=save_list()
cho_1['state']='readonly'
cho_1.bind('<<ComboboxSelected>>',auto_1)
button_copy_1=Button(mat,
                     text='Copy to clipboard',
                     command=copy1,
                     bg='lightcyan',
                     relief=RIDGE,
                     overrelief=RAISED,cursor='hand2')

#second input
label_2=Label(mat,text='Input the second matrix',bg='azure')
st_2=scrolledtext.ScrolledText(mat,width=25,height=8,bg='aliceblue')
cho_2=ttk.Combobox(mat,width=15)
cho_2['values']=save_list()
cho_2['state']='readonly'
cho_2.bind('<<ComboboxSelected>>',auto_2)
button_copy_2=Button(mat,
                     text='Copy to clipboard',
                     command=copy2,
                     bg='lightcyan',
                     relief=RIDGE,
                     overrelief=RAISED,
                     cursor='hand2')

#output
label_3=Label(mat,text='Output',bg='azure')
st_3=scrolledtext.ScrolledText(mat,state=DISABLED,width=25,height=8,bg='aliceblue')
button_copy_3=Button(mat,
                     text='Copy to clipboard',
                     command=copy3,
                     bg='lightcyan',
                     relief=RIDGE,
                     overrelief=RAISED,
                     cursor='hand2')
button_save_3=Button(mat,
                     text='Save',
                     command=save3,
                     bg='floralwhite',
                     state=DISABLED,
                     relief=RIDGE,
                     overrelief=RAISED)
button_process=Button(mat,
                      text='Process',
                      width=20,
                      height=2,
                      command=process,
                      bg='lemonchiffon',
                      relief=RIDGE,
                      overrelief=RAISED,
                     cursor='hand2')

#search
label_search=Label(mat,text='Select a matrix has been saved',bg='azure')
st_search=scrolledtext.ScrolledText(mat,width=25,height=8,bg='aliceblue')
cho_search=ttk.Combobox(mat,width=15)
cho_search['values']=save_list()[:-5]
cho_search['state']='readonly'
cho_search.bind('<<ComboboxSelected>>',auto_search)
button_copy_search=Button(mat,
                          text='Copy to clipboard',
                          command=copysearch,
                          bg='lightcyan',
                          relief=RIDGE,
                          overrelief=RAISED,
                          cursor='hand2')
button_delete=Button(mat,
                     text='Delete',
                     command=delete_matrix_,
                     bg='floralwhite',
                     relief=RIDGE,
                     overrelief=RAISED,
                     cursor='hand2')

#place
label_0.place(x=5,y=10,anchor=NW)
r1.place(x=15,y=40,anchor=NW)
r2.place(x=15,y=70,anchor=NW)
r3.place(x=15,y=100,anchor=NW)
r4.place(x=15,y=130,anchor=NW)
r5.place(x=15,y=160,anchor=NW)
r6.place(x=15,y=190,anchor=NW)
r7.place(x=15,y=220,anchor=NW)

label_search.place(x=510,y=10,anchor=NW)
st_search.place(x=680,y=40,anchor=NW)
cho_search.place(x=510,y=40,anchor=NW)
button_copy_search.place(x=680,y=185,anchor=NW)
button_delete.place(x=868,y=185,anchor=NW)

label_1.place(x=5,y=270,anchor=NW)
cho_1.place(x=5,y=300)
st_1.place(x=175,y=300,anchor=NW)
button_copy_1.place(x=175,y=445)

label_2.place(x=463,y=270,anchor=NW)
cho_2.place(x=463,y=300,anchor=NW)
st_2.place(x=633,y=300,anchor=NW)
button_copy_2.place(x=633,y=445,anchor=NW)

label_3.place(x=5,y=485,anchor=NW)
st_3.place(x=175,y=515,anchor=NW)
button_process.place(x=485,y=630,anchor=NW)
button_save_3.place(x=377,y=660,anchor=NW)
button_copy_3.place(x=175,y=660,anchor=NW)

label_warn.place(x=5,y=700,anchor=NW)
st_warn.place(x=5,y=730,anchor=NW)

#mainloop
mat.mainloop()
