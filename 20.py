s = "("

stack =[]
mapper = {"}":"{","]":"[",")":"("}



for l in s:
    if l not in mapper:
        stack.append(l)
    elif stack:
        if stack[-1]==mapper[l]:
            stack.pop()
        else:
            print(False)
    else:
        print(False)
print(not stack)


