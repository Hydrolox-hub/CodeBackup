from random import randint
n=[[0 for i in range(2)]for j in range(10)]
data=randint(1, 100)
n[0][0]=data    #第1个结点赋值
n[0][1]=-1   
print("第1个结点：[" +str(data)+",-1]") 
 
head=0          #初始化头结点 
for i in range(1,10):
    data=randint(1, 100)  
    n[i][0]=data    #第i+1个结点赋值
    print("第"+str(i+1)+"个结点数据：" +str(data))
    
    p=head #每次产生的新数据都要从 头结点 开始比较大小
    if data<=n[head][0]: #新产生的 i结点data 比 头结点数据 还要小
        head=i      #更新头指针，i成为头结点
        n[i][1]=p   #新结点i 指向 原头结点
    else:
        q=n[p][1]   #p为头结点，q为头结点的下一个结点
        while n[q][0]<data and q!=-1:
            p=q     #迭代
            q=n[p][1]   #q为p的下一个结点
        n[p][1]=i   #i结点插入p，q之间，修改p结点的指针，指向i（位置）
        n[i][1]=q   #i结点的指针指向q
        
    print("逐步无序输出链表:");print(n)  
#根据data值有序输出链表
print("\n根据data值有序输出链表:")
p=head
while p!=-1:
    print(n[p][0])
    p=n[p][1]
   