# def sort(n):
#     for i in range(len(n)):
#         for j in range(len(n)-i-1):
#             if n[j]>n[j+1]:
#                 n[j],n[j+1]=n[j+1],n[j]
#     return n
# n=list(map(int,input().split()))
# print(sort(n))


#MOST EFFICIENT WAY FOR BUBBLE SORT:
# a=[3,5,1,2,4,7,9,3]
# c=0
# for j in range(len(a)-1):
#     f=False
#     for i in range(len(a)-1-j):
#         c=c+1
#         if(a[i]>a[i+1]):
#             f=True
#             a[i],a[i+1]=a[i+1],a[i]
#         if (f==False):
#             break
# print(a)
# print(c)
#             


#Kth largest element usin bubble sort:
# a=[3,5,1,2,4,7,9,3]
# c=0
# k=3
# for j in range(k):
#     f=False
#     for i in range(len(a)-1-j):
#         c=c+1
#         if(a[i]>a[j+1]):
#             f=True
#             a[i],a[i+1]=a[i+1],a[i]
#         if (f==False):
#             break
#      
#         
#         
# print(a[-k])
# print(c)
            

#SORT THE ELEMENTS BEFORE K AND AFTER K :
a=[2,5,8,6,3,1,9,4,7]
k=1
c=0
for i in range(k,len(a)-k-1):
    f=False
    for j in range(i+1,len(a)-k):
        c=c+1
        if a[j]<a[i]:
            f=True
            a[i],a[j]=a[j],a[i]
    if f==False:
        break
    print(a)
#print(c)

