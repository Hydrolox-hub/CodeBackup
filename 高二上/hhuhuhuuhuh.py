dic={"(":2,")":2,"+":0,"-":0,"*":1,"/":1}
st=''
s=[-1]*100
top=-1
a=input('请输入中缀表达式：')
j=0

for i in a:
    if i==" " and "0"<=a[j]<="9":
        x=a[j:int(a.find(i)+1)]
        st=st+x+" "
        j=int(x)+1
    elif i=="(":
        top+=1
        s[top]=i
    elif s[top]=="(" or top==-1 or dic[s[top]]<=dic[i]:
        top+=1
        s[top]=i
    elif dic[s[top]]>dic[i]:
         st=st+i+" "
    else:
        st=st+s[top]+" "
        top-=2
while top!=-1:
     st=st+s[top]+" "
     top-=1
print(st)
