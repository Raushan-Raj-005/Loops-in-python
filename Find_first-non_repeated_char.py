# Given a string, find the first non-repeated character.

str = input("Enter your string: ")

for i in str:
    print(i)
    if str.count(i) == 1:
        print("Character is: ", i)
        break