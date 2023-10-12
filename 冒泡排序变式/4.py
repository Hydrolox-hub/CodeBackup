def bubble(data):#最大元素下沉
    length=len(data)
    for i in range(1,length):
        for j in range(0,length-i):
            if data[j][1]>data[j+1][1]:
                data[j],data[j+1]=data[j+1],data[j]
            elif data[j][1]==data[j+1][1] and data[j][0]>data[j+1][0]:
                data[j],data[j+1]=data[j+1],data[j]

data=[['A',4],['B',2],['C',3],['E',2],['D',2]]
print("待排序列：",data)
bubble(data)
print("排序结果：",data)
