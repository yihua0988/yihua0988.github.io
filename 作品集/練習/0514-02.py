# 自訂Triangle類別,有成員變數底和高,
# 方法有建構子__init__(self,底,高)
# 及方法area()面積
# 自訂Volume繼承Triangle,有成員變數高度
# 有建構子__init__(self,底,高,高度)
# 方法有pile()三角柱,taper()三角錐
# 三角柱:底面積*高度
# 三角錐:底面積*高度/3


# import math
class Triangle:
    def __init__(self,底,高):
        self.底=底
        self.高=高
        
    def area(self):
        return self.底*self.高/2
        
class Volume(Triangle):
    def __init__(self,底,高,高度):
        super().__init__(底,高)
        self.高度=高度
        
    def pile(self):
        return self.area()*self.高度   
     
    def taper(self):
        return self.area()*self.高度/3
    
T=Volume(底=2,高=3,高度=5)
print("面積:",T.area())
print("三角柱體積:",T.pile())
print("三角錐體積:",T.taper())    
