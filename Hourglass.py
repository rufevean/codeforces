"""
WRONG SOLUTION
"""
"""
n = int(input())
# n =1
for _ in range(n):
    capacity,flip,time = map(int,input().split())
    up_flip = 0
    if time > flip:
        time = (time%flip) + flip
    down_flip = capacity
    curr = 0
    while True:
        if curr == time:
            if (time // flip) % 2 == 0:
                print(down_flip)
                break
            else:
                print(up_flip)
                break
        if ( curr // flip ) % 2 == 0 and down_flip > 0:
            down_flip = down_flip - 1 
            up_flip = up_flip + 1 
        elif (curr // flip) % 2 and up_flip >0:
            down_flip = down_flip + 1
            up_flip = up_flip - 1
        curr = curr + 1
"""


"""
CORRECT SOLUTION
"""

n = int(input())
for _ in range(n):
    capacity,flip,time = map(int,input().split())
    cycle = 2 * capacity 

    time = time % cycle 
    if time <= capacity :
        up = time
    else:
        up = cycle - time
    down = capacity - up
    print(down)