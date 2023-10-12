def bubble1(data):#最小元素上浮
    length=len(data)
    for i in range(1,length):
        for j in range(length-1,i-1,-1):
            if data[j]<data[j-1]:
                data[j],data[j-1]=data[j-1],data[j]

def bubble2(data):#最大元素下沉
    length=len(data)
    for i in range(1,length):
        for j in range(0,length-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]

data=[3,4,1,6,2,9,7,0,8,5]
print("待排序列：",data)
bubble2(data)
print("排序结果：",data)
