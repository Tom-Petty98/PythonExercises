# Decided not to do the first 2 easy chaalnges because they were a bit too easy.

import sys

def near(a, b):
    for i in range(len(a)):
        c = a[:i] + a[i + 1:]
        if c == b:
            return True
    
    return False

print(near("reset", "rest"))
print(near ("dragoon", "dragon"))
print(near ("eave", "leave"))
print(near ("sleet", "lets"))



def times_table():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    b = []

    for i in a:

        if len(b) == 12:
            print(b)
            b.clear()

        for j in a:
            c = i*j
            b.append(c)
    print(b)


times_table()

