import math
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a+b>c and a+c>b and b+c>a:
    p=0.5*(a+b+c)
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print("三角形面积是%.2f"%(area))
else:
    print("不能构成三角形")
