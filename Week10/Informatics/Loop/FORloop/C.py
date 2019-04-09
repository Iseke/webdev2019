import math
a = int(input())
b = int(input())
for x in range(a,b+1):
    if math.ceil(math.sqrt(x))- math.sqrt(x)== 0:
        print(x,end=' ')

