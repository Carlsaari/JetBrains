initial = int(input())
final = int(input())
counter = 0

while initial >= final:
    counter += 12
    initial /= 2

print(counter)
