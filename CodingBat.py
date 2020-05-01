# I saved the answers from code bat that where interesting or differed from their soloutions



def missing_char(str, n):
  char = str[n]
  return str.replace(char, '')

# Is the same as

def missing_char2(str, n):
  front = str[:n]  
  back = str[n+1:]  
  return front + back

#-----------------------------------------------------

def front_back(str):
  f = str[:1]
  m = str[1:-1]
  e = str[-1:]
  
  if len(str) < 2:
    return str
  elif len(str) == 2:
    return e + f
  else:
    return e + m + f

# Is the same as

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:-1]  # if the string is 2 letter this wont return any values so theres no point checking
  
  # last + mid + first
  return str[-1] + mid + str[0]

def string_times(str, n):
  return str * n

#-------------------------

#The power of slicing

def string_bits(str):
  return str[::2]

# Is the same as

def string_bits2(str):
  result = ""

  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

#---------------------------------
# checks to see how many times a substring occurs in a string

def last2(str):
  last2 = str[-2:]
  count = 0
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count += 1
  return count


#--------------------------------
# Checks if 9 is one of the first 4 values in array

def array_front9(nums):
  
  for i in nums[:4]:
    if i == 9:
      return True
  return False

#--------------------------------
# check for seq

def array123(nums):
  seq = [1, 2, 3]

  for i in range(len(nums)-2):
    sub = nums[i:i+3]
    
    if (sub == seq):
      return True
  return False
  