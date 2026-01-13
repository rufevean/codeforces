n = int(input())
seq = list(map(int,input().split()))
first  = float('-inf')
firstidx = 0
last = float('inf')
lastidx = len(seq)-1
ll = len(seq)-1

for idx,sol in enumerate(seq):
    if sol > first:
        firstidx = idx
        first = sol 
    if sol <= last:
        lastidx = idx 
        last = sol 
if firstidx > lastidx :
    print(ll-lastidx + firstidx - 1 ) 
else:
    print(ll-lastidx+firstidx)



