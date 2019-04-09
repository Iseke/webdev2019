import math
v = int(input())
t = int(input())
div = (v*t)/109
if math.abs(v*t)==109 or t%109==0 or v==0 or t==0:
    print(0)
    