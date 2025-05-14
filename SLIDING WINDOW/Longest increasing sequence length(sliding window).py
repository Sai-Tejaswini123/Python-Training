#Longest increasing sequence length:
li=[2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9]
# li=[1,2,3,2,3,4,5,6,7,8,9]
count = 1
max_count = 1
for i in range(len(li) - 1):
    if li[i+1] - li[i] == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1  
print("Longest increasing sequence length:", max_count)
