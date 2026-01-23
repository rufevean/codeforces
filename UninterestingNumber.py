def sol():
    arr = list(map(int,list(input())))
    twos = arr.count(2)
    threes = arr.count(3)
    for i in range(min(9,twos+1)):
        for j in range(min(9,threes+1)):
            if (sum(arr) + 2*(i) + 6*(j)) % 9 == 0:
                print("YES")
                return
    print("NO")
    return


for _ in range(int(input())):
    sol()


