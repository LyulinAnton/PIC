G = 6.67408*1e-1 #м^3/(кг*с^2)

class CB(): #CelestialBody
      dt = 0.0001
      def __init__(self, x, vx, y, vy, z, vz, m):
            self.x   = x
            self.y   = y
            self.z   = z
            self.vx  = vx
            self.vy  = vy
            self.vz  = vz
            self.m   = m
            #self.ind = ind
            
      def get_coord(self, y):
            x, vx, y, vy, z, vz = y
            self.x  = x
            self.vx = vx
            self.y  = y
            self.vy = vy
            self.z  = z
            self.vz = vz
      
def get_trj(arr):
      init = []
      for el in arr:
            init.extend((el.x, el.y, el.z))
      return init