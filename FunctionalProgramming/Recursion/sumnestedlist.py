from runtest import run_tests

def sum_nested_list(lst):
    sum = 0
    
    for item in lst:      
        if isinstance(item, int):
            sum += item
        else:
            sum += sum_nested_list(item)

    return sum


run_cases = [
    ([1, 2, [3, 4]], 10),
    ([5, [6, 7], [[8, 9], 10]], 45),
]

submit_cases = run_cases + [
    ([], 0),
    ([1, [2], [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]], 55),
]


def test(input_list, expected_output):
    print("---------------------------------")
    print(f"Input list: {input_list}")
    print(f"Expected output: {expected_output}")
    result = sum_nested_list(input_list)
    print(f"Actual output: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


run_tests(submit_cases, test)