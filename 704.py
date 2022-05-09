nums = [-1,0,3,5,9,12]
l=0
r=len(nums)-1
target = 9
while l<=r:

    m=(l+r)//2
    if nums[m] > target:
        r=m-1
    elif nums[m] < target:
        l = m+1
    else:

        print(m)
print(-1)
