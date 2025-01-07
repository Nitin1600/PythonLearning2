# User Defined
# 1. The can't return -> non return
# 2.They can return something
# They have parameters
# They don't parameters / arguments


# 1. The can't return -> non return
# # No Return Type and No Parameter / Argument - NRNP
# def greet():
#     print("Hello, there!")
#
# result = greet()
# print(result)

# 2. # No Return Type and with Argument
# def greet_by_name(name):
#     print("Hello,", name)
#
# greet_by_name("Amith")

# 3. No Return Type and with Default Argument

# def greet_default(name="Amith"):
#     print("Hello", name.upper())
#
# greet_default("Brar")
# greet_default()
# greet_default(name="Mahesh")

# def greet(name1="Amith", name2="Shilpa", name3="Mani"):
#     print("Multiple_arguments", name1,name2,name3)
#
# greet()
# greet(name1="Kallu")
# greet(name3="Kallu")

# def sum_of_two_numbers(num1,num2):
#     return num1 + num2

def sum_of_two_numbers(num1=100,num2=200):
    return num1 + num2

result = sum_of_two_numbers(10,34)
result2 = sum_of_two_numbers(num2=10,num1=34)
result3 = sum_of_two_numbers()
print(result)
print(result2)
print(result3)