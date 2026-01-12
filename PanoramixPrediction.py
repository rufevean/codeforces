import math
n,m = map(int,input().split())
flag = True

def isPrime(num):
    check = int(math.sqrt(num))
    for i in range(2,check+1):
        if num % i == 0:
            return False
    return True
if not isPrime(m):
    print("NO")
else:
    for i in range(n+1,m):
        if isPrime(i):
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")


    