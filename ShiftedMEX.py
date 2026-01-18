t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    sarray = list(set(array))
    sarray.sort()
    highest = 0
    curr = 0
    for i in range(len(sarray)):
        if i == 0 or sarray[i] != sarray[i - 1] + 1:
            curr = 1
        else:
            curr += 1
        highest = max(highest, curr)
    print(highest)
