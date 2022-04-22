from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

res = defaultdict(list)

for word in strs:
    count = [0]*26
    for letter in word:
        count[ord(letter)-ord("a")]+=1
    res[tuple(count)].append(word)

print(res.values())

