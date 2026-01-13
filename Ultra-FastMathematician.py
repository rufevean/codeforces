num1 = input()
num2 = input()
res = []
for i in range(len(num1)):
    res.append(str(int(num1[i])^int(num2[i])))
print(''.join(res))