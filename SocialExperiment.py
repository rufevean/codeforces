n = int(input())
for _ in range(n):
    people = int(input())
    if people <= 3:
        print(people)
    else:
        if not people%2:
            print(0)
        else:
            print(1)
