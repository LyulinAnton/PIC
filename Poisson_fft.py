import numpy as np
from math import pi, sqrt, sin
import time


def Forward(Net, N, L):
      h = L/N
      mk3 = np.zeros([N-1, N-1, N-1])
      for i in range(N-1):
            for j in range(N-1):
                  mk3[:,i,j] = -np.array(np.fft.fft([0]+list(Net[i,j,:]), 2*N).imag[1:N])
      mk2k3 = np.zeros([N-1, N-1, N-1])
      for k3 in range(N-1):
            for i in range(N-1):
                  mk2k3[:,k3,i] = -np.array(np.fft.fft([0]+list(mk3[k3,i,:]), 2*N).imag[1:N])
      mk1k2k3 = np.zeros([N-1, N-1, N-1])
      for k2 in range(N-1):
            for k3 in range(N-1):
                  mk1k2k3[:,k2,k3] = -np.array(np.fft.fft([0]+list(mk2k3[k2,k3,:]), 2*N).imag[1:N])
      return mk1k2k3

def Back(M, N, L):
      h = L/N
      Vk2k3 = np.zeros([N-1, N-1, N-1])
      for k2 in range(N-1):
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
      Vk3 = np.zeros([N-1, N-1, N-1])
      for k3 in range(N-1):
            for i in range(N-1):
                  Vk3[k3,i,:]=-np.array(np.fft.fft([0]+list(Vk2k3[:,k3,i]), 2*N).imag[1:N])
      V = np.zeros([N-1,N-1,N-1])
      for i in range(N-1):
            for j in range(N-1):
                  V[i,j,:]=-(8/(N*N*N))*np.array(np.fft.fft([0]+list(Vk3[:,i,j]), 2*N).imag[1:N])
      return V



def Poisson3D(Net, L):     
      N = len(Net[0,0])+1
      M = Forward(Net, N, L)
      V = Back(M, N, L)
      return V
