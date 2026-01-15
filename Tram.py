n = int(input())
cap = 0
enter = 0
exit = 0
curr = 0 
for _ in range(n):
    o,i = map(int,input().split())
    curr = curr - o + i 
    cap = max(curr,cap)
print(cap)