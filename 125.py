s = "race a car"

l,r=0,len(s)-1

result="true"

while l < r:
    while l<r and not s[l].isalpha():
        l+=1
    while r>l and not s[r].isalpha():
        r-=1
    if s[r].lower()!=s[l].lower():

        result = "false"
    l+=1
    r-=1
print(result)
