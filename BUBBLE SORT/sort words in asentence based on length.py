#SORT THE SENTENCES ACCORDING TO THE LENGTH OF THE WORDS IN A SENTENCE:
def count(x):
    c=0
    for _ in range(len(x)):
        c+=1
    return c
def sorting(a,b):
    for i in range(len(b)-1):
        f=0
        for j in range(len(b)-i-1):
            if (b[j]>b[j+1]):
                b[j],b[j+1]=b[j+1],b[j]
                a[j],a[j+1]=a[j+1],a[j]
                f=1
        if(f==0):
            break
    return a
s="An apple a day keeps doctor away"
x=s.split()
b=[]
for i in x:
    b.append(count(i))
q=sorting(x,b)
p=' '.join(q)
print(p)


        
        
    
        
    