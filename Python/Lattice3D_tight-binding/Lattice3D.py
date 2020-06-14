from Cubic import *
from Tetragonal import *
from Othorhombic import *
from Hexagonal import *
from Trigonal import *
from scipy.integrate import quad
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

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
                 a=(1,1,1),
                 angle=(90,0,0),
                 radian_type=False,
                 err=10**-8):
        # lat
        if lattice=='Cubic_1':
            a=(a[0],)*3
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Cubic_1(t=t,
                             a=a,
                             angle=angle,
                             radian_type=radian_type,
                             err=err)
        elif lattice=='Cubic_2':
            a=(a[0],)*3
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Cubic_2(t=t,
                             a=a,
                             angle=angle,
                             radian_type=radian_type,
                             err=err)
        elif lattice=='Cubic_3':
            a=(a[0],)*3
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Cubic_3(t=t,
                             a=a,
                             angle=angle,
                             radian_type=radian_type,
                             err=err)
        elif lattice=='Tetragonal_1':
            a=(a[0],)*2+(a[2],)
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Tetragonal_1(t=t,
                                  a=a,
                                  angle=angle,
                                  radian_type=radian_type,
                                  err=err)
        elif lattice=='Tetragonal_2':
            a=(a[0],)*2+(a[2],)
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Tetragonal_2(t=t,
                                  a=a,
                                  angle=angle,
                                  radian_type=radian_type,
                                  err=err)
        elif lattice=='Othorhombic_1':
            a=(a[0],a[1],a[2])
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Othorhombic_1(t=t,
                                   a=a,
                                   angle=angle,
                                   radian_type=radian_type,
                                   err=err)
        elif lattice=='Othorhombic_2':
            a=(a[0],a[1],a[2])
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Othorhombic_1(t=t,
                                   a=a,
                                   angle=angle,
                                   radian_type=radian_type,
                                   err=err)
        elif lattice=='Othorhombic_3':
            a=(a[0],a[1],a[2])
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Othorhombic_1(t=t,
                                   a=a,
                                   angle=angle,
                                   radian_type=radian_type,
                                   err=err)
        elif lattice=='Othorhombic_4':
            a=(a[0],a[1],a[2])
            angle=(np.pi/2,0,0) if radian_type else (90,0,0)
            self.lat=Othorhombic_1(t=t,
                                   a=a,
                                   angle=angle,
                                   radian_type=radian_type,
                                   err=err)
        elif lattice=='Hexagonal':
            a=(a[0],)*2+(a[2],)
            angle=(2*np.pi/3,0,0) if radian_type else (120,0,0)
            self.lat=Hexagonal(t=t,
                               a=a,
                               angle=angle,
                               radian_type=radian_type,
                               err=err)
        elif lattice=='Trigonal':
            a=(a[0],)*3
            ang1=angle[0] # radian type
            ang2=angle[0]/np.pi*180 # degree type
            angle=(ang1,
                   np.arcsin(np.cos(ang1)/np.cos(ang1/2)),
                   ang1/2) if radian_type else (ang2,
                                                np.arcsin(np.cos(ang2)
                                                          /np.cos(ang2/2)),
                                                ang2/2)
            self.lat=Trigonal(t=t,
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
        self.angle_vector=self.lat.angle_vector
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

def Plot2D(func,limit=(-5,5),k=(None,0,0),n=100,figsize=(8,6),
           label='',linewidth=1.0,title='',xlabel=None,ylabel='',show=True,
           savename=None):
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
    if isinstance(savename,str):
        plt.savefig(savename)
    elif isinstance(savename,(tuple,list)):
        for i in savename:
            plt.savefig(savename)
    if show:
        plt.show()

def Plot3D(func,limit=((-5,5),(-5,5)),k=(None,None,0),n=(50,50),
           xlabel=None,ylabel=None,zlabel='',show=True,
           savename=None):
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
    if isinstance(savename,str):
        plt.savefig(savename)
    elif isinstance(savename,(tuple,list)):
        for i in savename:
            plt.savefig(savename)
    if show:
        plt.show()