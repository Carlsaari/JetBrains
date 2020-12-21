# put your python code here
first_group = int(input())
second_group = int(input())
third_group = int(input())

first_desks = first_group % 2 + first_group // 2
second_desks = second_group % 2 + second_group // 2
third_desks = third_group % 2 + third_group // 2

desks = first_desks + second_desks + third_desks
print(desks)
