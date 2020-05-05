def lone_sum(a, b, c):
  
  if a == b and a == c:
    return 0
  elif a == b:
    return c
  elif a == c:
    return b
  elif b == c:
    return a
  else:
    return a + b + c

#is the same as

def lone_sum2(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum

#-----------------------------

def lucky_sum(a, b, c):
  nums = [a, b, c]
  
  sum = 0
  
  for i in nums:
    
    if i == 13:
      return sum
    
    sum += i
  
  return sum

#----------------------------------

def fix_teen(n):
  if n == 15 or n == 16:
    return n
  elif n >= 13 and n <= 19:
    return 0
  else:
    return n
    

def no_teen_sum(a, b, c):
  a = fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)
  
  return a + b + c

#-------------------------------------

def round10(n):
  
  r = n % 10
  if (r >= 5 ):
    return n + (10 - r)
  else:
    return n - r 

#---------------------------------------

def round10(num):
  mod = num % 10
  num -= mod
  if mod >= 5: num += 10
  return num
