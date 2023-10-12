data=[12,5,8,6,7,9,64,52]
def insert(data):
    b=[0]*len(data)
    for i in range(0,len(data)):
        temp=data[i]
        j=i-1
        while j>-1 and b[j]>temp:
            b[j+1]=b[j]
            j-=1
        b[j+1]=temp

    print(b)

insert(data)
    
