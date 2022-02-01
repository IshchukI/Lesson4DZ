import random

RANDOM_UPPER_BOUND = 100
FIRST_SET_SIZE = 10
SECOND_SET_SIZE = 5

set_data_1 = set()
set_data_2 = set()

while len(set_data_1) != FIRST_SET_SIZE:
    set_data_1.add(random.randint(0, RANDOM_UPPER_BOUND))

while len(set_data_2) != SECOND_SET_SIZE:
    set_data_2.add(random.randint(0, RANDOM_UPPER_BOUND))

print(f"{set_data_1} ---> {len(set_data_1)}")
print(f"{set_data_2} ---> {len(set_data_2)}")


if len(set_data_1.intersection(set_data_2)) == 0:
    print("Общих элементов нет")
else:
    print(f"Общие элементы: {set_data_1.intersection(set_data_2)}")