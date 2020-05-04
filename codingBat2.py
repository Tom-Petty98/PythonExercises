#code completed on monday (04/05/20)

# completed string-1 and list-1 which turned out to be easier than the warmups I did on friday


# reverses list
def reverse3(nums):
  return nums[::-1]

#shuffles each item one index to the left
def rotate_left3(nums):
  
  list1 = []
  
  for i in range(len(nums)-1):
    list1.append(nums[i + 1])
    
  list1.append(nums[0])
  
  return list1

# searches list for specific value
def has23(nums):
  if nums.count(2) > 0 or nums.count(3) > 0:
    return True
  return False

#noupper limit on weekend party

def cigar_party(cigars, is_weekend):
  if (is_weekend):
    return cigars >= 40
  else:
    return cigars >= 40 and cigars <= 60