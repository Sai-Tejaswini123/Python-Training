#back tracking and recursion
def land(a,i,j,n):
    if(i==n or j==n or i<0 or j<0 or a[i][j]==0  or a[i][j]==2):
        return 0
    if (a[i][j]==1):
        a[i][j]=2
    land(a,i-1,j,n)
    land(a,i,j-1,n)
    land(a,i+1,j,n)
    land(a,i,j+1,n)
a=[[1,0,0,1,1],[1,0,0,0,1],[0,0,0,1,0],[1,0,0,0,0],[1,0,0,0,1]]

for i in a:
    print(i)
c=0
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            land(a,i,j,5)
    c=c+1
print(c)

