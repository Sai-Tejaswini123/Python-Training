#sort the strings in a list in lexographical order compare only two charcters.if first 2 characters are same dont sort
def sort(a):
    for i in range(len(a)-1):
        flag=False
        for j in range(len(a)-i-1):
            if a[j][:2]>a[j+1][:2]:
               
                a[j],a[j+1]=a[j+1],a[j]
                flag=True
        if flag==False:
            break
    return a
            

a=['zebra','cat','apple','car']
print(sort(a))




#OR
#without slicing
def sort(a):
    for i in range(len(a) - 1):
        flag = False
        for j in range(len(a) - i - 1):
            if a[j][0] > a[j + 1][0]:
                
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True
            elif a[j][0] == a[j + 1][0] and a[j][1] > a[j + 1][1]:
                flag = True
                a[j], a[j + 1] = a[j + 1], a[j]
        if not flag:
            break
    return a

a = ['zebra', 'cat', 'apple', 'car']
print(sort(a))
