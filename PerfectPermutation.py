import sys
n = int(input())
if n %2 ==  1:
    print(-1)
    sys.exit()
res = []
for i in range(0,n,2):
    res.append(str(i+2))
    res.append(str(i+1))
print(' '.join(res))
