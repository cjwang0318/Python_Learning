#https://www.youtube.com/watch?v=ZW-TWrEF6qc
# 1. swap variables
a = 5
b = 10
a, b = b, a
print(a, b)

# 2. list comprehension
# squares = []
# for i in range(10):
#     if i % 2 == 0:
#         squares.append(i*i)
# print(squares )

squares = [i*i for i in range(10) if i % 2 == 0]
print(squares)

# 3, print without new lines
# data = [0, 1, 2, 3, 4, 5]
# for i in data:
#     print(i, end=" ")
# print()
# print("'done" )
data = [0, 1, 2, 3, 4, 5]
print(*data)

# 4, space separated numbers to integer list
user_input = "1 2 3 4 5 6"
my_list = list(map(int, user_input.split()))
print(my_list)

# 4, reading file into list
names = [line.strip() for line in open("names.txt", "r")]
print(names)