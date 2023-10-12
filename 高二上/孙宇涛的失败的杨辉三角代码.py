import queue
n=int(input('输入行数：'))
q=queue.Queue(n**2)
q.put(1)
print(q.get(),end='\n')
q.put(1);q.put(1)
for i in range(3,n+1):
    
    for j in range(2,i):
        a=q.get()
        print(a,end=' ')
        b=q.get()
        print(b,end=' ')
        q.put(a+b)
        b=a
    q.put(1)
    print(' ',end='\n')
c=q.size()
for i in c:
    print(q.get())
