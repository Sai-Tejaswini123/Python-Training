#FINDING THE NO ON STEPS TO REACH THE DESTINATION WITH HURDLES GIVEN
def frog(n,i,j,hurd):
    if(i==n or j==n or (i,j) in hurd):
        return 0
    if(i==n-1 and j==n-1):
        return 1
    return frog(n,i+1,j,hurd)+frog(n,i,j+1,hurd)
n=5
i=2
j=3
hurd=[(2,1),(4,1),(5,2),(3,5)]
print(frog(n,i-1,j-1,hurd))