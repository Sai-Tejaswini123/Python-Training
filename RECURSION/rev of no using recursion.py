#REVERSE OF A NUMBER USING RECURSION
def reverse(r,n):
    if n==0:
        return r
    return  reverse(r*10+n%10,n//10)
n=int(input())
print(reverse(0,n))
