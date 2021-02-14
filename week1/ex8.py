#https://www.acmicpc.net/problem/4949

while True:
    sw = True
    line = input()
    if line == '.' :
        break
    stack =[]
    for i in line:
        if i =='(' :
            stack.append('(')
        elif i =='[':
            stack.append('[')
        elif i == ')':
            if len(stack) == 0 or stack.pop() != '(' :
                sw = False
                break
        elif i == "]":
            if len(stack) == 0 or stack.pop() != '[' :
                sw = False
                break
    if sw and len(stack) == 0:
        print("yes")
    else:
        print("no")

