k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
fought = [False]*d 
for i in range(1,d+1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        fought[i-1] = True 
count = 0
for fight in fought:
    if fight:
        count = count + 1
print(count) 