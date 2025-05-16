#forest in fire
def fire_catch(m,i,j,n=None):
    if n==None:
        n=len(m)
    if i>=n or j>=n or i<0 or j<0 or m[i][j]==0 or m[i][j]==2 :
        return 0
    if m[i][j]==1:
        m[i][j]=2
        
    fire_catch(m,i-1,j,n)
    fire_catch(m,i+1,j,n)
    fire_catch(m,i,j+1,n)
    fire_catch(m,i,j-1,n)
m=[]
n=int(input())
for _ in range(n):
    m.append(list(map(int,input().split())))
c=0
fire_catch(m,2,5,n)
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            c+=1

        
print(c)

'''6
1 0 0 1 1 1
1 1 1 0 0 0
0 0 1 1 1 1
1 1 1 0 0 0
0 0 0 0 0 1
1 0 0 1 0 0
'''