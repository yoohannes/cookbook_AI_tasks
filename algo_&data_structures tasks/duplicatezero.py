nums = [2, 3, 0, 2, 30, 0]
numsnew = []


def bruteforce(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            numsnew.append(nums[i])
            numsnew.append(0)
        else:
            numsnew.append(nums[i])
    return print(numsnew)


def optimized(nums):
    for i in range(len(nums)-1):
        if nums[i] == 0:

            for j in range(len(nums)-1, i+1, -1):

                nums[j] = nums[j - 1]
            nums[i+1]=0

        else:
            i = i + 2
    return print(nums)
#optimized(nums)
for i in range(len(nums)-1):
    if nums[i]==0:
        print("here here")
        next()
    print(nums[i])
