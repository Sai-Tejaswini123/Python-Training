#FINDING SECOND MAXIMUM ELEMENT:
a=list(map(int,input().split()))
m1=0
m2=0#second maximum
for i in a:
    if i>m1:
        m2=m1
        m1=i
    elif i!=m1 and i>m2:
        m2=i
print(m2)
    