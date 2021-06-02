S = str(input())
length = len(S)
for i in range(length-1):
    current = S[i]
    next = S[i+1]
    if current == next:
        if current.isalnum():
            print(current)
            break
        else:
            continue
else:
    print("-1")
