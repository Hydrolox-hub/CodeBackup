year=int(input("请输入某年的年份："))
isleapyear=(year%4==0 and year%100!=0)or(year%400==0)
if isleapyear:
    print("闰年")
else:
    print("平年")
