import os
import numpy as np
import matplotlib.pyplot as plt
import time

def draw_xy():
      global tmp
      global cnt
      print(len(tmp))
      fig = plt.figure(1)
      fig, ax = plt.subplots(1,1)
      ax.set_xlim(-2,2)
      ax.set_ylim(-2,2)
      for k in range(65, (len(tmp)+1)//3):
            if(k<(len(tmp)+1)//6):
                  ax.scatter(tmp[k*3], tmp[k*3+1], s=8, color='blue')
                  #ax.scatter(trj[k*3][l], trj[k*3+1][l], s=8, color='blue')
            else:
                  ax.scatter(tmp[k*3], tmp[k*3+1], s=8, color='red')
                  #ax.scatter(trj[k*3][l], trj[k*3+1][l], s=8, color='red')
      plt.grid(True)
      #fig.savefig('slides/xy/'+str(cnt)+'.png')
      fig.savefig('slides/xy/'+str(cnt)+'.png')
      plt.show()
      del fig
      del ax
      
def draw_xz():
      global tmp
      global cnt
      print(len(tmp))
      fig = plt.figure(1)
      fig, ax = plt.subplots(1,1)
      ax.set_xlim(-2,2)
      ax.set_ylim(-2,2)
      for k in range(65, (len(tmp)+1)//3):
            if(k<(len(tmp)+1)//6):
                  ax.scatter(tmp[k*3], tmp[k*3+2], s=8, color='blue')
                  #ax.scatter(trj[k*3][l], trj[k*3+1][l], s=8, color='blue')
            else:
                  ax.scatter(tmp[k*3], tmp[k*3+2], s=8, color='red')
                  #ax.scatter(trj[k*3][l], trj[k*3+1][l], s=8, color='red')
      plt.grid(True)
      #fig.savefig('slides/xy/'+str(cnt)+'.png')
      fig.savefig('slides/xz/'+str(cnt)+'.png')
      plt.show()
      del fig
      del ax
      
def draw_yz():
      global tmp
      global cnt
      print(len(tmp))
      fig = plt.figure(1)
      fig, ax = plt.subplots(1,1)
      ax.set_xlim(-2,2)
      ax.set_ylim(-2,2)
      for k in range(65, (len(tmp)+1)//3):
            if(k<(len(tmp)+1)//6):
                  ax.scatter(tmp[k*3+1], tmp[k*3+2], s=8, color='blue')
                  #ax.scatter(trj[k*3][l], trj[k*3+1][l], s=8, color='blue')
            else:
                  ax.scatter(tmp[k*3+1], tmp[k*3+2], s=8, color='red')
                  #ax.scatter(trj[k*3][l], trj[k*3+1][l], s=8, color='red')
      plt.grid(True)
      #fig.savefig('slides/xy/'+str(cnt)+'.png')
      fig.savefig('slides/yz/'+str(cnt)+'.png')
      plt.show()
      del fig
      del ax

a = time.monotonic()

      
with open('tmpalt.txt', "r") as fle:
    lines = fle.readlines()
    print(len(lines))
    cnt = 0
    BL = 0
    for line in lines:
          #tmp = f.readline().split()
          tmp = line.split()
          tmp = list(map(float, tmp))
          '''if(cnt>250):
              draw_xy()'''
          if(BL==5 and cnt>830):
              draw_xy()
              #draw_xz()
              #draw_yz()              
              BL=0
          if(cnt<=830):
                BL=0
          BL+=1
          #draw_xy()
          #draw_xz()
          #draw_yz()
          cnt+=1
          b = time.monotonic()
          print(cnt, '   ',BL,'   ', b-a)
          a = b
