numbers = [2,3,4]
target = 6

l,r=0,len(numbers)-1

while l<r:
    if numbers[l] + numbers[r] == target:
        print( [l+1,r+1])
        break
    elif numbers[l]+numbers[r]>target:
        r-=1
    else:
        l+=1