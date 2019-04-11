def lone_sum(a, b, c):
  if a==b and b!=c:
    return c
  if b==c and c!=a:
    return a
  if a==c and c!=b:
    return b
  if a==b and b==c:
    return 0
  elif a!=b and b!= c:return a+b+c
