# Reverse a string using a loop.

str = input("Enter your string: ")

reversed_str =""

for i in str:
    # reversed_str = reversed_str + i    # return same string
    reversed_str = i + reversed_str      # return reversed string
    
print(reversed_str)    