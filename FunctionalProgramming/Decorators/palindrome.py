from functools import lru_cache 
from runtest import run_tests

@lru_cache()
def is_palindrome(word):
    if word == "":
        return True
    elif word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])



submit_cases = [
    ( "aibohphobia", True, ),
    ( "eve", True, ),
    ( "level", True, ),
    ( "tat", True, ),
    ( "rotator", True, ),
    ( "potato", False, ),
    ( "", True, ),
    ( "a", True, ),
    ( "apple", False, ),
    ( "redivider", True, ),
    ( "divide", False, ),
    ( "kayak", True ),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: '{input}'")
    print(f"Expecting: {expected_output}")
    result = is_palindrome(input)
    print(f"   Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


run_tests(submit_cases, test)