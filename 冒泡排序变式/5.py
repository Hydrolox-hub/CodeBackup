def bubble(data):#最小元素上浮
    length=len(data)
    for i in range(1,length):
        for j in range(length-1,i,-1):
            if data[j]<data[j-2]:
                data[j],data[j-2]=data[j-2],data[j]


data=[3,4,1,6,2,9,7,0,8,5]

print("待排奇数位置：")
for i in range(0,len(data),2):
    print(data[i],end=" ")
print("\n待排偶数位置：")
for i in range(1,len(data),2):
    print(data[i],end=" ")
bubble(data)

print("\n奇数位置结果：")
for i in range(0,len(data),2):
    print(data[i],end=" ")
print("\n偶数位置结果：")
for i in range(1,len(data),2):
    print(data[i],end=" ")
