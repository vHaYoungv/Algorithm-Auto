def check(s):
    stk = []
    for x in s:
        if x=='(':
            stk.append(x)
        else:
            if stk and stk[-1]=='(':
                stk.pop()
            else:
                return False
    return not stk

n = int(input())
for i in range(n):
    if check(input()):
        print("YES")
    else:
        print("NO")

