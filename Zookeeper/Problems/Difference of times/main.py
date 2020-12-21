# put your python code here
first_hours = int(input())
first_minutes = int(input())
first_seconds = int(input())

second_hours = int(input())
second_minutes = int(input())
second_seconds = int(input())

first = (first_hours * 60 * 60) + (first_minutes * 60) + first_seconds
second = (second_hours * 60 * 60) + (second_minutes * 60) + second_seconds

result = second - first
print(result)
