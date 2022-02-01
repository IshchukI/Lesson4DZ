import random

RANDOM_UPPER_BOUND = 50
FIRST_LIST_SIZE = 5
SECOND_LIST_SIZE = 5

list_data_1 = list()
list_data_2 = list()
set_data_1 = set()
set_data_2 = set()

while len(list_data_1) != FIRST_LIST_SIZE:
    el = random.randint(0, RANDOM_UPPER_BOUND)
    if el not in list_data_1:
        list_data_1.append(el)

while len(list_data_2) != SECOND_LIST_SIZE:
    el = random.randint(0, RANDOM_UPPER_BOUND)
    if el not in list_data_2:
        list_data_2.append(el)

set_data_1 = set(list_data_1)
set_data_2 = set(list_data_2)

print(f"A: {list_data_1} ---> {len(list_data_1)}")
print(f"B: {list_data_2} ---> {len(list_data_2)}")
print("-----------------------------------------")
print(f"A: {set_data_1} ---> {len(set_data_1)}")
print(f"B: {set_data_2} ---> {len(set_data_2)}")
print(set_data_1.union(set_data_2))
print("-----------------------------------------")

for item in list_data_2:
    if item not in list_data_1:
        list_data_1.append(item)


print(list_data_1)
