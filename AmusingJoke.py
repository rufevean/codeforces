from collections import defaultdict
gn = input()
rh = input()
pile = input()
grc  = defaultdict(int)
pilec = defaultdict(int)
for char in gn:
    grc[char] +=1
for char in rh:
    grc[char] +=1
for char in pile:
    pilec[char] +=1
print("YES" if pilec == grc else "NO")
