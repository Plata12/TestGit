row = int(input())
for i in range(row):
    for j in range(row - i):
        print(" ", end=" ")
    for j in range(2 * i):
        print("*", end=" ")
    print("*")