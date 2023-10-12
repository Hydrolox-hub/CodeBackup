info=input("请输入十八位居民身份证号码：")
if int(info[16])%2==1:
    xb="男"
else:
    xb="女"
print("您的出生日期为：",info[6:10],"年",info[10:12],"月",info[12:14],"日","性别为：",xb)
