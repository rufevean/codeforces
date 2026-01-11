def LightsOut(matrix):
    default = [[True,True,True] for _ in range(3)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for _ in range(int(matrix[i][j])%2):
                default[i][j] = not default[i][j]
                if i > 0:
                    default[i-1][j] = not default[i-1][j]
                if i < len(matrix)-1:
                    default[i+1][j] = not default[i+1][j]
                if j > 0:
                    default[i][j-1] = not default[i][j-1]   
                if j < len(matrix[0])-1:
                    default[i][j+1] = not default[i][j+1]
    for i in range(len(default)):
        for j in range(len(default)):
            default[i][j] = '1' if default[i][j] else '0'
    return default
test = []
for _ in range(3):
    test.append(list(map(int,input().split())))
resmat = LightsOut(test)
for row in resmat:
    print("".join(row))
