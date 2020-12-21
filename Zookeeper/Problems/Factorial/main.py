start = int(input())
factorial = start - 1

while factorial > 0:
    start *= factorial
    factorial -= 1

print(start)

