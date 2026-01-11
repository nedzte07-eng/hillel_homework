list_for_6_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

sum_of_even = 0
for item in list_for_6_4:
    if item % 2 == 0:
        sum_of_even += item

print(sum_of_even)