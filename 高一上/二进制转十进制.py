str1=input('二进制数:')
d=0
i=0
while i<len(str1):
    d=2*d+int(str1[i])
    i=i+1
print('十进制数：'+str(d))

