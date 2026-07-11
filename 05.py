import math
n=math.factorial(5)
print(n)
#递归
n=5
def jiecheng(num):
  if num==1:
    return 1
  else:
    return num*jiecheng(num-1)
print(jiecheng(n))
