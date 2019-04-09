ls = [float(e) for e in input().split()]
def power(p,n):
    res = 1
    for i in range(0, n):
        res*=p
    return res
print(power(ls[0],int(ls[1])))
