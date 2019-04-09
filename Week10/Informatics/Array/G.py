n = int(input())
ls = [int(e) for e in input().split()]
cnt =0
for i in range(0, int(n/2)):
    tem = ls[i]
    ls[i] = ls[n-i-1]
    ls[n - i - 1] = tem
for i in range(0,n):
    print(ls[i])