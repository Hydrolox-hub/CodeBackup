import random
import math
n=int(input('输入一个完全平方数：'))
print('列表为')
k=[]
s,max,h,l='',0,1,1
for i in range(1,n+1,1):
    a=random.randint(10,99)
    s+=str(a)+','
    if a>max:
        max=a
        h=int((i-1)//math.sqrt(n)+1)
        l=int((i-1)%math.sqrt(n)+1)
    if i%math.sqrt(n)==0:
       
        print(s)
        k.append([h,l,max])
        s,max='',0
for i in range(len(k)):
    h=k[i][0]
    l=k[i][1]
    max=k[i][2]
    print('第',h,'行最大值位于第',l,'列')
    print('最大值为',max)
        