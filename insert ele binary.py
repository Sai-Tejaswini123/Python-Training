a=[2,4,6,7,8,10,13,15]
key=9
l=0
h=len(a)-1
r=-1
while l<=h:
    mid=(l+h)//2
    if a[mid]==key:
        r=mid
        break
    elif key<a[mid]:
        h=mid-1
    elif key>a[mid]:
        l=mid+1
if r!=-1:
    print(r)
else:
    print(l)