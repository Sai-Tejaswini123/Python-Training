#backtracking
def rat(a,i,j,n):
    if(a[i][j]==0 or i>=n or j>=n):
        return 0
    if (i==n-1 or j==n-1 and a[i][j]==1 ):
        return 1
    return rat(a,i,j+1,n)+rat(a,i+1,j,n)

n=int(input())
m=[]
for i in range(n):
    m.append(list(map(int,input().split())))
print(rat(m,0,0,n))
