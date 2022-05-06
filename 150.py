tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

stack = []
for s in tokens:
    if s=="+":
        stack.append(stack.pop()+stack.pop())
    elif s=="-":
        a= stack.pop()
        b= stack.pop()
        stack.append(b-a)
    elif s == "*":
        stack.append(stack.pop() * stack.pop())
    elif s == "/":
        a = stack.pop()
        b = stack.pop()
        stack.append(int(b / a))
    else:
        stack.append(int(s))

print(stack.pop())
