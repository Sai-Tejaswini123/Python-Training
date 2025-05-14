#FINDING A NUMBER WITH FREQUENCY 1 USING sliding window :
a=list(map(int,input().split()))
for i in range(0,len(a)-1,2):
    if a[i]!=a[i+1]:
        print(a[i])
        break
else:
    print(a[-1])