n = int(input())
ls = [int(e) for e in input().split()]
cnt = 0
for i in range(1, n-1):
    if ls[i] > ls[i-1] and ls[i] > ls[i+1]:
        cnt+=1
print(cnt)