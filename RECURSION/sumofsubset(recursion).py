#PRINT TRUE IF THE SUM OF SUBSET IS FORMED WITH THE ELEMENTS IN SUBSETS:
# def subset(a,k,x=[],i=0):
#     if i==len(a):
#         if sum(x)==k:
#             print('True')
#         return
#     subset(a,k,x+[a[i]],i+1)
#     subset(a,k,x,i+1)
# 
# a=[2,3,4]
# k=5
# subset(a,k)

#OR(BEST):
def subset(a,k,i):
    if(k==0):
        return True
    if i==0:
        return False
    
    if a[i-1]>k:
        return subset(a,k,i-1)
    return subset(a,k-a[i-1],i-1) or subset(x,k,i-1)
a=[2,3,4]
k=7
print(subset(a,k,len(a)))