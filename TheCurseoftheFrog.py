
"""
    INCOMPLETE SOLUTION
"""
import collections
def solve():
    jumps,dest = map(int,input().split())
    jump_data = []
    step_data = []
    rollback = []
    r_m = collections.defaultdict(list)

    for _ in range(jumps):
        pos,step,neg = map(int,input().split())
        jump_data.append(pos)
        step_data.append(step)
        rollback.append(neg)
    for i in range(len(max(step_data))):
        for idx,jump in enumerate(jump_data):
            if not step_data[idx] % rollback[i] == 0:
                r_m[i].append(jump)
            else:
                r_m[i].append(jump-rollback[idx])

    for r_m in r_m.values():
        r_m.sort(reverse=True)
    print(r_m)
    curr = 1
    cp = 0
    while cp < dest:
        curr_jumps_pos = []
        for key,val in r_m.items():
            if curr % key == 0:
                curr_jumps_pos.extend(val)
        j = 0
        curr_jumps_pos.sort(reverse=True)
        while curr_jumps_pos[j] >= 0:

            pass






n = int(input())
for _ in range(n):
    solve()
