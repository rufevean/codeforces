length = int(input())
stones = input()
left = 0
c = 0 
for right in range(1,len(stones)):
    if stones[right] == stones[left]:
        c = c + 1
    else:
        left = right
print(c)

