import math
num = int(input())
i = int(1)
while i <= num:
    if math.ceil(math.sqrt(i)) - math.sqrt(i) == 0:
        print(i, end=' ')
    i += 1
