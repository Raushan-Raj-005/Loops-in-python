# Check if a number is prime.

num = int(input("Enter a Number: "))

is_prime = True  #take an Assumption 

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break
        
print(is_prime)
