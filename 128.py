nums = [100,4,200,1,3,2,1]

numSet = set(nums)

print(nums)
longest = 0
for n in numSet:
     # check if start of a sequence
     if (n-1) not in nums:
         next_sequence = 0
         while (n+next_sequence) in nums:
             next_sequence+=1

         longest = max(longest,next_sequence)
print(longest)
