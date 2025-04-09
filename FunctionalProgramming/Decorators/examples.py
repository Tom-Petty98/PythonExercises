from functools import lru_cache

# lru_cache memoizes the inputs and outputs of the decorated function in a size-restricted
# dictionary. It speeds up repeated calls to a slow function with the same inputs. 
# For instance, if the function reads from disc, makes network requests, or requires a 
# lot of computation AND it is used repeatedly with the same inputs.

@lru_cache()
def factorial_r(x):
    if x == 0:
        return 1
    else:
        return x * factorial_r(x - 1)

factorial_r(10) # no previously cached result, makes 11 recursive calls
# 3628800
factorial_r(5)  # just looks up cached value result
# 120
factorial_r(12) # makes two new recursive calls, the other 11 are cached
# 479001600