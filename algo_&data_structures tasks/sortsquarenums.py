nums = [-5, -3, -2, -1]
nums = [i * i for i in nums]

print(nums)


def sortsquare(nums):
    for i in range(len(nums) - 1):
        if nums[i + 1] is not None:

            if nums[i] > nums[i + 1]:
                temp = nums[i + 1]
                nums[i + 1] = nums[i]
                nums[i] = temp
            else:
                continue
        if i > 0 and nums[i - 1] > nums[i]:
            sortsquare(nums)

    return print(nums)



sortsquare(nums)
