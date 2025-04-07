def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)

def sum_nums(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))