# Compute the factorial of a number using While loop.

num = int(input("Enter your number: "))
factorial = 1

while num > 0:
    # factorial = factorial * num
    # num = num - 1
    
    factorial *= num
    num -= 1
    
print("Factorial is: ", factorial)    
