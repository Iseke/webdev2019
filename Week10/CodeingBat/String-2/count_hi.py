def count_hi(str):
  cnt=0
  s = "hi"
  for i in range(len(str)):
    if str[i:i+2]==s:
      cnt+=1
  return cnt
string = "hiislamhi"
print(count_hi(string))