matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target =399
rows = len(matrix)
cols = len(matrix[0])
l = 0
r= rows*cols-1


while l<=r:
    mid = (l+r)//2
    i=mid//cols
    j=mid%cols
    if matrix[i][j]>target:
        r=mid-1
    elif matrix[i][j]<target:
        l= mid+1
    else:
        print(True)
        break



print(False)


