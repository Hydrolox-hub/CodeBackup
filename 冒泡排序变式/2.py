def bubble(data1,data2):#最大元素下沉
    length=len(data2)
    for i in range(1,length):
        for j in range(0,length-i):
            if data2[j]>data2[j+1]:
                data1[j],data1[j+1]=data1[j+1],data1[j]
                data2[j],data2[j+1]=data2[j+1],data2[j]

data1=['A','B','C','E','D']
data2=[4,2,3,5,1]
print("待排序列：")
for i in range(len(data2)):
    print(data1[i],data2[i])

bubble(data1,data2)
print("排序结果：")
for i in range(len(data2)):
    print(data1[i],data2[i])

