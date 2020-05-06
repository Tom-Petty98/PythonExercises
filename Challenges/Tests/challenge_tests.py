import pytest
from Code import DailyChallenge2

def test_find_factorial():
    assert DailyChallenge2.find_factorial(0) == 1
    assert DailyChallenge2.find_factorial(2) == [1, 2]
    assert DailyChallenge2.find_factorial(3) == [1, 2, 6]
    assert DailyChallenge2.find_factorial(5) == [1, 2, 6, 24, 120]
    assert DailyChallenge2.find_factorial(7) == [1, 2, 6, 24, 120, 720, 5040]
    assert DailyChallenge2.find_factorial(8) == [1, 2, 6, 24, 120, 720, 5040, 40320]
    

    
    