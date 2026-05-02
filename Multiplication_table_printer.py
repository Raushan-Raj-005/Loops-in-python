# Print the multiplication table for a given number up to 10.

Table = int(input("Enter your number: "))

for i in range(1, 11):
    print(Table, 'X', i, '=', Table * i )
    