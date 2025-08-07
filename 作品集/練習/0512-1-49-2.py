# 使用set集合,製作大樂透(1~49)功能,玩家輸入6個號碼,電腦開獎6個號碼,並對獎?

import random


pc=set(range(1,50))
user=set()

# print(x)
# sum=0
while len(user)<6:
    try:
        n=int(input("數字:"))
        if not (1<=n<=49):
            raise Exception("請輸入1~49")
        if n in user:
            print("號碼重複")
            continue
    
    
        user.add(n) 
    
    
    except Exception as e:
        print(e)


pc=set(random.sample(range(1,49),6))

print("pc=",sorted(pc))

# c=0     
# data=set()
# for i in range (6):
#   if pc.count(user[i])>0:
#         c+=1
          
# if c>0:
#       print("你中",c,"個")
#       print(data)
# else:
#       print("你都沒中")

data=user&pc
count=len(data)
if count>0:
              print("你中",count,"個")
              print(data)
else:
              print("你都沒中")    
        
    
