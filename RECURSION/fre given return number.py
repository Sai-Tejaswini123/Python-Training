#PRINTING THE NUMBER BASED ON GIVEN FREQUENCY:
# from collections import Counter
# def count(ct,k,keys,l,i=0):
#     if i==len(keys):
#         return l
#     if ct[keys[i]]==k:
#         l.append(keys[i])
#     return count(ct,k,keys,l,i+1,)
#         
# a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
# k=1
# ct=Counter(a)
# keys=list(ct.keys())
# print(count(ct,k,keys,l=[]))


#OR(USING DICTIONARY):
def value(x,f,d,i=0):
    if i==len(x):
        return "not found"
    if d[x[i]]==f:
        return x[i]
    return value(x,f,d,i+1)
def fre(x,f,d={},i=0):
    if i==len(x):
        return value(list(d.keys()),f,d)
    if x[i] not in d:
        d[x[i]]=1
    else:
        d[x[i]]+=1
    return fre(x,f,d,i+1)
a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
f=4
print(fre(a,f))



# def iterate(x,f,i=0):
#     if i==len(x):
#         return "no number found"
#     if freq(x,x[i])==f:
#         return x[i]
#     return iterate(x,f,i+1)
# a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
# k=1
# print(iterate(x,f))

        
        