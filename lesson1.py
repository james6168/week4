# lambdas:
# map, filter, reduce
# decorators

# square_number = lambda x: x ** 2
#
# print(square_number(3))

# Example 2

# upper_str = lambda str: str.upper()
# print(upper_str("Fuck you"))

# Example 3

# sum_some_list_of_integers = lambda lists: sum(lists)
#
# print(sum_some_list_of_integers([23, 22, 44]))

# Example 4

# sum_num = lambda x, y: x * y
#
# print(sum_num(3, 7))
# print((lambda x, y: x * y))

# Example 5

# kpi = {
#     "math": [2, 4, 6, 7],
#     "py": [2, 33, 6, 87],
#     "java": [2, 55, 6, 77]
# }
# dict_numbers = {key: sum(value) for key, value in kpi.items()}

# print(dict_numbers)

# Example 6
# kpi = {
#     "math": [2, 4, 6, 7],
#     "py": [2, 33, 6, 87],
#     "java": [2, 55, 6, 77]
# }
#
# dict_keys = {key: sum(value) if sum(value) != 128 else None for key, value in kpi.items() if sum(value) > 50}
# print(dict_keys)

# Example 7

# list_num = [2, 4, 5, 6]
# dict_of_indexes_and_values = tuple(enumerate(list_num))
# print(dict_of_indexes_and_values)

# Example map 1

# list_radius = [12, 33, 45, 6]
#
# def get_square_circle(radius):
#     from math import pi
#     square = radius ** 2 * pi
#     return round(square, 2)
#
# # print(get_square_circle(34))
#
# list_square = list(map(get_square_circle, list_radius))
# print(list_square)

# Example map 2

# list_radius = [12, 33, 45, 6]
#
# def get_factorial(num):
#     total_factorial = 1
#     for i in range(1, num + 1):
#         total_factorial = total_factorial * i
#     return total_factorial
#
# print(list(map(get_factorial, list_radius)))

# Example map 3

# def sum_num (a, b, c):
#     return a + b * c
#
# list_numbers1 = [2, 4, 6, 7, 4]
# list_numbers2 = [2, 4, 6, 7]
# sum_list = list(map(sum_num, list_numbers1, list_numbers1, list_numbers1))
# print(sum_list)

# Filter


