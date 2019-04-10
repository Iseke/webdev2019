def string_bits(str):
  res=""
  for x in range(len(str)):
    if x%2==0:
      res+=str[x]
  return res
