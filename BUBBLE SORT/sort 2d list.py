#sort according to the second element in the matrix
a=[[2,3],[5,1],[1,4],[2,7],[1,3]]
for j in range(len(a)-1):
    f=True
    for i in range(len(a)-1-j):
        if((a[i][1])>(a[i+1][1])):
            f=False
            a[i],a[i+1]=a[i+1],a[i]
    if (f==True):
        break
print(a)

