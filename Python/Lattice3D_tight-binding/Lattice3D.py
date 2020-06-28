from Cubic import *
from Tetragonal import *
from Othorhombic import *
from Monoclinic import *
from Triclinic import *
from Hexagonal import *
from Trigonal import *
from scipy.integrate import quad
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import copy

'''
--------------------------------------------------------------------------------
Preparation
--------------------------------------------------------------------------------
'''
def length_to_minimum(vector,v):
    a=np.array(vector);b=np.array(v[0]);c=np.array(v[1])
    d={}
    for i in (-1,0,1):
        for j in (-1,0,1):
            new_vec=vector+i*b+j*c
            d[np.linalg.norm(new_vec)]=new_vec
    while min(tuple(d.keys()))!=np.linalg.norm(vector):
        vector=d[min(tuple(d.keys()))]
        d={}
        for i in (-1,0,1):
            for j in (-1,0,1):
                new_vec=vector+i*b+j*c
                d[np.linalg.norm(new_vec)]=new_vec
    return vector

def refine_vector(vector):
    a=np.array(vector[0]);b=np.array(vector[1]);c=np.array(vector[2])
    a=length_to_minimum(a,(b,c))
    b=length_to_minimum(b,(a,c))
    c=length_to_minimum(c,(a,b))
    return (tuple(a),tuple(b),tuple(c))

'''
================================================================================
variable:
t: exchange energy
a: length of lattice vector, a tuple including 3 elements, default (1,1,1)
angle: a tuple with 3 angles. Default (90,0,0)
    between vector a and vector b
    between vector c and normal vector of plane a,b
    between vector a and the projection of vector c on plane a,b
radian_type: angle is radian system/degree measure. Default False
    radian system: True
    degree measure: False
err: a number to measure how close the two numbers.
    if |a-b|<=err, then regarded the a==b, and only select the smaller one.
================================================================================
'''

# self.
# t,a,b,c,alpha,beta,gamma,angle_vector,theta,phi,angle,lattice,reciprocal
# normal,V,lattice_V,reciprocal_V,order
class Lattice():
    def __init__(self,lattice='Cubic_1',
                 t=1,
                 t_reverse=None,
                 a=(1,1,1),
                 angle=(90,0,0),
                 radian_type=False,
                 err=10**-8):
        # lat
        if lattice=='Cubic_1':
            a=(a[0],)*3
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Cubic_1(t=t,
                             t_reverse=t_reverse,
                             a=a,
                             angle=angle,
                             radian_type=radian_type,
                             err=err)
        elif lattice=='Cubic_2':
            a=(a[0],)*3
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Cubic_2(t=t,
                             t_reverse=t_reverse,
                             a=a,
                             angle=angle,
                             radian_type=radian_type,
                             err=err)
        elif lattice=='Cubic_3':
            a=(a[0],)*3
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Cubic_3(t=t,
                             t_reverse=t_reverse,
                             a=a,
                             angle=angle,
                             radian_type=radian_type,
                             err=err)
        elif lattice=='Tetragonal_1':
            a=(a[0],)*2+(a[2],)
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Tetragonal_1(t=t,
                                  t_reverse=t_reverse,
                                  a=a,
                                  angle=angle,
                                  radian_type=radian_type,
                                  err=err)
        elif lattice=='Tetragonal_2':
            a=(a[0],)*2+(a[2],)
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Tetragonal_2(t=t,
                                  t_reverse=t_reverse,
                                  a=a,
                                  angle=angle,
                                  radian_type=radian_type,
                                  err=err)
        elif lattice=='Othorhombic_1':
            a=(a[0],a[1],a[2])
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Othorhombic_1(t=t,
                                   t_reverse=t_reverse,
                                   a=a,
                                   angle=angle,
                                   radian_type=radian_type,
                                   err=err)
        elif lattice=='Othorhombic_2':
            a=(a[0],a[1],a[2])
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Othorhombic_1(t=t,
                                   t_reverse=t_reverse,
                                   a=a,
                                   angle=angle,
                                   radian_type=radian_type,
                                   err=err)
        elif lattice=='Othorhombic_3':
            a=(a[0],a[1],a[2])
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Othorhombic_1(t=t,
                                   t_reverse=t_reverse,
                                   a=a,
                                   angle=angle,
                                   radian_type=radian_type,
                                   err=err)
        elif lattice=='Othorhombic_4':
            a=(a[0],a[1],a[2])
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Othorhombic_1(t=t,
                                   t_reverse=t_reverse,
                                   a=a,
                                   angle=angle,
                                   radian_type=radian_type,
                                   err=err)
        elif lattice=='Monoclinic_1':
            a=(a[0],a[1],a[2])
            angle=(np.pi/2,angle[1],np.pi/2) if radian_type else (90,angle[1],90)
            self.lat=Monoclinic_1(t=t,
                                  t_reverse=t_reverse,
                                  a=a,
                                  angle=angle,
                                  radian_type=radian_type,
                                  err=err)
        elif lattice=='Monoclinic_2':
            a=(a[0],a[1],a[2])
            angle=(np.pi/2,angle[1],np.pi/2) if radian_type else (90,angle[1],90)
            self.lat=Monoclinic_2(t=t,
                                  t_reverse=t_reverse,
                                  a=a,
                                  angle=angle,
                                  radian_type=radian_type,
                                  err=err)
        elif lattice=='Triclinic':
            a=(a[0],a[1],a[2])
            self.lat=Triclinic(t=t,
                               t_reverse=t_reverse,
                               a=a,
                               angle=angle,
                               radian_type=radian_type,
                               err=err)
        elif lattice=='Hexagonal':
            a=(a[0],)*2+(a[2],)
            angle=(2*np.pi/3,0,0) if radian_type else (120,0,0)
            self.lat=Hexagonal(t=t,
                               t_reverse=t_reverse,
                               a=a,
                               angle=angle,
                               radian_type=radian_type,
                               err=err)
        elif lattice=='Trigonal':
            a=(a[0],)*3
            ang1=angle[0] # radian type
            ang2=angle[0]/180*np.pi # degree type
            angle=(ang1,
                   np.arcsin(np.cos(ang1)/np.cos(ang1/2)),
                   ang1/2) if radian_type else (angle[0],
                                                np.arcsin(np.cos(ang2)
                                                          /np.cos(ang2/2))/np.pi*180,
                                                angle[0]/2)
            self.lat=Trigonal(t=t,
                              t_reverse=t_reverse,
                              a=a,
                              angle=angle,
                              radian_type=radian_type,
                              err=err)
        else:
            raise ModuleNotFoundError('No Lattice Named %s'%(lattice))
        self.t=t
        self.a=a[0]
        self.b=a[1]
        self.c=a[2]
        if not radian_type:
            angle=(np.pi/180*angle[0],
                   np.pi/180*angle[1],
                   np.pi/180*angle[2])
        self.alpha=self.lat.alpha
        self.beta=self.lat.beta
        self.gamma=angle[0]
        self.angle_lattice=self.lat.angle_lattice
        self.vector=self.lat.vector
        self.theta=angle[1]
        self.phi=angle[2]
        self.angle=(self.gamma,self.theta,self.phi)
        self.lattice=self.lat.lattice
        self.reciprocal=self.lat.reciprocal
        self.normal=self.lat.normal
        self.V=self.lat.V
        self.lattice_V=self.lat.lattice_V
        self.reciprocal_V=self.lat.reciprocal_V
        self.order=self.lat.order

    def energy(self,kx,ky,kz):
        return self.lat.energy(kx,ky,kz)

'''
================================================================================
Plotting the energy in k-space
variable:
func: input the function name, for exmaple lat.energy
    !! without brace '(' and ')' !!
limit: range for plotting, default (-5,5)
k: tuple with 3 elements representing 3 dimensions of (kx,ky,kz).
    None means this dimension should be plotted
    Default (None,0,0), ky=0,kz=0
n: number of points to plot.Default 100
figsize: figure's size. matplotlib's parameter
label: label of the curve. matplotlib's parameter
linewidth: thickness of curve. matplotlib's parameter
title: title of figure. matplotlib's parameter
xlabel ylabel: label of 3 axis. matplotlib's parameter
show: if figure should be shown at last
    True (default) figure should be shown
savename: saved figure's name.
    None (default) do not save
    'any string.format' save figure in the format of 'format' 
        .eps .jpg .png recommended
================================================================================
'''
def Plot2D(func,limit=(-5,5),k=(None,0,0),n=100,figsize=(8,6),
           label='',linewidth=1.0,title='',xlabel=None,ylabel='',show=True,
           savename=None):
    if type(func).__name__=='Lattice':
        func=func.energy
    plt.figure(figsize=figsize)
    x=np.linspace(limit[0],limit[1],n)
    y=[]
    for i in x:
        if k[0]==None:
            k_vec='$k_{x}$'
            y.append(func(i,k[1],k[2]))
        elif k[1]==None:
            k_vec='$k_{y}$'
            y.append(func(k[0],i,k[2]))
        elif k[2]==None:
            k_vec='$k_{z}$'
            y.append(func(k[0],k[1],i))
    plt.plot(x,y,label=label,linewidth=linewidth)
    plt.grid()
    plt.title(title)
    plt.xlabel(k_vec if xlabel==None else xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    if not isinstance(savename,(str,tuple,list)) and savename!=None:
        raise TypeError('Type of %s not supported'%(str(type(savename)[8:-2])))
    elif savename!=None:
        if type(savename)==str:
            plt.savefig(savename)
        else:
            for i in savename:
                if not isinstance(i,str) and savename!=None:
                    raise TypeError('Type of %s not supported'%(str(type(savename)[8:-2])))
                elif savename!=None:
                    plt.savefig(savename)
    if show:
        plt.show()

def Plot3D(func,limit=((-5,5),(-5,5)),k=(None,None,0),n=(50,50),
           xlabel=None,ylabel=None,zlabel='',show=True,
           savename=None):
    if type(func).__name__=='Lattice':
        func=func.energy
    fig=plt.figure()
    ax=fig.gca(projection='3d')
    X=np.linspace(limit[0][0],limit[0][1],n[0])
    Y=np.linspace(limit[1][0],limit[1][1],n[1])
    X,Y=np.meshgrid(X,Y)
    Z=[]
    i=0
    while i<n[1]:
        Z.append([])
        j=0
        while j<n[0]:
            if k[0]==None and k[1]==None:
                Z[-1].append(func(X[j][i],Y[j][i],k[2]))
            elif k[0]==None and k[2]==None:
                Z[-1].append(func(X[j][i],k[1],Y[j][i]))
            elif k[1]==None and k[2]==None:
                Z[-1].append(func(k[0],X[j][i],Y[j][i]))
            j=j+1
        i=i+1
    Z=np.array(Z)
    if k[0]==None and k[1]==None:
        xlabel='kx' if xlabel==None else xlabel
        ylabel='ky' if ylabel==None else ylabel
    elif k[0]==None and k[2]==None:
        xlabel='kx' if xlabel==None else xlabel
        ylabel='kz' if ylabel==None else ylabel
    elif k[1]==None and k[2]==None:
        xlabel='ky' if xlabel==None else xlabel
        ylabel='kz' if ylabel==None else ylabel
    ax.set_xlabel(xlabel, color='r')
    ax.set_ylabel(ylabel, color='g')
    ax.set_zlabel(zlabel, color='b')
    surf = ax.plot_surface(X,Y,Z,
                           rstride=1,cstride=1,cmap=cm.coolwarm,
                           linewidth=0,antialiased=False)
    z=[]
    for i in Z:
        z=z+list(i)
    ax.set_zlim(min(z)-0.3*abs(max(z)-min(z)),max(z)+0.3*abs(max(z)-min(z)))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    if not isinstance(savename,(str,tuple,list)) and savename!=None:
        raise TypeError('Type of %s not supported'%(str(type(savename)[8:-2])))
    elif savename!=None:
        if type(savename)==str:
            plt.savefig(savename)
        else:
            for i in savename:
                if not isinstance(i,str) and savename!=None:
                    raise TypeError('Type of %s not supported'%(str(type(savename)[8:-2])))
                elif savename!=None:
                    plt.savefig(savename)
    if show:
        plt.show()

'''
================================================================================
plotting Wigner Seitz unit cell
********************************************************************************
Wigner_Seitz_unit_cell_condition
variable:
vector: primitive vectors of a lattice, like
    ((x1,y1,z1),(x2,y2,z2),(x3,y3,z3))
    can also input the class Lattice directly
return a tuple of condition
    for example, return ((a,b,c,d),...), then all the points (x,y,z) in the WS
    cell satisfy
    a*x+b*y+c*z+d<0,...
********************************************************************************
is_in_condition
variable:
point: coordinate of the testing point.
    (1,1,1) for example
condition: that has been explained in Wigner_Seitz_unit_cell_condition
    ((a,b,c,d),...)
********************************************************************************
Plot3D_WS_cell:
variable:
condition: that has been explained in Wigner_Seitz_unit_cell_condition
n: index of the plot point.
    If n is huge, the edge of cell's plane will get closer, but not smooth when 
        turning the perspective.
show_point: show the lattice points that make contributions to the form of WS
    cell
show_line: show the connection lines between center point and the points that
    make contributions to the form of WS cell, which illustrate how they form
    the cell.
xlabel ylabel: label of 3 axis. matplotlib's parameter
show: if figure should be shown at last
    True (default) figure should be shown
savename: saved figure's name.
    None (default) do not save
    'any string.format' save figure in the format of 'format' 
        .eps .jpg .png recommended
================================================================================
'''
def is_in_condition(point,condition,err=10**-8):
    for i in condition:
        l=np.sqrt(point[0]**2+point[1]**2+point[2]**2)
        x=point[0]/l;y=point[1]/l;z=point[2]/l
        dd=(point[0]*x+point[1]*y+point[2]*z)*err
        d=point[0]*i[0]+point[1]*i[1]+point[2]*i[2]+i[3]
        d1=d-dd;d2=d+dd
        if d>0 and d1>0 and d2>0:
            return False
    return True

def Wigner_Seitz_unit_cell_condition(vector):
    # step 1: find all points may form the WS cell
    points=[]
    condition=[]
    n=1
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            for k in range(-n,n+1):
                if (i,j,k)==(0,0,0):
                    continue
                points.append(tuple( i*np.array(vector[0])
                                    +j*np.array(vector[1])
                                    +k*np.array(vector[2]) ))
                d=(points[-1][0]**2/2
                   +points[-1][1]**2/2
                   +points[-1][2]**2/2)
                condition.append( points[-1]+(-d,) )
    n=2
    n_condition=len(condition)
    flag=True
    while flag:
        for i in range(-n,n+1):
            for j in range(-n,n+1):
                for k in range(-n,n+1):
                    if (i,j,k)==(0,0,0) or (i,j,k) in points:
                        continue
                    points.append(tuple( i*np.array(vector[0])
                                        +j*np.array(vector[1])
                                        +k*np.array(vector[2]) ))
                    if is_in_condition(points[-1],condition):
                        d=(points[-1][0]**2/2
                           +points[-1][1]**2/2
                           +points[-1][2]**2/2)
                        condition.append( points[-1]+(-d,) )
        # if no more point can be considered in a bigger lattice area
        if n_condition==len(condition):
            break
        n_condition=len(condition)
        n=n+1
    # step 2: eliminate the ineffective condition(s)
    c=[]
    i=0
    while i<n_condition:
        if is_in_condition(tuple(np.array(condition[i][:3])/2),
                           condition[:i]+condition[i+1:]):
            c.append(condition[i])
        i=i+1
    while len(c)!=n_condition:
        condition=copy.deepcopy(c)
        n_condition=len(c)
        c=[] # new condition: with effective condition(s)
        i=0
        while i<n_condition:
            if is_in_condition(tuple(np.array(condition[i][:3])/2),
                               condition[:i]+condition[i+1:]):
                c.append(condition[i])
            i=i+1
    return c

def Plot3D_WS_cell(vector,n=100,err=10**-8,
                   show_point=True,show_line=False,
                   rstride=1,cstride=1,cmap='rainbow',
                   xlabel=None,ylabel=None,zlabel=None,
                   show=True,savename=None):
    if type(vector).__name__=='Lattice':
        vector=vector.vector
    vector=refine_vector(vector)
    condition=Wigner_Seitz_unit_cell_condition(vector)
    scale=2*max([np.linalg.norm(i[:3]) for i in condition])
    rang=tuple(np.linspace(-scale,scale,n))
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1,projection='3d')
    ax.scatter(0,0,0,color='red',label='Center atom')
    nearby_atoms=[[],[],[],]
    n_=len(condition)
    i=0
    while i<n_:
        c=condition[i]
        nearby_atoms[0].append(c[0])
        nearby_atoms[1].append(c[1])
        nearby_atoms[2].append(c[2])
        if show_line:
            ax.plot((0,c[0]),(0,c[1]),(0,c[2]),color='lightblue',linewidth=1.0)
        x=[];y=[];z=[]
        if c[2]==0 and c[0]==0: # a=0 c=0
            # x_m [x1,             x2,             ...]
            # z_m [[z1.1,z1.2,...],[z2.1,z2.2,...],...]
            y_=-c[3]/c[1] # y is a constant in this case
            x_m=[];z_m=[]
            j=0
            while j<n:
                x_m.append(rang[j])
                z_m.append([])
                k=0
                while k<n:
                    if is_in_condition((rang[j],y_,rang[k]),
                                       condition[:i]+condition[i+1:],err=err):
                        z_m[-1].append(rang[k])
                    k=k+1
                if z_m[-1]==[]:
                    x_m.pop();z_m.pop()
                j=j+1
            n_x_m=len(x_m)
            j=0
            while j<n_x_m:
                x.append((x_m[j],)*n)
                y.append((y_,)*n)
                z.append(np.linspace(min(z_m[j]),max(z_m[j]),n))
                j=j+1
            x=np.transpose(x)
            y=np.transpose(y)
            z=np.transpose(z)
        elif c[2]==0 and c[1]==0: # b=0 c=0
            # y_m [y1,             y2,             ...]
            # z_m [[z1.1,z1.2,...],[z2.1,z2.2,...],...]
            x_=-c[3]/c[0] # x is a constant in this case
            y_m=[];z_m=[]
            j=0
            while j<n:
                y_m.append(rang[j])
                z_m.append([])
                k=0
                while k<n:
                    if is_in_condition((x_,rang[j],rang[k]),
                                       condition[:i]+condition[i+1:],err=err):
                        z_m[-1].append(rang[k])
                    k=k+1
                if z_m[-1]==[]:
                    y_m.pop();z_m.pop()
                j=j+1
            n_y_m=len(y_m)
            j=0
            while j<n_y_m:
                x.append((x_,)*n)
                y.append((y_m[j],)*n)
                z.append(np.linspace(min(z_m[j]),max(z_m[j]),n))
                j=j+1
            x=np.transpose(x)
            y=np.transpose(y)
            z=np.transpose(z)
        elif c[2]==0:
            # x_m [x1,             x2,             ...]
            # z_m [[z1.1,z1.2,...],[z2.1,z2.2,...],...]
            x_m=[];z_m=[]
            j=0
            while j<n:
                x_m.append(rang[j])
                y_=-(c[0]*rang[j]+c[3])/c[1]
                z_m.append([])
                k=0
                while k<n:
                    if is_in_condition((rang[j],y_,rang[k],),
                                       condition[:i]+condition[i+1:],err=err):
                        z_m[-1].append(rang[k])
                    k=k+1
                if z_m[-1]==[]:
                    x_m.pop();z_m.pop()
                j=j+1
            n_x_m=len(x_m)
            j=0
            while j<n_x_m:
                x.append((x_m[j],)*n)
                y.append((-(c[0]*x_m[j]+c[3])/c[1],)*n)
                z.append(np.linspace(min(z_m[j]),max(z_m[j]),n))
                j=j+1
            x=np.transpose(x)
            y=np.transpose(y)
            z=np.transpose(z)
        else:
            x_m=[];y_m=[]
            for j in rang:
                x_m.append(j)
                y_m.append([])
                for k in rang:
                    z_temp=-( c[0]*j+c[1]*k+c[3] )/c[2]
                    if is_in_condition((j,k,z_temp),
                                       condition[:i]+condition[i+1:],err=err):
                        y_m[-1].append(k)
                if y_m[-1]==[]:
                    x_m.pop();y_m.pop()
            n_x_m=len(x_m)
            j=0
            while j<n_x_m:
                x.append((x_m[j],)*n)
                y.append(np.linspace(min(y_m[j]),max(y_m[j]),n))
                z_temp=[]
                for k in range(n):
                    z_temp.append(-( c[0]*x[-1][k]+c[1]*y[-1][k]+c[3] )/c[2])
                z.append(z_temp)
                j=j+1
            x=np.transpose(x)
            y=np.transpose(y)
            z=np.transpose(z)
        if len(z)!=0:
            ax.plot_surface(x,y,z,
                            rstride=rstride,cstride=cstride,cmap=cmap)
        i=i+1
    if show_point:
        ax.scatter(nearby_atoms[0],nearby_atoms[1],nearby_atoms[2],
                   'm',label='Nearby atoms')
    ax.set_xlabel('x' if xlabel==None else xlabel,color='r')
    ax.set_ylabel('y' if ylabel==None else ylabel,color='g')
    ax.set_zlabel('z' if zlabel==None else zlabel,color='b')
    plt.legend()
    if not isinstance(savename,(str,tuple,list)) and savename!=None:
        raise TypeError('Type of %s not supported'%(str(type(savename)[8:-2])))
    elif savename!=None:
        if type(savename)==str:
            plt.savefig(savename)
        else:
            for i in savename:
                if not isinstance(i,str) and savename!=None:
                    raise TypeError('Type of %s not supported'%(str(type(savename)[8:-2])))
                elif savename!=None:
                    plt.savefig(savename)
    if show:
        plt.show()

'''
================================================================================
Plotting lattice's points
variable:
vector: 3 primitive vectors, can also input the "Lattice" class directly
layer: how many cells ((2*layer)^3) to be plotted
color: the atoms' color
show_quiver: show 3 primitive vectors or not
quiver_color: 3 primitive vectors' color
refine_vec: get the shortest primitive vectors or not
xlabel ylabel: label of 3 axis. matplotlib's parameter
show: if figure should be shown at last
    True (default) figure should be shown
savename: saved figure's name.
    None (default) do not save
    'any string.format' save figure in the format of 'format' 
        .eps .jpg .png recommended
================================================================================
'''
def PlotLattice(vector,layer=1,color='red',
                show_quiver=True,quiver_color='blue',refine_vec=False,
                xlabel=None,ylabel=None,zlabel=None,
                savename=None,show=True):
    if type(vector).__name__=='Lattice':
        vector=vector.vector
    if refine_vec:
        vector=refine_vector(vector)
    x=np.array(vector[0]);y=np.array(vector[1]);z=np.array(vector[2])
    vecs=[[],[],[],]
    # use matplotlib
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1,projection='3d')
    # list all the lattice points to be plotted
    for i in range(-abs(layer),abs(layer)+1):
        for j in range(-abs(layer),abs(layer)+1):
            for k in range(-abs(layer),abs(layer)+1):
                new_vec=i*x+j*y+k*z
                vecs[0].append(new_vec[0])
                vecs[1].append(new_vec[1])
                vecs[2].append(new_vec[2])
    ax.scatter(vecs[0],vecs[1],vecs[2],label='Lattice points',color=color)
    if show_quiver:
        qui=[[0,0,0],[0,0,0],[0,0,0],
             [x[0],y[0],z[0]],[x[1],y[1],z[1]],[x[2],y[2],z[2]],]
        ax.quiver(qui[0],qui[1],qui[2],qui[3],qui[4],qui[5],
                  color=quiver_color,label='Primitive Vector')
    ax.set_xlabel('x' if xlabel==None else xlabel,color='r')
    ax.set_ylabel('y' if ylabel==None else ylabel,color='g')
    ax.set_zlabel('z' if zlabel==None else zlabel,color='b')
    plt.legend()
    if not isinstance(savename,(str,tuple,list)) and savename!=None:
        raise TypeError('Type of %s not supported'%(str(type(savename)[8:-2])))
    elif savename!=None:
        if type(savename)==str:
            plt.savefig(savename)
        else:
            for i in savename:
                if not isinstance(i,str) and savename!=None:
                    raise TypeError('Type of %s not supported'%(str(type(savename)[8:-2])))
                elif savename!=None:
                    plt.savefig(savename)
    if show:
        plt.show()