import random


LIST_SIZE = 10
RANDOM_UPPER_BOUND = 100

l = list()
t = tuple()

for _ in range (0, LIST_SIZE):
    l.append(random.randint(0, RANDOM_UPPER_BOUND))
    l.append(random.randint(0, RANDOM_UPPER_BOUND)/10)

t = tuple(l)

print(f"list: {l}, type: {type(l)}")
print(f"tuple: {t}, type: {type(t)}")







