for _ in range(int(input())):
    nr,spikes,ins = map(int,input().split())
    pos = list(map(int,input().split()))
    alive = [1]*nr
    spike_pos = set(map(int,input().split()))
    instructions = input()
    ans = []
    for char in instructions:
        if char == "L":
            for idx,p in enumerate(pos):
                pos[idx] = p - 1
                if pos[idx] in spike_pos:
                    alive[idx] = 0
        else:
            for idx,p in enumerate(pos):
                pos[idx]= p + 1
                if pos[idx] in spike_pos:
                    alive[idx] = 0
        ans.append(sum(alive))
    print(*ans)




