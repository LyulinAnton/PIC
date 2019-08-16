import numpy as np
from math import pi, sqrt, sin
import time


def fft3D(arr):
    _N = N+2
    return -np.array(np.fft.fft([0]+list(arr), 2*_N).imag[1:_N])

def Forward(Net, N, L):
    mk3 = np.apply_along_axis(fft3D, 0, Net)                  
    mk2k3 = np.apply_along_axis(fft3D, 1, mk3)
    mk1k2k3 = np.apply_along_axis(fft3D, 2, mk2k3)
    return mk1k2k3

def Back(M, N, L):
    h = L/N
    Vk2k3 = np.zeros([N-1, N-1, N-1])
    for k2 in range(N-1): #Не очень аккуратно, зато быстро пишется
          for k3 in range(N-1):
                for i in range(N-1):
                      for k1 in range(N-1):
                            s1 = sin((k1+1)*pi*h/(2*L))
                            s1*=s1
                            
                            s2 = sin((k2+1)*pi*h/(2*L))
                            s2*=s2
                            
                            s3 = sin((k3+1)*pi*h/(2*L))
                            s3*=s3
                              
                            s = (s1+s2+s3)*(4/(h*h))
                            
                            Vk2k3[k2,k3,i]+=M[k1,k2,k3]*sin((k1+1)*pi*(i+1)/N)/s
    Vk3 = np.apply_along_axis(fft3D, 1, Vk2k3)
    V = (8/(N*N*N))*np.apply_along_axis(fft3D, 0, Vk3)
    return V



def Poisson3D(Net, L):
    '''
    На вход подается кубическая сеть значений функции в правой части уравнения Пуассона
    Сеть должна содержать значения на границе куба - рассматриваемой области.
    L - длина стороны куба
    '''
    N = len(Net[0,0])+1
    M = Forward(Net, N, L)
    V = Back(M, N, L)
    return V
