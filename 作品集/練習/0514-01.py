# 自訂Ball類別繼承Circle
# 有建構子 __init__(self,x,y,半徑)
# 方法BallArea()球面積   4*pi*r2 
#     BallVolume()球体積 4/3*pi*r3 

import math
class Circle:
    def __init__(self,xx,yy,rr):
        self.x=xx
        self.y=yy
        self.r=rr
        
class Ball(Circle):
    def __init__(self,xx,yy,rr):
        super().__init__(xx,yy,rr)
        
    def BallArea(self):
        return self.r**2*4*math.pi        
     
    def BallVolume(self):
        return self.r**2*(3/4)*math.pi
    
    
ball=Ball(0,0,15)
print("球面積:",ball.BallArea())
print("球面積:",ball.BallVolume())
    