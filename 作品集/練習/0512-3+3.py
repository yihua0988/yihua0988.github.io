# 使用set集合,製作一個包牌程式,玩家輸入3個包牌號碼,另外3個使用random產生,並輸入購買金額(1注50元),產生多組包牌組合?

print("輸入3個包牌號碼(1~49),另外3個隨產生")

x=int(input("請輸入購買金額(每注50元):"))
z=int(x/50)


import random


pc=set(range(1,49))
user=set()

while len(user)<3:
    try:
        n=int(input("數字:"))
        if not (1<=n<=49):
            raise Exception("請輸入1~49")
        if n in user:
            print("號碼重複")
            continue
           
    
        user.add(n) 
        # u2=set(random.sample(range(1,10),3))
        # if u2 in n:
        #     continue
    except Exception as e:
        print(e)

print("您的號碼:")
i=0
for i in range(z):

    while True:
        u2=set(random.sample(range(1,49),3))
        if u2.isdisjoint(user):  
            break
        
        # if u2 in n:
        #     
    a=user|u2
    print(a) 
    i+=1
# s=list.count(a)
# print(s)


pc=set(random.sample(range(1,49),6))
data=pc&a
count=len(data)
if count>0:
              print("你中",count,"個")
              print(data)
else:
              print("你都沒中")    
            
print("pc=",pc)

# print("pc=",sorted(pc))

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

# data=user&pc
# count=len(data)
# if count>0:
#               print("你中",count,"個")
#               print(data)
# else:
#               print("你都沒中")    
        
    
