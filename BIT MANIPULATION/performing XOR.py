#PERFORMING XOR:
#(QUESTION)INPUT:5-----------OUTPUT: 1^2^3^4^5
#time complexity=O(n)
a=int(input("enter a number"))
s=0
for i in range(1,a+1):
    s=s^i
print(s)

#OR(time complexity=O(1)
if a%4==1:
    print(1)
elif a%4==2:
    print(a+1)
elif a%4==3:
    print(0)
else:
    print(n)