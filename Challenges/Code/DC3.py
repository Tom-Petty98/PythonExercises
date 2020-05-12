# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.

#   (without,hello,bag,world) -> bag,hello,without,world

def sort_words(s1):
    a = s1.split(',')

    a.sort()
    s2 = ""

    for i in range(len(a)):
        if i == len(a) -1:
            s2 += a[i]
        else:
            s2 += a[i] + ","
    
    return s2


print(sort_words("without,hello,bag,world"))

 

