n = int(input())
ls = input().split()
cnt = 0
for i in range(1, n):
    if int(ls[i]) > int(ls[i-1]):
        cnt += 1
print(cnt)