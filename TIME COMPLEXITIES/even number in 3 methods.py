#EVEN OR ODD NUMBER:
a=int(input("enter a number"))
if a%2==0:
    print("the number is even")
else:
    print("the number is odd")
    
#method-2:
if a&1!=1:
    print("the number is even")
else:
    print("the number is odd")
    
#method-3:
if a^1==a+1:
    print("even")
else:
    print("odd")
