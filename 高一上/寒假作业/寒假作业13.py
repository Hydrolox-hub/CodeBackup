def peach(n):
    if n==10:
        return 1
    else:
        return(peach(n+1)+1)*2
print("第一天桃子的个数：",peach(1))
