#PRINT ALL SUBSETS:
def subset(x,s=[],i=0):
    if i==len(x):
        print(s)
        return
    subset(x,s+[x[i]],i+1)
    subset(x,s,i+1)
a=[2,3,4]
subset(a)



