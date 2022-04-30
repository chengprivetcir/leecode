nums = [-1, 0, 1, 2, -1, -4]

res= []
nums.sort()
for i,v in enumerate(nums):
    if i > 0 and nums[i]==nums[i-1]:
        continue
    l,r=i+1,len(nums)-1
    while l<r:
        if v+ nums[l]+nums[r]>0:
            r-=1
        elif v+nums[l] +nums[r]<0:
            l+=1
        else:
            res.append([v,nums[l],nums[r]])
            r-=1
            while nums[r]==nums[r+1] and l<r:
                r-=1
print(res)


#different from distinct number, distinct number move pointers both