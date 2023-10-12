n=int(input("请输入数字:"))
while n!= 1:
    if n%2 == 0:
        n = n //2
    else:
        n = n*3+1
    print(n)
