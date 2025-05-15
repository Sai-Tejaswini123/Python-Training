#PRINT THE MINIMUM NO OF COINS TO GET THE GIVEN NUMBER IF NOT RETURN -1:
def sum_subset(a,k,x=0,i=0,res=[]):
    if i==len(a):
        if k==0:
            res.append(x)
        return 
    if a[i]<=k:
        sum_subset(a,k-a[i],x+1,i+1,res)
    sum_subset(a,k,x,i+1,res)

a=[2,4,6,8]
k=14
res=[]
sum_subset(a,k,res=res)
print("All counts:", res)
print("Minimum:", min(res) if res else "-1")

#OR
def sum_subset(a,k,x=0,i=0,m=999999):
    if i==len(a):
        if k==0:
            if x<m:
                m=x
        return m
    
    if a[i]<=k:
        m=sum_subset(a,k-a[i],x+1,i+1,m)
    m=sum_subset(a,k,x,i+1,m)
    return m
    
a=[2,4,6,8]
k=14
b=sum_subset(a,k)
if b==999999:
    print(-1)
else:
    print(b)


