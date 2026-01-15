expr =list(input().split("+"))
low = 0
high = len(expr)-1
mid = 0
while low <= mid <= high:
    if expr[mid] == '2':
        mid = mid + 1
    elif expr[mid] == '3':
        expr[mid],expr[high]= expr[high],expr[mid]
        high = high - 1 
    elif expr[mid] == '1':
        expr[mid],expr[low] = expr[low],expr[mid]
        low = low + 1
        mid = mid + 1
res = expr[0]
for exp in expr[1:]:
    res = res + "+" +exp
print(res)
