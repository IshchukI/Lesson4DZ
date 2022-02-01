import random

RANDOM_UPPER_BOUND = 100

list_data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
inner_tuples_as_list = list()
list_data_after_changes = list()

for item in list_data:
    inner_tuples_as_list.append(list(item))



for item in inner_tuples_as_list:
    item[-1] = random.randint(0, RANDOM_UPPER_BOUND)


for item in inner_tuples_as_list:
    list_data_after_changes.append(tuple(item))

print(f"исходный список c кортежами: {list_data}")
print(f"список списков: {inner_tuples_as_list}")
print(f"обратно в список c кортежами: {list_data_after_changes}")



