#maximum profit 
#a=[2,4,1,5,8,1,4]
a=[13,14,2,5,8,1,4]
profit=0
buy=a[0]
for i in range(1,len(a)):
    if a[i]>buy:
        profit=max(profit,a[i]-buy)
    else:
        buy=a[i]
print(profit)

#maximum profit(greedy):O(n)
a=[13,14,2,5,8,1,4]
profit=0
buy=a[0]
for i in range(1,len(a)):
    if a[i]>buy:
        if a[i]-buy>profit:
            profit=a[i]-buy
    else:
        buy=a[i]
print(profit)
# method-3:Two pointer approach:O(n*n)
a=[13,14,2,5,8,1,4]
mp=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>mp:
            mp=a[j]-a[i]
print(mp)