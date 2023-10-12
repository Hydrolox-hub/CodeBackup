def su(a):
    for i in range(2,a):
        t=a%i
        if t==0:
            return False
    return True
k=int(input())
print(su(k))
for i in range(1,100):
    if su(i)==True:
        print(i)
