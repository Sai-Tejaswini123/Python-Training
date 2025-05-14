#PERFORMING XOR IN GIVEN RANGE:
#(QUESTION): input:5  to 10      output:5^6^7^8^9^10
n=int(input())
m=int(input())
def xor_total(a):
    if a%4==1:
        return 1
    elif a%4==2:
        return a+1
    elif a%4==3:
        return 0
    else:
        return a
print(xor_total(n-1)^xor_total(m))
    