#FIND MAX EVEN AND MIN ODD NUMBER(GREEDY ALGORITHM):
a=list(map(int,input().split()))
m=0
m1=999999
for i in a:
    if(i>m and i%2==0):
        m=i
    if (i<m1 and i%2!=0):
        m1=i
print(m,m1)

