nums = [1,2,3,1]

dic = {}

for number in nums:
    if number in dic:
        print(True)
    dic[number] = 1
print(False)