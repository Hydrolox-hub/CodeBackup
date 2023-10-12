#a=[66,66,55,44,33,33,22,22,11]
b=[11,22,22,33,33,44,55,66,66]
key=33

L=0;R=8
while L<R:
    m=(L+R)//2
    if b[m]<=key:
        L=m+1
    else:
        R=m
print(R)
print(L)
