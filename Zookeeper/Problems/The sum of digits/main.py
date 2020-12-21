# put your python code here
integer = int(input())
first = integer // 100
second = integer // 10 - first * 10
third = integer // 1 - first * 100 - second * 10
total = first + second + third
print(total)

