print(2)
for i in range(3,100):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i)
            
    

      
