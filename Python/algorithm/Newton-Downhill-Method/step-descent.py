# step and stepde should be used together
# func is a function, variable should be a tuple(func(tuple))
def step(func,y0,step=None,minimum=True):
    if isinstance(y0,(list,tuple)):
        x0=tuple(list(y0).copy())
        if step==None:
            step=len(y0)*(1,)
    elif isinstance(x0,(int,float,complex)):
        x0=(y0,)
        if step==None:
            step=(1,)
    paras=[(x0[0]-step[0],),(x0[0],),(x0[0]+step[0],)]
    i=1
    while i<len(x0):
        para=[]
        for tup in paras:
            para.append(tup+(x0[i]-step[i],))
            para.append(tup+(x0[i],))
            para.append(tup+(x0[i]+step[i],))
        paras=[]
        for p in para:
            paras.append(p)
        i=i+1
    d={}
    for i in paras:
        d[func(i)]=i
    if minimum:
        # print(min(d.keys()),d[min(d.keys())])
        return min(d.keys()),d[min(d.keys())]
    else:
        # print(max(d.keys()),d[max(d.keys())])
        return max(d.keys()),d[max(d.keys())]

def stepde(func,y0,step=None,minimum=True):
    x0=y0
    output,x1=grad(func,x0,step,minimum=True)
    while x1!=x0:
        x0=x1
        output,x1=grad(func,x1,step,minimum=True)
    return output,x1

# this is just a checking func
def z(tup):
    return (tup[0]-1.7)**2+(tup[1]-1)**2

print(gradde(z,(1,2),step=(0.1,0.1)))
