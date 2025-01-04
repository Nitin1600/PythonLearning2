# Conditions and Loops

# Write a program to take a user age and let him know if he can go the club.
# 21

# Logic Building
# 1. user input - data type -> int
# o/p -> String -> user if he can go or not.


# 2. Rough loigc
# age  > 21 -> print can go
# age < 21 -> print can't go

age = input("Enter the age: \n")
age = int(age)

if age >= 21:
    print(f"Can go club with {age} years of age")
else:
    print(f"Can't go with {age} years of age")