nums=[-4,-1,0,3,10]
nums = [i * i for i in nums
for i in range(len(nums) - 1):

    for j in range(len(nums) - i - 1):
        if (nums[i + 1] != None):

            if nums[i] > nums[j + 1]:
                temp=nums[j+1]
                nums[j + 1] = nums[i]
                nums[i] = temp

            else:
                continue
print(nums)