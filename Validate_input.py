# keep asking the user for input until they enter a number b/w 1 and 10.

while True:
    num = int(input("Enter value b/w 1 and 10: "))
    if 1<= num <= 10:
        print("Thanks")
        break
    else:
        print("Invalid Entery, please enter number b/w 1 and 10")