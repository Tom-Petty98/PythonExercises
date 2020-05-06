def print_factorial(num):
    factorial = 1

    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
            factorial = factorial*i
            print(factorial, end=', ')


#print_factorial(8)

def find_factorial(num):
    factorial = 1
    a = []

    if num < 0:
        return "Sorry, factorial does not exist for negative numbers"
    elif num == 0:
        return  1
    else:
       for i in range(1,num + 1):
            factorial = factorial*i
            a.append(factorial)
    return a

#print(find_factorial(2))