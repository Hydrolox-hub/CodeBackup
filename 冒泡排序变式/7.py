def bubble(data):#最大元素下沉
    length=len(data)
    for i in range(1,length):
        for j in range(0,length-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]

data=[[3,4,1,6,2],[9,7,0,8,5],[7,2,5,1,8]]

print("待排序列：",data)
for i in range(len(data)):
    bubble(data[i])
print("排序结果：",data)
