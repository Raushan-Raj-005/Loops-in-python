# Print the multiplication table for a given number up to 10. but skip the fifth iteration.

Table =int(input("Enter your number: "))

for i in range (1, 11):
    if i == 5:
        continue
    print(Table, 'X', i, Table * i)
    
    