import random

RANDOM_UPPER_BOUND = 100
SET_SIZE = 20
CHECK_SET_SIZE = 5

set_data = set()
s_for_check = set()

while len(set_data) != SET_SIZE:
    set_data.add(random.randint(0, RANDOM_UPPER_BOUND))

while len(s_for_check) != CHECK_SET_SIZE:
    s_for_check.add(random.randint(0, RANDOM_UPPER_BOUND))

print(f"{set_data} ---> {len(set_data)}")
print(f"{s_for_check} ---> {len(s_for_check)}")



print(f"Исходный SET содержит элемент: {set_data.intersection(s_for_check)}")



