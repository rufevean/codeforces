t = int(input())
for _ in range(t):
    n, m, h = map(int, input().split())
    base = list(map(int, input().split()))
    add = [0] * n
    for _ in range(m):
        idx, val = map(int, input().split())
        idx -= 1
        add[idx] += val
        if base[idx] + add[idx] > h:
            add = [0] * n
    result = [base[i] + add[i] for i in range(n)]
    print(*result)
