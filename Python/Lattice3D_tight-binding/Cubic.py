import math
import numpy as np

# t: tight binding energy
# angle: shown as vector-convention. (gamma,theta,phi)
# readian_type: True if angle input is in radian. Default False
# err: if two lengths are close, regarded as the same (as the smaller one)
class Cubic_1():
    def __init__(self,t=1,a=(1,1,1),
                 angle=(90,0,0),radian_type=False,err=10**-8):
        # t
        if isinstance(t,(int,float,complex)):
            self.t=(t,)
        elif isinstance(t,(list,tuple)):
            self.t=tuple(sorted(t))[::-1]
        else:
            raise TypeError('type of '+str(type(t))[8:-2]+' not supported')
        n_t=len(self.t)
        # angle gamma, theta, phi
        self.a=a[0]
        self.b=a[1]
        self.c=a[2]
        if not radian_type:
            angle=(np.pi/180*angle[0],
                   np.pi/180*angle[1],
                   np.pi/180*angle[2])
        self.gamma=angle[0]
        self.theta=angle[1]
        self.phi=angle[2]
        self.angle=(self.gamma,self.theta,self.phi)
        # lattice vector
        self.lattice=((self.a,
                       0,
                       0), # vec a
                      (self.b*np.cos(self.gamma),
                       self.b*np.sin(self.gamma),
                       0), # vec b
                      (self.c*np.sin(self.theta)*np.cos(self.phi),
                       self.c*np.sin(self.theta)*np.sin(self.phi),
                       self.c*np.cos(self.theta))) # vec c
        # angle alpha, beta
        self.alpha=np.arccos(np.dot(self.lattice[0],self.lattice[2])
                             /(np.linalg.norm(self.lattice[0])
                               *np.linalg.norm(self.lattice[2])))
        self.beta=np.arccos(np.dot(self.lattice[1],self.lattice[2])
                            /(np.linalg.norm(self.lattice[1])
                              *np.linalg.norm(self.lattice[2])))
        self.angle_vector=(self.alpha,self.beta,self.gamma)
        self.normal=(tuple(np.cross(self.lattice[0],self.lattice[1])),
                     tuple(np.cross(self.lattice[1],self.lattice[2])),
                     tuple(np.cross(self.lattice[2],self.lattice[0])))
        self.V=np.dot(np.cross(np.array(self.lattice[0]),
                               np.array(self.lattice[1])),
                      np.array(self.lattice[2]))
        self.V=abs(self.V)
        self.lattice_V=self.V
        # reciprocal
        self.reciprocal=(tuple(2*np.pi*np.array(self.normal[0])/self.V),
                         tuple(2*np.pi*np.array(self.normal[1])/self.V),
                         tuple(2*np.pi*np.array(self.normal[2])/self.V))
        self.reciprocal_V=np.dot(np.cross(np.array(self.reciprocal[0]),
                                          np.array(self.reciprocal[1])),
                                 np.array(self.reciprocal[2]))
        # order ((length,
        #        ((theta,phi),(theta,phi),...),
        #        (vector1,vector2,...,),
        #        t),
        #        ...)
        self.order=((self.a,
                     ( (np.pi/2,0),
                       (np.pi/2,np.pi/2),
                       (0,0), ),
                     ((self.a,0,0),
                      (0,self.b,0),
                      (0,0,self.c)),
                     self.t[0]),)

    def energy(self,kx,ky,kz):
        a=np.cos(kx*self.a)+np.cos(ky*self.b)+np.cos(kz*self.c)
        print(a)
        return -2*self.t[0]*a

class Cubic_2():
    def __init__(self,t=1,a=(1,1,1),
                 angle=(90,0,0),radian_type=False,err=10**-8):
        # t
        if isinstance(t,(int,float,complex)):
            self.t=(t,)
        elif isinstance(t,(list,tuple)):
            self.t=tuple(sorted(t))[::-1]
        else:
            raise TypeError('type of '+str(type(t))[8:-2]+' not supported')
        n_t=len(self.t)
        # angle gamma, theta, phi
        self.a=a[0]
        self.b=a[1]
        self.c=a[2]
        if not radian_type:
            angle=(np.pi/180*angle[0],
                   np.pi/180*angle[1],
                   np.pi/180*angle[2])
        self.gamma=angle[0]
        self.theta=angle[1]
        self.phi=angle[2]
        self.angle=(self.gamma,self.theta,self.phi)
        # lattice vector
        self.lattice=((self.a,
                       0,
                       0), # vec a
                      (self.b*np.cos(self.gamma),
                       self.b*np.sin(self.gamma),
                       0), # vec b
                      (self.c*np.sin(self.theta)*np.cos(self.phi),
                       self.c*np.sin(self.theta)*np.sin(self.phi),
                       self.c*np.cos(self.theta))) # vec c
        # angle alpha, beta
        self.alpha=np.arccos(np.dot(self.lattice[0],self.lattice[2])
                             /(np.linalg.norm(self.lattice[0])
                               *np.linalg.norm(self.lattice[2])))
        self.beta=np.arccos(np.dot(self.lattice[1],self.lattice[2])
                            /(np.linalg.norm(self.lattice[1])
                              *np.linalg.norm(self.lattice[2])))
        self.angle_vector=(self.alpha,self.beta,self.gamma)
        self.normal=(tuple(np.cross(self.lattice[0],self.lattice[1])),
                     tuple(np.cross(self.lattice[1],self.lattice[2])),
                     tuple(np.cross(self.lattice[2],self.lattice[0])))
        self.V=np.dot(np.cross(np.array(self.lattice[0]),
                               np.array(self.lattice[1])),
                      np.array(self.lattice[2]))
        self.V=abs(self.V)
        self.lattice_V=self.V
        # reciprocal
        self.reciprocal=(tuple(2*np.pi*np.array(self.normal[0])/self.V),
                         tuple(2*np.pi*np.array(self.normal[1])/self.V),
                         tuple(2*np.pi*np.array(self.normal[2])/self.V))
        self.reciprocal_V=np.dot(np.cross(np.array(self.reciprocal[0]),
                                          np.array(self.reciprocal[1])),
                                 np.array(self.reciprocal[2]))
        # order ((length,
        #        ((theta,phi),(theta,phi),...),
        #        (vector1,vector2,...,),
        #        t),
        #        ...)
        self.order=((np.sqrt(3*self.a**2)/2,
                     ((np.arcsin(2/np.sqrt(3)),np.pi/4),
                      (np.arcsin(2/np.sqrt(3)),3*np.pi/4),
                      (np.arcsin(2/np.sqrt(3)),-np.pi/4),
                      (np.arcsin(2/np.sqrt(3)),-3*np.pi/4),),
                     ((self.a/2,self.b/2,self.c/2),
                      (-self.a/2,self.b/2,self.c/2),
                      (self.a/2,-self.b/2,self.c/2),
                      (-self.a/2,-self.b/2,self.c/2),),
                     self.t[0]),)

    def energy(self,kx,ky,kz):
        a=np.cos( (kx*self.a + ky*self.b + kz*self.c)/2 )
        b=np.cos( (kx*self.a + ky*self.b - kz*self.c)/2 )
        c=np.cos( (kx*self.a - ky*self.b + kz*self.c)/2 )
        d=np.cos( (kx*self.a - ky*self.b - kz*self.c)/2 )
        return -2*self.t[0]*(a+b+c+d)

class Cubic_3():
    def __init__(self,t=1,a=(1,1,1),
                 angle=(90,0,0),radian_type=False,err=10**-8):
        # t
        if isinstance(t,(int,float,complex)):
            self.t=(t,)
        elif isinstance(t,(list,tuple)):
            self.t=tuple(sorted(t))[::-1]
        else:
            raise TypeError('type of '+str(type(t))[8:-2]+' not supported')
        n_t=len(self.t)
        # angle gamma, theta, phi
        self.a=a[0]
        self.b=a[1]
        self.c=a[2]
        if not radian_type:
            angle=(np.pi/180*angle[0],
                   np.pi/180*angle[1],
                   np.pi/180*angle[2])
        self.gamma=angle[0]
        self.theta=angle[1]
        self.phi=angle[2]
        self.angle=(self.gamma,self.theta,self.phi)
        # lattice vector
        self.lattice=((self.a,
                       0,
                       0), # vec a
                      (self.b*np.cos(self.gamma),
                       self.b*np.sin(self.gamma),
                       0), # vec b
                      (self.c*np.sin(self.theta)*np.cos(self.phi),
                       self.c*np.sin(self.theta)*np.sin(self.phi),
                       self.c*np.cos(self.theta))) # vec c
        # angle alpha, beta
        self.alpha=np.arccos(np.dot(self.lattice[0],self.lattice[2])
                             /(np.linalg.norm(self.lattice[0])
                               *np.linalg.norm(self.lattice[2])))
        self.beta=np.arccos(np.dot(self.lattice[1],self.lattice[2])
                            /(np.linalg.norm(self.lattice[1])
                              *np.linalg.norm(self.lattice[2])))
        self.angle_vector=(self.alpha,self.beta,self.gamma)
        self.normal=(tuple(np.cross(self.lattice[0],self.lattice[1])),
                     tuple(np.cross(self.lattice[1],self.lattice[2])),
                     tuple(np.cross(self.lattice[2],self.lattice[0])))
        self.V=np.dot(np.cross(np.array(self.lattice[0]),
                               np.array(self.lattice[1])),
                      np.array(self.lattice[2]))
        self.V=abs(self.V)
        self.lattice_V=self.V
        # reciprocal
        self.reciprocal=(tuple(2*np.pi*np.array(self.normal[0])/self.V),
                         tuple(2*np.pi*np.array(self.normal[1])/self.V),
                         tuple(2*np.pi*np.array(self.normal[2])/self.V))
        self.reciprocal_V=np.dot(np.cross(np.array(self.reciprocal[0]),
                                          np.array(self.reciprocal[1])),
                                 np.array(self.reciprocal[2]))
        # order ((length,
        #        ((theta,phi),(theta,phi),...),
        #        (vector1,vector2,...,),
        #        t),
        #        ...)
        self.order=((np.sqrt(2*self.a**2)/2,
                     ((np.pi/2,np.pi/4),
                      (np.pi/2,3*np.pi/4),
                      (np.pi/4,0),
                      (np.pi/4,np.pi),
                      (np.pi/4,np.pi/2),
                      (np.pi/4,-np.pi/2),),
                     ((self.a/np.sqrt(2),self.b/np.sqrt(2),0),
                      (-self.a/np.sqrt(2),self.b/np.sqrt(2),0),
                      (self.a/np.sqrt(2),0,self.c/np.sqrt(2)),
                      (-self.a/np.sqrt(2),0,self.c/np.sqrt(2)),
                      (0,self.b/np.sqrt(2),self.c/np.sqrt(2)),
                      (0,-self.b/np.sqrt(2),self.c/np.sqrt(2))),
                     t[0]),)

    def energy(self,kx,ky,kz):
        a=np.cos( (kx*self.a + ky*self.b)/2 )
        b=np.cos( (kx*self.a - ky*self.b)/2 )
        c=np.cos( (kx*self.a + kz*self.c)/2 )
        d=np.cos( (kx*self.a - kz*self.c)/2 )
        e=np.cos( (ky*self.b + kz*self.c)/2 )
        f=np.cos( (ky*self.b - kz*self.c)/2 )
        return -2*self.t[0]*(a+b+c+d+e+f)
