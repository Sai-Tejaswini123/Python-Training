#(SAY WHETHER A NUMBER IS POWER OF 2 OR  NOT)
#TIME COMPLEXITY=O(1)
n=int(input())
if n&(n-1)==0:
    print("yes")
else:
    print("no")
    
#OR-----(O(logn))
while n%2==0:
    n=n//2
if n==1:
    print("yes")
else:
    print("No")