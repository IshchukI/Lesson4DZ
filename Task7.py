import random

RANDOM_UPPER_BOUND = 50
FIRST_SET_SIZE = 10
SECOND_SET_SIZE = 10

set_data_1 = set()
set_data_2 = set()

while len(set_data_1) != FIRST_SET_SIZE:
    set_data_1.add(random.randint(0, RANDOM_UPPER_BOUND))

while len(set_data_2) != SECOND_SET_SIZE:
    set_data_2.add(random.randint(0, RANDOM_UPPER_BOUND))

print(f"A: {set_data_1} ---> {len(set_data_1)}")
print(f"B: {set_data_2} ---> {len(set_data_2)}")


set_data_1 = set_data_1.difference(set_data_2)

print(f"элементы в наборе A без эелемнтов в наборе B:\n{set_data_1}")