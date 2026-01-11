num = input()
lucky_digits = 0
for n in num:
    if n == '4' or n == '7':
        lucky_digits += 1
flag = True 
for n in str(lucky_digits):
    if n != '4' and n != '7':
        flag = False
print("YES" if flag else "NO")