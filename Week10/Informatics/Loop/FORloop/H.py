num = int(input())
count = 0
for x in range(1,num+1):
    if num % x == 0:
        #print(x)
        count+=1

print(count)