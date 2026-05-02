# Given a list of numbers, count how many are positive & negative.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count = 0
negative_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Total positive numbers count is: ", positive_number_count)

for num in numbers:
    if num < 0:
        negative_number_count += 1
print("Total negative number count is: ", negative_number_count)