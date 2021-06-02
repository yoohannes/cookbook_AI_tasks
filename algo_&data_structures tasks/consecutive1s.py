array = [1, 1, 0, 1, 1, 1,0]
answer = []
count = 0
for i in array:
    if i == 1:
        count += 1
    else:
        answer.append(count)
        count = 0
        continue
answer.append(count)    #if the last binary digit is 1
print(max(answer))
