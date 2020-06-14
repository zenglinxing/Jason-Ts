import numpy as np

# t: tight binding energy
# angle: shown as vector-convention. (gamma,theta,phi)
# readian_type: True if angle input is in radian. Default False
# err: if two lengths are close, regarded as the same (as the smaller one)
class Tetragonal_1():
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
        # order
        length_=tuple(sorted( (self.a,self.b,self.c) )) # all lengths
        length_angle=[[self.a,(np.pi/2,0)],
                      [self.b,(np.pi/2,np.pi/2)],
                      [self.c,(0,0)]]
        length=() # lengths eliminating the closer
        l_=length_[0]
        length=(l_,)
        # dic={length:((theta,phi),(theta,phi),...)}
        dic={l_:()}
        for j in length_angle:
            if l_==j[0]:
                dic[l_]=dic[l_]+(j[1],)
        pre=l_
        for i in length_[1:]:
            if l_==i or i==pre:
                continue
            if abs(i-l_)<=err and i-l_!=0:
                for j in length_angle:
                    if i==j[0]:
                        dic[l_]=dic[l_]+(j[1],)
            else:
                dic[i]=()
                for j in length_angle:
                    if i==j[0]:
                        dic[i]=dic[i]+(j[1],)
                length=length+(i,)
                l_=i
            pre=i
        n_l=len(length)
        n=min(n_l,n_t)
        order=()
        i=0
        while i<n:
            ang=dic[length[i]] # tuple (a,a,...,a)
            l=length[i]
            vec=()
            for j in ang:
                vec=vec+( (l*np.sin(j[0])*np.cos(j[1]),
                           l*np.sin(j[0])*np.sin(j[1]),
                           l*np.cos(j[0]),) ,)
            order=order+( (l,ang,vec,self.t[i],) ,)
            i=i+1
        self.order=order

    def energy(self,kx,ky,kz):
        f=0
        for i in self.order:
            for j in i[2]:
                f=f-2*i[-1]*np.cos(j[0]*kx
                                   +j[1]*ky
                                   +j[2]*kz)
        return f

class Tetragonal_2():
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
        # order
        length_=tuple(sorted( (self.a,
                               self.b,
                               self.c,
                               np.sqrt(self.a**2
                                       +self.b**2
                                       +self.c**2)/2,) )) # all lengths
        length_angle=[ [self.a,(np.pi/2,0)],
                      [self.b,(np.pi/2,np.pi/2)],
                      [self.c,(0,0)],
                      [np.sqrt(self.a**2
                               +self.b**2+self.c**2)/2,
                       (np.arctan(np.sqrt(self.a**2
                                          +self.b**2)/self.c),
                        np.pi/4)],
                      [np.sqrt(self.a**2
                               +self.b**2+self.c**2)/2,
                       (np.arctan(np.sqrt(self.a**2
                                          +self.b**2)/self.c),
                        -np.pi/4)],
                      [np.sqrt(self.a**2
                               +self.b**2+self.c**2)/2,
                       (-np.arctan(np.sqrt(self.a**2
                                           +self.b**2)/self.c),
                        np.pi/4)],
                      [np.sqrt(self.a**2
                               +self.b**2+self.c**2)/2,
                       (-np.arctan(np.sqrt(self.a**2
                                           +self.b**2)/self.c),
                        -np.pi/4)], ]
        length=() # lengths eliminating the closer
        l_=length_[0]
        length=(l_,)
        # dic={length:((theta,phi),(theta,phi),...)}
        dic={l_:()}
        for j in length_angle:
            if l_==j[0]:
                dic[l_]=dic[l_]+(j[1],)
        pre=l_
        for i in length_[1:]:
            if l_==i or i==pre:
                continue
            if abs(i-l_)<=err and i-l_!=0:
                for j in length_angle:
                    if i==j[0]:
                        dic[l_]=dic[l_]+(j[1],)
            else:
                dic[i]=()
                for j in length_angle:
                    if i==j[0]:
                        dic[i]=dic[i]+(j[1],)
                length=length+(i,)
                l_=i
            pre=i
        n_l=len(length)
        n=min(n_l,n_t)
        order=()
        i=0
        while i<n:
            ang=dic[length[i]] # tuple (a,a,...,a)
            l=length[i]
            vec=()
            for j in ang:
                vec=vec+( (l*np.sin(j[0])*np.cos(j[1]),
                           l*np.sin(j[0])*np.sin(j[1]),
                           l*np.cos(j[0]),) ,)
            order=order+( (l,ang,vec,self.t[i],) ,)
            i=i+1
        self.order=order

    def energy(self,kx,ky,kz):
        f=0
        for i in self.order:
            for j in i[2]:
                f=f-2*i[-1]*np.cos(j[0]*kx
                                   +j[1]*ky
                                   +j[2]*kz)
        return f