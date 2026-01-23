def solve():
    high,row,col = map(int,input().split())
    array = list(map(int,input().split()))
    array.sort()
    array.reverse()
    pairs = high // 2
    sum = 0
    visited = set()
    for idx,val in enumerate(array):
        for idx2,j in enumerate(array):
            if  val<= row and j<= col and pairs > 0 and idx not in visited and idx2 not in visited and idx != idx2:
                visited.add(idx)
                visited.add(idx2)
                pairs = pairs - 1
                sum = sum + 1
    print(sum)

x = int(input())
for _ in range(x):
    solve()
