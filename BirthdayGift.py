#n,k = map(int,input().split())
n =3
k =2

dp = [[0]*(n+1) for _ in range(k+1)]

for j in range(1,n+1):
    dp[1][j] = 1

for size in range(2,k+1):
    for first in range(1,n+1):
        for last in range(1,n+1):
            if last % first == 0:
                dp[size][last] += dp[size-1][first]
count = 0
for j in range(1,n+1):
    count = count + dp[k][j]
print(count)
print(dp)
