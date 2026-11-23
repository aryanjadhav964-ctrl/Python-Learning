# taking inour a number from user
user_number = int(input(" Enter your Number : "))

## the logic
if user_number % 2 == 0:
    print(f" Your number {user_number} is even number")
elif user_number % 2 == 1:
    print(f" Your number {user_number} is odd number")