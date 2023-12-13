def check(s):
    stk = []
    for x in s:
        if x=='(':
            stk.append(x)
        else:
            if stk and stk[-1]=='(':
                stk.pop()
            else:
                print("NO")
                return
    if stk:
        print("NO")
    else:
        print("YES")

n = int(input())
for i in range(n):
    check(input())


