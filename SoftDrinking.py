input = list(map(int,input().split()))
people = input[0]
bottles = input[1]
volume = input[2]
limes = input[3]
slices = input[4]
salt = input[5]
nl = input[6]
np = input[7]


total_volume = bottles * volume
total_slices = limes * slices

toasts = 0

while total_volume >= nl and total_slices > 0 and salt >=np :
    toasts +=1
    total_volume -= nl
    total_slices -= 1
    salt -=np
print(toasts//people)
