# 自訂Discount繼承Book有成員變數運費,
# 有建構子__init__(self,編號,書名,單價,數量,運費)
# 方法有tal()判斷
# 50000以上  打7折
# 30000~50000  打85折
# 20000~30000  打9折
# 其餘不打折,並加上運費

import bk as b



class Discount(b.Book):
    def __init__(self,編號,書名,單價,數量,運費):
        super().__init__(編號,書名,單價,數量)
        self.運費=運費
    
    def money(self):   
        t=self.tal()
        if t>=50000:
            return (t*0.7)+self.運費
        elif 30000<t<50000:
            return (t*0.85)+self.運費
        elif 20000<t<=30000:
            return (t*0.9)+self.運費 
        
        else:   
            return t+self.運費


