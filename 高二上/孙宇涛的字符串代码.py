a=input('请输入一个任意的字符串：')
num=0
abc=0
upabc=0
el=0
for i in a:
    if '0'<i<'9':
        num+=1
    elif 'a'<i<'z':
        abc+=1
    elif 'A'<i<'Z':
        upabc+=1
    else:
        el+=1
print('数字个数：')
print(num)
print('小写个数：')
print(abc)
print('大写个数：')
print(upabc)
print('其他字符个数：')
print(el)
