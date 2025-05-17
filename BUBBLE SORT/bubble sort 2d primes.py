#sort according to the primes numbers:
#input:[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
#output:[[14,8,3],[8,10,5],[7,9,20],[4,13,12]]
'''def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def sublist(a):
    for n in a:
        if prime(n):
            return n
def sort(a):
    for j in range(len(a)-1):
        f=False
        for i in range(len(a)-1-j):
            if sublist(a[i])>sublist(a[i+1]):
                
                a[i],a[i+1]=a[i+1],a[i]
                f=True
        if (f==False):
            break
    return a

a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
print(sort(a))'''


#(medthod-2):

def prime(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            return i
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
b=[]
for i in a:
    b.append(prime(i))
for i in range(len(b)-1):
    f=0
    for j in range(len(b)-1-i):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
            f=1
    if(f==0):
        break
print(a)
            
            
        