import pytest
from Code import makeBricks

#def test_make_bricks():
 #   assert makeBricks.make_bricks(1000000, 1000, 1000100) == True
  #  assert makeBricks.make_bricks(43, 1, 46) == True
   # assert makeBricks.make_bricks(3, 1, 9) == False 

def test_make_bricks3():
    assert makeBricks.make_bricks(1000000, 1000, 1000100) == True
    assert makeBricks.make_bricks(43, 1, 46) == True
    assert makeBricks.make_bricks(3, 1, 9) == False 