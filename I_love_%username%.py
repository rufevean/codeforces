n = int(input())
perf = list(map(int,input().split()))

curr_max = perf[0]
curr_min = perf[0]
amazing = 0

for per in perf[1:]:
    if per > curr_max:
        amazing = amazing + 1
        curr_max = per 
    elif per < curr_min:
        amazing = amazing + 1
        curr_min = per 
print(amazing)