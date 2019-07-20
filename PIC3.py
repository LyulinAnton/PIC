from math import sqrt, pi, modf
from CB3d import CB, get_trj, G
import numpy as np
from Poisson_fft import Poisson3D

#======================================================================
#N = int(40) # 2*N+1 ячеек на одной оси 
N = int(50)
L = 25 # на самом деле +h
d = 2
h = L/N
print('h/10 = ', h/10)

Net = np.full((2*N+1,2*N+1,2*N+1), 0, np.float64)
PHI = np.full((2*N+1,2*N+1,2*N+1), 0, np.float64)

m       = np.float128(1)
v       = np.float128(0.3)
T       = np.float128(20)
step    = np.float128(0.1)
d       = np.float128(-0.3)
max_h   = np.float128(1)
antirez = np.float128(0)
Np      = 50

left_y = np.linspace(0, max_h, Np)
left_y = list(map(np.float128, left_y))

matrix = [(x,y) for x in left_y for y in left_y]
leftBodies  = [CB(-0.4, +v, +x[0]-0.3, 0, +x[1]-0.3, 0, m) for x in matrix]
rightBodies = [CB(+0.4, -v, -x[0]+0.3, 0, -x[1]+0.3, 0, m) for x in matrix]
Cbarr = leftBodies + rightBodies
#======================================================================

def density(Net, PHI, L, h):
      global d
      global Cbarr
      global N
      '''считаем плотности'''
      Net = np.full((2*N+1,2*N+1,2*N+1), 0, np.float64)
      PHI = np.full((2*N+1,2*N+1,2*N+1), 0, np.float64)
      print(len(Cbarr))
      for k1,el in enumerate(Cbarr):
            i = int((el.x+h/2)//h)+int(N)
            j = int((el.y+h/2)//h)+int(N)
            k = int((el.z+h/2)//h)+int(N)
            if((i>=0+1 and i<int(2*N+1-1)) and (j>=0+1 and j<int(2*N+1-1)) and (k>=0+1 and k<int(2*N+1-1))):
                  Net[i,j,k]+=1
            else:
                  del Cbarr[k1]
      
      PHI = Poisson3D(Net, L)
      return PHI

def Force(PHI, L, h, dt):
      global Cbarr
      global N
      
      
      for k1,el in enumerate(Cbarr):
            i = int((el.x+h/2)//h)+int(N)
            j = int((el.y+h/2)//h)+int(N)
            k = int((el.z+h/2)//h)+int(N)
            
            Fx=0
            Fy=0
            Fz=0
            
            try:
                  if(i>0 and i<int(2*N)):
                        Fx = (PHI[i+1,j,k]-PHI[i-1,j,k])/(2*h)
                  if(j>0 and j<int(2*N)):
                        Fy = (PHI[i,j+1,k]-PHI[i,j-1,k])/(2*h)
                  if(k>0 and k<int(2*N)):
                        Fz = (PHI[i,j,k+1]-PHI[i,j,k-1])/(2*h)
            except:
                  del Cbarr[k1]
                  
        
            
            el.vx = Fx*dt+el.vx
            el.vy = Fy*dt+el.vy
            el.vz = Fz*dt+el.vz
            el.x = el.vx*dt+el.x
            el.y = el.vy*dt+el.y
            el.z = el.vz*dt+el.z


import time
a = time.monotonic()
for k in range(int(T//step)):
      with open('tmpalt.txt', 'a') as f:
            for el in get_trj(Cbarr):
                  f.write(str(el)+' ')
            f.write('\n')
      print(k,'/',int(T//step)-1)
      b = time.monotonic()
      print(b-a)
      print('len =', len(Cbarr))
      a=b
      PHI = density(Net, PHI, L,h)
      Force(PHI, L, h, step)
with open('tmpalt.txt', 'a') as f:
            for el in get_trj(Cbarr):
                  f.write(str(el)+' ')
            f.write('\n')      

      
