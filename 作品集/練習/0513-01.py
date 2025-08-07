# 圓面積=半徑x半徑x3.14
# 圓周長 = 2πr

# 圓心x,y

import math

class Circle:
    def __init__(self,xx,yy,rr):
        self.x=xx
        self.y=yy
        self.r=rr
    def area(self):
        
        return round(self.r**2*math.pi,2)
    def length(self):
        
        return round(self.r*2*math.pi,2)
if __name__=="__main__":
    xx=int(input("x:"))
    yy=int(input("y:"))
    rr=int(input("r:"))
    z=Circle(xx,yy,rr)
    print("圓面積=",z.area())
    print("圓周長=",z.length())