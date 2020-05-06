# duplicate each char in string 'The' -> 'TThhee'

def double_char(str):
  a = ''
  
  for i in str:
    a += i + i
  
  return a

#-----------------------------------------------------
# Returns True if cat and dog are mentioned in equal amounts

def cat_dog(str):
  return str.count('cat') == str.count('dog')

#------------------------------------------------------

import re

def count_code(str):
  reg = re.compile("co.e")
  count = 0
  
  for i in range(len(str) - 3):
    if i == 'c' and str[i:i+4] == reg:
      count += 1
      
  return count


def count_code2(str):
  count = 0
  s = str.lower()
  
  for i in range(len(str) - 3):
    if s[i] == 'c':
      a = s[i:i+2] + s[i + 3]
      if a == 'coe':
        count += 1
  
  return count

#--------------------------------------------------------

def end_other(a, b):
  if len(a) < len(b):
    return a.lower() == b[-len(a):].lower()
  
  return b.lower() == a[-len(b):].lower()


def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))

#------------------------------------------------------------
# Return True if the given string contains an appearance of "xyz" where the xyz 
# is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

# xyz_there('abc.xyzxyz') → True


def xyz_there(str):
  
  c = str.count('xyz')
  n = str.count('.xyz')
  
  return c - n >= 1



