num = int(input())
while num > 1:
    if num%2!=0:
        print("NO")
        break
    num/=2

else:
    print("YES")