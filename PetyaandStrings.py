import sys
word1  = input()
word2  = input()

val1 = 0
val2 = 0
i = 0
for i in range(len(word1)):
    val1 += ord(word1[i].lower())
    val2 += ord(word2[i].lower())
    if val1 < val2:
        print(-1)
        sys.exit()
    elif val1 > val2:
        print(1)
        sys.exit()

print(0)
