def bubble(data):#最小元素上浮
    length=len(data)
    for i in range(1,length):
        for j in range(length-1,i-1,-1):
            if data[j]<data[j-1] and data[j]%2==data[j-1]%2:
                data[j],data[j-1]=data[j-1],data[j]
            elif data[j]%2==0 and data[j-1]%2==1:
                data[j],data[j-1]=data[j-1],data[j]



data=[3,4,1,6,2,9,7,0,8,5]
print("待排序列：",data)
bubble(data)
print("排序结果：",data)
