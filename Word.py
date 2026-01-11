word = input()
upper = 0
for char in word:
    if char == char.upper():
        upper = upper + 1
if upper > len(word)-upper:
    print(word.upper())
else:
    print(word.lower())