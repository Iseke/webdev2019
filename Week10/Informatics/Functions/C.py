ls = [int(e) for e in input().split()]
def xor(x,y):
    if x==0 and y==0 or x==1 and y==1:
        return 0
    else:
        return 1
print(xor(ls[0],ls[1]))