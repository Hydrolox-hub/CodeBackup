from random import randint
data_a=[]
head_a=-1
data_b=[]
head_b=-1

tmp=randint(95,100)
data_a.append([tmp,head_a]) #添加第一个结点
head_a=0
for i in range(1,5):
    tmp=data_a[i-1][0]-randint(1,5)
    data_a.append([tmp,data_a[i-1][1]])   #链表一 尾部添加新结点[tmp,-1]
    data_a[i-1][1]=i
print(" 链表结构的原始数据序列一：")
print(data_a)

tmp=randint(95,100)
data_b.append([tmp,head_b])
head_b=0
for i in range(1,5):
    tmp=data_b[i-1][0]-randint(1,5)
    data_b.append([tmp,data_b[i-1][1]])   #链表二 尾部添加新结点[tmp,-1]
    data_b[i-1][1]=i
print(" 链表结构的原始数据序列二： ")
print(data_b)

k_a=head_a #k_a与k_b指向两个链表中未合并的数据序列中最前面（值最大）的结点
k_b=head_b
q_a=head_a #记录要插入位置的前驱结点

n=0 #记录数据处理的总个数（次数）
while(k_a!=-1 and k_b!=-1):
    n=n+1
    print("---第"+str(n)+"次") 
    if data_a[k_a][0]>=data_b[k_b][0]:
        print("AAA")
        print(data_a)   #输出data_a的数据
        q_a=k_a
        k_a=data_a[k_a][1]
    else:
        if k_a==head_a:  # 在链表 data_a 的头部插入结点
            print("BBB")
            data_a.append([data_b[k_b][0],head_a])
            print(data_a)   #输出data_a的数据
            
            head_a=len(data_a)-1 #新插入的数据成为头结点（最小）
            
            q_a=head_a   #更新q_a
            print(q_a)   #输出q_a的数据
            
            k_b=data_b[k_b][1] #k_b指向链表data_b中的下一个结点          
        else:               # 在链表 data_a 的中间插入结点
            print("CCC") 
            data_a.append([data_b[k_b][0],k_a])
            print(data_a)
            
            data_a[q_a][1]=len(data_a)-1
            print(data_a)
            
            q_a=data_a[q_a][1]
            print(q_a)
            
            k_b=data_b[k_b][1]

while k_b!=-1:
    n=n+1
    print("---第"+str(n)+"次") 
    print("DDD")
    data_a.append([data_b[k_b][0],-1])
    print(data_a)
    
    data_a[q_a][1]=len(data_a)-1
    print(data_a)
    
    q_a=data_a[q_a][1]
    print(q_a)
    
    k_b=data_b[k_b][1]
print(" 链表结构的合并后数据序列: ")
print(data_a)
print(" 按链表链接顺序输出数据序列: ")
tmp=head_a
while data_a[tmp][1]!=-1:
    print(data_a[tmp][0],end=" ")
    tmp=data_a[tmp][1]
print(data_a[tmp][0])