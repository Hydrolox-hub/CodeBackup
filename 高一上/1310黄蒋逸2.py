def huiwen(a):
    if str(a) == str(a)[::-1]:
        return True
    else:
        return False
k=input()
print(huiwen(k))
for i in range(1000, 9999):
    if huiwen(i) == True:
        print(i)
