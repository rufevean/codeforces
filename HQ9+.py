word = input()
import sys
language = {"H","Q","9"}
for char in word:
    if char in language:
        print("YES")
        sys.exit()
print("NO")
