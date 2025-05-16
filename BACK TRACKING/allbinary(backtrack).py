#PRINT THE BINARY NUMBERS WHEN A NUMBER IS GIVEN BEFORE THAT NUMBERS NEED TO BE PRINTED
import math
re=[]
def allbinary(a,n,s=''):
    if len(s)==n:
        re.append(s)
        return
    allbinary(a,n,s+'0')
    allbinary(a,n,s+'1')
a=5
n=int(math.log(a,2))+1
allbinary(a,n)
for  i in range(a+1):
    print(re[i])
    
 
#OR 

import math
def allbinary(a,n,s=''):
    if a==-1:
        return a
    if len(s)==n:
        print(s)
        a=a-1
        return a
    a=allbinary(a,n,s+'0')
    a=allbinary(a,n,s+'1')
    return a
a=5
n=int(math.log(a,2))+1
allbinary(a,n)
