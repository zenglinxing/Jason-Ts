import numpy as np

def vec2angle(vec): # vec=(a,b,c)
    projection=np.sqrt(vec[0]**2+vec[1]**2)
    length=np.sqrt(vec[0]**2+vec[1]**2+vec[2]**2)
    if vec[0]==0: # a=0
        if vec[1]==0: # b=0
            phi=0
            theta=0 if vec[2]>=0 else np.pi
        else: # b!=0
            phi=np.pi/2*vec[1]/abs(vec[1])
            if vec[2]==0:
                theta=np.pi/2
            else:
                theta=np.arctan(abs(vec[1])/vec[2]) if vec[2]>0 else np.pi+np.arctan(abs(vec[1])/vec[2])
    else: # a!=0
        if vec[1]==0: # b=0
            phi=0 if vec[0]>0 else np.pi
            if vec[2]==0: # c=0
                theta=np.pi/2
            else: # c!=0
                theta=np.arctan(abs(vec[0])/vec[2]) if vec[2]>0 else np.pi+np.arctan(abs(vec[0])/vec[2])
        else: # b!=0
            if vec[0]>0:
                phi=np.arctan(vec[1]/vec[0])
            else:
                phi=vec[1]/abs(vec[1])*np.pi+np.arctan(vec[1]/vec[0])
            if vec[2]==0:
                theta=np.pi/2
            else:
                theta=np.arctan(projection/vec[2]) if vec[2]>0 else np.pi+np.arctan(projection/vec[2])
    return theta,phi

# t: tight binding energy
# angle: shown as vector-convention. (gamma,theta,phi)
# readian_type: True if angle input is in radian. Default False
# err: if two lengths are close, regarded as the same (as the smaller one)
class Tetragonal_1():
    def __init__(self,t=1,t_reverse=None,a=(1,1,1),
                 angle=(90,0,0),radian_type=False,err=10**-8):
        # t
        if isinstance(t,(int,float,complex)):
            self.t=(t,)
        elif isinstance(t,(list,tuple)):
            if t_reverse!=None:
                self.t=tuple(sorted(t,reverse=t_reverse))
            else:
                self.t=tuple(t)
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
        self.angle_lattice=(self.alpha,self.beta,self.gamma)
        self.vector=self.lattice
        self.normal=(tuple(np.cross(self.vector[0],self.vector[1])),
                     tuple(np.cross(self.vector[1],self.vector[2])),
                     tuple(np.cross(self.vector[2],self.vector[0])))
        self.V=abs(np.dot(np.cross(np.array(self.vector[0]),
                                   np.array(self.vector[1])),
                          np.array(self.vector[2])))
        self.lattice_V=abs(np.dot(np.cross(np.array(self.lattice[0]),
                                           np.array(self.lattice[1])),
                                  np.array(self.lattice[2])))
        V=(np.dot(np.cross(self.vector[1],
                           self.vector[2]),
                  np.array(self.vector[0])),
           np.dot(np.cross(self.vector[2],
                           self.vector[0]),
                  np.array(self.vector[1])),
           np.dot(np.cross(self.vector[0],
                           self.vector[1]),
                  np.array(self.vector[2])),)
        # reciprocal
        self.reciprocal=(tuple(2*np.pi*np.array(self.normal[1])/V[0]),
                         tuple(2*np.pi*np.array(self.normal[2])/V[1]),
                         tuple(2*np.pi*np.array(self.normal[0])/V[2]),)
        self.reciprocal_V=abs(np.dot(np.cross(np.array(self.reciprocal[0]),
                                              np.array(self.reciprocal[1])),
                                     np.array(self.reciprocal[2])))
        # order
        # lengths of lattice's edge
        lengths=tuple(np.linalg.norm(i) for i in self.lattice)
        n_lengths=np.ceil(max(lengths)/min(lengths))
        # lattice in (-n,n) will be considered
        n=int(2*n_t*n_lengths)
        # list all the possible vectors that may in the neighbor
        possible=[]
        length_=[]
        length_angle=[]
        for h in range(-n,n+1):
            for k in range(-n,n+1):
                for l in range(-n,n+1):
                    if (h,k,l)==(0,0,0):
                        continue
                    possible.append(tuple( h*np.array(self.lattice[0])
                                          +k*np.array(self.lattice[1])
                                          +l*np.array(self.lattice[2]) ))
                    length_.append( np.linalg.norm(possible[-1]) )
                    length_angle.append((length_[-1],
                                         vec2angle(possible[-1]),))
        length_=tuple(sorted(tuple(set(length_))))
        length=() # lengths eliminating the closer
        l_=length_[0]
        length=(l_,)
        # dic={length:((theta,phi),(theta,phi),...)}
        dic={l_:()}
        for j in length_angle:
            if l_==j[0]:
                dic[l_]=dic[l_]+(j[1],)
        for i in length_[1:]:
            if abs(i-l_)<=err:
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
    def __init__(self,t=1,t_reverse=None,a=(1,1,1),
                 angle=(90,0,0),radian_type=False,err=10**-8):
        # t
        if isinstance(t,(int,float,complex)):
            self.t=(t,)
        elif isinstance(t,(list,tuple)):
            if t_reverse!=None:
                self.t=tuple(sorted(t,reverse=t_reverse))
            else:
                self.t=tuple(t)
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
        self.angle_lattice=(self.alpha,self.beta,self.gamma)
        self.vector=(tuple(1/2*(np.array(self.lattice[0])
                                +np.array(self.lattice[1])
                                +np.array(self.lattice[2]))),
                     tuple(1/2*(np.array(self.lattice[0])
                                -np.array(self.lattice[1])
                                +np.array(self.lattice[2]))),
                     tuple(1/2*(np.array(self.lattice[0])
                                +np.array(self.lattice[1])
                                -np.array(self.lattice[2]))),)
        self.normal=(tuple(np.cross(self.lattice[0],self.lattice[1])),
                     tuple(np.cross(self.lattice[1],self.lattice[2])),
                     tuple(np.cross(self.lattice[2],self.lattice[0])))
        self.V=abs(np.dot(np.cross(np.array(self.vector[0]),
                                   np.array(self.vector[1])),
                          np.array(self.vector[2])))
        self.lattice_V=abs(np.dot(np.cross(np.array(self.lattice[0]),
                                           np.array(self.lattice[1])),
                                  np.array(self.lattice[2])))
        V=(np.dot(np.cross(self.vector[1],
                           self.vector[2]),
                  np.array(self.vector[0])),
           np.dot(np.cross(self.vector[2],
                           self.vector[0]),
                  np.array(self.vector[1])),
           np.dot(np.cross(self.vector[0],
                           self.vector[1]),
                  np.array(self.vector[2])),)
        # reciprocal
        self.reciprocal=(tuple(2*np.pi*np.array(self.normal[1])/V[0]),
                         tuple(2*np.pi*np.array(self.normal[2])/V[1]),
                         tuple(2*np.pi*np.array(self.normal[0])/V[2]),)
        self.reciprocal_V=abs(np.dot(np.cross(np.array(self.reciprocal[0]),
                                              np.array(self.reciprocal[1])),
                                     np.array(self.reciprocal[2])))
        # order
        # lengths of lattice's edge
        lengths=tuple(np.linalg.norm(i) for i in self.lattice)
        n_lengths=np.ceil(max(lengths)/min(lengths))
        # lattice in (-n,n) will be considered
        n=int(2*n_t*n_lengths)
        # list all the possible vectors that may in the neighbor
        possible=[]
        length_=[]
        length_angle=[]
        for h in range(-n,n+1):
            for k in range(-n,n+1):
                for l in range(-n,n+1):
                    if (h,k,l)==(0,0,0):
                        possible.append(tuple( h*np.array(self.lattice[0])
                                              +k*np.array(self.lattice[1])
                                              +l*np.array(self.lattice[2])
                                              +1/2*np.array(self.vector[0])
                                              +1/2*np.array(self.vector[1])
                                              +1/2*np.array(self.vector[2]) ))
                        length_.append( np.linalg.norm(possible[-1]) )
                        length_angle.append((length_[-1],
                                             vec2angle(possible[-1]),))
                        continue
                    possible.append(tuple( h*np.array(self.lattice[0])
                                          +k*np.array(self.lattice[1])
                                          +l*np.array(self.lattice[2]) ))
                    length_.append( np.linalg.norm(possible[-1]) )
                    length_angle.append((length_[-1],
                                         vec2angle(possible[-1]),))
                    # if a cell has more than one atom,
                    possible.append(tuple( h*np.array(self.lattice[0])
                                          +k*np.array(self.lattice[1])
                                          +l*np.array(self.lattice[2])
                                          +1/2*np.array(self.vector[0])
                                          +1/2*np.array(self.vector[1])
                                          +1/2*np.array(self.vector[2]) ))
                    length_.append( np.linalg.norm(possible[-1]) )
                    length_angle.append((length_[-1],
                                         vec2angle(possible[-1]),))
        length_=tuple(sorted(tuple(set(length_))))
        length=() # lengths eliminating the closer
        l_=length_[0]
        length=(l_,)
        # dic={length:((theta,phi),(theta,phi),...)}
        dic={l_:()}
        for j in length_angle:
            if l_==j[0]:
                dic[l_]=dic[l_]+(j[1],)
        for i in length_[1:]:
            if abs(i-l_)<=err:
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