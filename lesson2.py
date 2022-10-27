# Dicts Methods

from copy import deepcopy

# test = {"test": "test"}
#
# student = {
#     "name": "Chingiz",
#     "surname": "Chingizov",
#     "subjects": [
#         {"name": "math", "grade": 80},
#         {"name": "programming", "grade": 101}
#         **test
#     ]
# }
#
# student2 = deepcopy(student)
#
#
# student2['subjects'][0]['grade'] = 85

# print(student)
# print(student2)
#
# print(student.items())
# print(student.popitem())
# print(student)

# print(student.setdefault("surname", "Asanov"))
# print(student)

# student.update((("surname", "Asanov"), ("name", "Beka")))
# print(student)

# Values
# print(student.keys())

# a = "".join(["1", "1"])
# print(a)

#set collection

# sets = set()
# print(type(sets))

# profession = {"backend", "backend", 12, (), (1, 2)}
# for i in profession:
#     print(i)

# print(profession)

# list_set = tuple(profession)
#
# print(list_set)


# cities = {"Tokyo", "Naryn", "Bishkek", "Baku", "Karakol", "Batken"}
# towns = {"Naryna", "Batkena"}

# cities.add("Stokholm")

# print(dir(cities))

# cities.clear()

# a = cities.copy()

# cities.discard("Tokyo")

# cities.remove("Baku")

# city_town = cities.union(towns)
#
# cities.update({1: 5, 8: 9}.values())
#
# print(cities)
# print(towns)

# inter = cities.intersection(towns)
#
# print(inter)

# cities.intersection_update(towns)
#
# print(cities)

# print(cities.symmetric_difference(towns))

# towns.symmetric_difference(cities)
# towns.symmetric_difference_update(cities)
# print(towns)

# pop_element = cities.pop()
#
# print(pop_element)

# towns.update(("nazgul",))
# print(towns)

# print(cities.issubset(towns))
# print(cities.issuperset(towns))

# print(cities.isdisjoint(towns))

#collections

# Задача

student = {
    "name": "Nazgul",
    "age": 18,
    "year": None,
    "subjects": {
        "math": (80, 47, 68, 100),
        "python": (67, 88, 97, 88),
        "html": (67, 80, 97, 88),
        "css": (67, 88, 91, 88),
        "hist": (64, 64, 24, 56)
    },
    "total": None
}

# Solution
# student["year"] = 2022 - 18
#
# list_of_marks = student.get("subjects").values()
#
# list_of_averages = []
#
# for i in list_of_marks:
#     list_of_averages.append(int(sum(i)/len(i)))
#
# student["total"] = int(sum(list_of_averages)/len(list_of_averages))

# print(student)

# Решение от ментора:

student["year"] = 2022 - student["age"]

#find average of each subject

for key, value in student["subjects"].items():
    student["subjects"][key] = sum(value) / len(value)

#find total average

student["total"] = sum(student["subjects"].values()) / len(student["subjects"])
print(student)








