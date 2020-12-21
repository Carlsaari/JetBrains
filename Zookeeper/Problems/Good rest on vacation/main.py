# put your python code here
duration = int(input())
food = int(input())
flight = int(input())
hotel = int(input())

total = (duration * food) + (flight * 2) + ((duration - 1) * hotel)

print(total)
