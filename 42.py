height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

l,r = 0, len(height)-1
res = 0
lmax, rmax = height[0],height[len(height)-1]
while l < r:
    if lmax < rmax:
        l+=1

        if (lmax - height[l])>0:
            res+=lmax - height[l]
        lmax = max(lmax, height[l])
    else:
        r-=1

        if(rmax- height[r])>0:
            res+=rmax- height[r]
        rmax = max(rmax, height[r])
print(res)

