n=int(input('十进制数：'))
str1=''
while n!=0:
    mod=n%2
    n=n//2
    str1=str(mod)+str1
print('二进制数：' + str1)

    
