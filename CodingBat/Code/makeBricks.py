def make_bricks(small, big, goal):
  
  for i in range(big + 1):
    
    if i * 5 == goal:
      return True
    
    for j in range(small + 1):
      if (i * 5) + j == goal:
        return True
    
  return False

#print(make_bricks(1000000, 1000, 1000100))
#print(make_bricks(43, 1, 46))


#-------------------------------
# without loops

def make_bricks2(small, big, goal):
  minSmallReq = goal % 5 
  diff = big * 5 - goal
  
  if diff >= 0 and (small >= minSmallReq):
    return True
  elif diff < 0 and (-diff <= small):
    return True
  else:
    return False

#--------------------------------
# The most efficient Method

def make_bricks3(small, big, goal):
  minSmallReq = goal % 5 
  max = small + (big * 5)
  
  if max < goal:
    return False
  elif small < minSmallReq:
    return False
  else:
    return True