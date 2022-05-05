s = "ABAB"
k = 2

dis = {}

res = 0

l = 0
max_letter=0

for r in range(len(s)):
    dis[s[r]]=1+dis.get(s[r],0)
    max_letter = max(dis[s[r]],max_letter)

    if r-l+1 - max_letter>k:
        dis[s[l]]-=1
        l+=1
    res = max(res,r-l+1)

print(res)

