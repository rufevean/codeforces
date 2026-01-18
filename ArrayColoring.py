n = int(input())
for _ in range(n):
    size = int(input())
    array = list(map(int, input().split()))
    """
        Blue - 0
        Red - 1
    """
    color = {}
    flag = False
    for num in array:
        color[num] = not not flag
        flag = not flag
    array.sort()
    ans = True
    for i in range(1,size):
        if color[array[i]] == color[array[i-1]]:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")


