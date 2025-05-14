#COUNT OF PRIME NUMBERS IN LIST 
def is_prime(i,x):
    if i>x//2:
        return True
    if x%i==0:
        return False
    return is_prime(i+1,x)
def prime_count(x, i,c):
    if i==len(x):
        return c
    if is_prime(2,x[i]):
        return prime_count(x,i+1,c+1)
    return prime_count(x,i+1,c)
a = [13,17,21,23,22,7,29]
print(prime_count(a,0,0))
