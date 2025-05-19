#LINEAR SEARCH
#print the last index where the element is found
a=[2,4,3,1,4,2,3,4,5]
x=9
f=0
for i in range(len(a)):
    if a[i]==x:
        k=i
        f=1
if f==0:
    print("-1")
else:
    print(k)
    
    
#OR

a=[2,4,3,1,4,2,3,4,5]
x=9
f=0
for i in range(len(a)-1,-1,-1):
    if a[i]==x:
        k=i
        f=1
if f==0:
    print("-1")
else:
    print(k)
    