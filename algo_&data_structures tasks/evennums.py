nums = [12, 345, 2, 6, 7896]
print(([(10 > i / 10 > 1) for i in nums]))
cou = 0
for i in nums:
    if len(str(i)) % 2 == 0:
        cou += 1
print(cou)
