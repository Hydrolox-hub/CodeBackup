import random
k=random.randint(0,100)
m=int(input("您猜的数字："))
n=3
while n >0:
    if m==k:
        print("恭喜猜对！")
        n=n-1
        break
    if m>k:
        print("偏大")
        n=n-1
        m=int(input("您猜的数字："))
    if m<k:
        print("偏小")
        n=n-1
        m=int(input("您猜的数字："))
    if n==0:
        print("很遗憾，猜错了，答案是：",k)
        break
