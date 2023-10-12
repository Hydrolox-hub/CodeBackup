def bubble(data,length):#最小元素上浮
    for i in range(1,length):
        for j in range(length-1,i-1,-1):
            if data[j]<data[j-1]:
                data[j],data[j-1]=data[j-1],data[j]
            elif data[j]==data[j-1]:
                data[j]=data[length-1]
                length=length-1
    print(data[:length])

data=[2,9,0,2,5,5,2,7]
length=len(data)

#print("排序结果：")
#bubble(data,length)

a=[]
for i in range(1,length):
    for j in range(length-1,i-1,-1):
        if data[j]<data[j-1]:
            data[j],data[j-1]=data[j-1],data[j]
            a.append(data[j])
        elif data[j]==data[j-1]:
            continue
print(a)