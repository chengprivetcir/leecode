nums = [1,2,3,4]
result = [24,12,8,6]

# 1 1 2 6
# 24 12 4 1
res = []
prefix = 1

for i in range(len(nums)):
    res.append(prefix)
    prefix = prefix * nums[i]

postfix = 1
for j in reversed(range(len(nums))):
    res[j] = res[j]*postfix
    postfix = postfix * nums[j]


print(res)

