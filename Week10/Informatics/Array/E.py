n = int(input())
ls = [int(e) for e in input().split()]
cnt = 0
for i in range(1,n):
    if ls[i-1]>0 and ls[i]>0 or ls[i-1]<0 and ls[i]<0:
        cnt+=1
if cnt>0:
    print("YES")
else:print("NO")