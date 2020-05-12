# Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number. The numbers obtained should be 
# printed in a comma-separated sequence on a single line.

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

def even_digits():

    for i in range(2000, 2900):
        d_even = True

        for digit in str(i):
            
            if int(digit) % 2 != 0:
                d_even = False
    
        if d_even:
            print(i, end=', ')

even_digits()


