# Calcluate the sum of odd numbers up to a given numbers n.


num = int(input("Enter n number : "))

Sum_odd = 0

for i in range(1, num+1):
    if i%2 != 0:
        Sum_odd += 1
        
print("Sum of odd number is: ", Sum_odd)