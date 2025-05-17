#sort the alphabets in ascending order:
a=['a','c','e','b','f']
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        if(ord(a[i])>ord(a[i+1])):    #if(a[i]>a[i+1]):
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if (f==False):
        break
print(a)


