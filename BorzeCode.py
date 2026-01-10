code = input()
ans = []
idx = 0
while idx < len(code):
    if code[idx] == ".":
        idx = idx + 1
        ans.append("0")
    else:
        if code[idx+1] == ".":
            ans.append("1")
        else:
            ans.append("2")
        idx = idx + 2
print("".join(ans))