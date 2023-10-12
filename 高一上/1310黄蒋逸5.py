year=int(input("请输入年份："))
month=int(input("请输入月份："))
day=int(input("请输入日期："))
n=[0,31,28,31,30,31,30,31,31,30,31,30,31]
i=1
sum=0
if month>=2:
    if year%4==0:
        n[2]=29
    else:
        if year%4==0 and year%100!=0:
            n[2]=29
while i<month:
    sum=sum+n[i]
    i=i+1
print("是第",sum+day,"天")
    
