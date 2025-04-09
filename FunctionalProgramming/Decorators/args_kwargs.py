def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)

#===========================================

def sub(a, b):
    return a - b

res = sub(b=3, a=2) # res = -1
res = sub(a=3, b=2) # res = 1

#sub(b=3, 2) error

def args_logger(*args, **kwargs):
    arg_count = 1
    for arg in args:
        print(f"{arg_count}. {arg}")
        arg_count += 1

    sorted_kwargs = dict(sorted(kwargs.items()))
    for kwargs in sorted_kwargs:
        print(f"* {kwargs}: {sorted_kwargs[kwargs]}")

def test(*args, **kwargs):
    args_logger(*args, **kwargs)
    print("========================================")


def main():
    test("Good", "riddance", date_str="01/01/2023")
    test(message="Hello World", to_delete="l")
    test("two", "star-crossed", "lovers")
    test("hi", True, f_name="Lane", l_name="Wagner", age=28)


main()