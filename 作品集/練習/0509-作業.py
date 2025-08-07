
# #1.請將str1,str2中的c,C刪除 並將str1,str2合併
str1=set("abcde")
str2=set("ABCDE")
str1.remove("c")
str2.remove("C")
print("1.",str1 | str2)


# #2.請在q2ans中加入元素"a","b”


aq2ans=set()
aq2ans.add("a") 
aq2ans.add("b")
print("2.",aq2ans)


# #3.請將字典q3ans 依序加入{"k1":"v1"}跟{"k2":"v2"}
# q3ans={"k0":"v0"}
q3ans={"k0":"v0"}
a={"k1":"v1"}
b={"k2":"v2"}
print("3.",q3ans|a|b)
    

#4.取出list1中的元素"b”
# list1 = [["a","b"],["c","d"]]
list1 = [["a","b"],["c","d"]]
print("4.",list1[0][1])

# #5.請寫出一迴圈,算出ans5,ans5為1~1024的的總和
# ans5=0
ans5=0
for i in range(1,1025):
 ans5+=i

print("5.",ans5)















