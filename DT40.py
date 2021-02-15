a=(100,200,666)
T1=[10,50,20,9,40,25,60,30,1,56]
L1=list(a)
for x in T1:
    L1.append(x)
T1=tuple(L1)
print(T1)