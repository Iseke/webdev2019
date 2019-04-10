a = int(input())
arr = [int(e) for e in input().split()]

max1 = max(arr[0], arr[1])
max2 = -999999

for x in range(0, len(arr)):
    if arr[x] > max1:
        max2 = max1
        max1 = arr[x]
    elif arr[x] > max2 and arr[x] != max1:
        max2 = arr[x]

print(max2)