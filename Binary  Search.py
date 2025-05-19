#BINARY SEARCH
#print the last index where the element is found
a=[2,3,5,6,7,7,8,9,10,10,10,13,15]
l=0
key=10
h=len(a)-1
res=-1
while l<=h:
    mid=(l+h)//2
    if a[mid]==key:
        res=mid
        l=mid+1#(tp print the last occurance index)
        #h=mid-1#to print the first occurance index
    elif key<a[mid]:
        h=mid-1
    else:
        l=mid+1
if res!=-1:
    print(res)
else:
    print("-1")

