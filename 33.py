# nums = [4,5,6,7,0,1,2]

nums = [7,8,9,0,1,2,3,4,5,6]



l = 0

r= len(nums) -1

res=nums[l]

while l<=r:
    m = (l+r)//2

    if nums[m]>= nums[l]:
        res = min(nums[l],res)
        l =m+1
    else:
        res = min(nums[m],res)
        r=m-1

print(res)







