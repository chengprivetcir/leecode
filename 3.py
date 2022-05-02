s = "pwwkew"
l = 0
charSet = set()
res= 0
for r in range(len(s)):
    # remove all duplicates from current sliding
    while s[r] in charSet:

        charSet.remove(s[l])
        l+=1
        print(l, charSet)
    charSet.add(s[r])
    res = max(res,r-l+1)
print(res)

