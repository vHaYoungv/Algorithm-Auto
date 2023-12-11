ipt = input()

for i in range(26):
    try:
        print(ipt.index(chr(ord('a') + i)), end=' ')
    except:
        print(-1, end=' ')
