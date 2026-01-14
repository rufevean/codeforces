from collections import defaultdict
n = int(input())
left = defaultdict(int)
right = defaultdict(int)
for _ in range(n):
    l,r = input().split()
    left[l] +=1
    right[r] +=1 

c = 0
if left['0'] > left ['1']:
    c = c + left['1']
else:
    c = c + left['0']
if right['0'] > right['1']:
    c = c + right['1']
else:
    c = c + right['0']
print(c)