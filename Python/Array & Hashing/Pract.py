nums = [4,1,-1,2,-1,2,3]
k = 2
counter = {}
result = []

for num in nums:
    counter[num] = 1 + counter.get(num,0)

sortedList = sorted(counter.items(), key=lambda x:x[1], reverse=True)

for i in range(k):
    result.append(sortedList[i][0])

print(result)