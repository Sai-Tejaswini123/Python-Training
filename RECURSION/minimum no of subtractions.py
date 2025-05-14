def see(n,p,q,c=0):
    if n==1:
        return 0
    if n<1:
        return False
    else:
        return 1+min(see(n-p,p,q,c+1) , see(n-q,p,q,c+1))  
n=20
p=3
q=5
print(see(n,p,q))
