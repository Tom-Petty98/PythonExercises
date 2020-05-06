#removes highest and lowest and returns the avaerage

def centered_average(nums):
  a = sorted(nums)
  del(a[0])
  del(a[-1])
  
  return sum(a) / len(a)

#------------------------------------------------------
# if num is 13 exclude it and the number following it

def sum13(nums):
  sum = 0
  
  for i in range(len(nums)):
    
    if i == 0 and nums[i] != 13:
      sum += nums[i]
    elif nums[i] != 13 and nums[i-1] != 13:
      sum += nums[i]

      
  return sum

  #---------------------------------------------------------
# Return the sum of the numbers in the array, except ignore sections of 
# numbers starting with a 6 and extending to the next 7 
# (every 6 will be followed by at least one 7). 

def sum67(nums):
  sum = 0
  n = True
  
  for i in range(len(nums)):
  
    if nums[i] == 6:
      n = False
    elif n:
      sum += nums[i]
    elif nums[i] == 7:
      n = True
  
  return sum

  #-------------------------------------
  # has consecutive 2's

  def has22(nums):
  
  for i in range(len(nums) -1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  
  return False