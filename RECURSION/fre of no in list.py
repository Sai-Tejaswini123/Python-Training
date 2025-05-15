#PRINT THE FREQUENCY OF K VALUE IN THE GIVEN LIST:
#FUNCTIONAL RECURSION
def fre(x,k,i=0):
    if i==len(x):
        return 0
    elif x[i]==k:
        return 1+fre(x,k,i+1)
    else:
        return fre(x,k,i+1)
x=[2,4,6,3,3,3,2,6,1,2,3,6,6,5]
k=6
print(fre(x,k))


#OR
#PARAMETRISED RECURSION:
def fre(x,k,i,c=0):
    if i==len(x):
        return c
    elif x[i]==k:
        return fre(x,k,i+1,c+1)
    else:
        return fre(x,k,i+1,c)
x=[2,4,6,3,3,3,2,6,1,2,3,6,6,5]
k=6
print(fre(x,k,0))









