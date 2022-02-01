tup_1 = (1, 2, 3, 4, 5)
tup_2 = (3, 5, 2, 1)
tup_3 = (2, 2, 3, 1, 2, 2)
sum = list()

max_len = max(len(tup_1), len(tup_2), len(tup_3))

for i in range(0, max_len):
    if i >= len(tup_1):
        tup1_val = 0
    else:
        tup1_val = tup_1[i]

    if i >= len(tup_2):
        tup2_val = 0
    else:
        tup2_val = tup_2[i]

    if i >= len(tup_3):
        tup3_val = 0
    else:
        tup3_val = tup_3[i]

    sum.append(tup1_val + tup2_val + tup3_val)

tup_sum = tuple(sum)

print(f"{tup_1} + \n{tup_2} + \n{tup_3}  ")
print("_"*3*max_len)
print(tup_sum)
