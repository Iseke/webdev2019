count =0
amount = int(input())
for x in range(1, amount+1):
    num = int(input())
    if num==0:
        count += 1

print(count)