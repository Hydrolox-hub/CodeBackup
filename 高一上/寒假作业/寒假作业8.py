def su(a):
    for i in range(2,a):
        t=a%i
        if t==0:
            return False
    return True
k=int(input())
if su(k)==True:
    print("是素数")
else:
    print("不是素数")
