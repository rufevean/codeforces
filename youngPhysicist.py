n = int(input())
res = [0,0,0]
for _ in range(n):
    arr = list(map(int,input().split()))
    for a in range(3):
        res[a] += arr[a]
if max(res) == min(res) == 0:
    print("YES")
else:
    print("NO")
