# We want to make a row of bricks that is goal inches long. We have a number of 
# small bricks (1 inch each) and big bricks (5 inches each). Return True if it is 
# possible to make the goal by choosing from the given bricks.

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

# ---------------------------------
# The same as before but returning the num of small bars used 

def make_chocolate(small, big, goal):
    minSmallReq = goal % 5
    total = small + (big * 5)
    diff = goal - big * 5
   
    if minSmallReq > small or total < goal:
      return -1
    elif big * 5 > goal:
      return minSmallReq
    else:
      return diff