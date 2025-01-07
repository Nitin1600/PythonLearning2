# class Person:
#     def __init__(self):
#         self.name = input("Enter name:\n")
#         self.age = input("Enter age:\n")
#         self.phone = input("Enter phone:\n")
#         self.occupation = input("Enter your occupation:\n")
#
#     def display(self):
#         print(f"Name is {self.name}", f"Age is {self.age}", f"Phone is {self.phone}",
#               f"Occupation is {self.occupation}")
#
# person1 = Person()
# person1.display()
# from pandas.io.sas.sas_constants import os_name_length

# from src.Aug.ex_13082024.Lab016 import name2


# class Calc:
#     def __init__(self):
#         print("DC")
#
#     def sum(self, a,b):
#         return a+b
#
#     def sub(self, a,b):
#         return a-b
#
#     def mul(self, a,b):
#         return a*b
#
#     def div(self, a,b):
#         return a/b
#
# object_ref = Calc()
# a = float(input("Enter the number: "))
# b = float(input("Enter the number: "))
# output_sum = object_ref.sum(a,b)
# output_sub = object_ref.sub(a,b)
# output_mul = object_ref.mul(a,b)
# output_div = object_ref.div(a,b)
#
# print(output_sum, output_sub, output_mul, output_div)

# class Calc:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def sum(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
#
# object_ref = Calc(3,4)
# object_ref2 = Calc(3,4)
# object_ref3 = Calc(3,4)
# object_ref4 = Calc(3,4)
# output = object_ref.sum()
# print(output)

#  Class Variable.
#  Method
#      # Public - Variable - Don't Mention anything
#      # Protected - _
#      # Private - __
# Inheritance
# Polymorphism
# Abstraction,
# Encapsulation
# Static Method
# Variables


# Variables
# 1. Local Variable (within the functionc / block
# 2. global
# 3. instance variable (within the class
# 4. static variable ( in future)

# a = 10
#
# class Person:
#     b = 11
#     c = 11
#
#     def print_infor(self):
#         global a
#         a = "Hello"
#         print(self.b)
#         print(self.c)
#
# obj_ref = Person()
# obj_ref.print_infor()
# print(a)

# count = 0
#
# def increament():
#     global count
#     count = count + 1
#
# increament()
# increament()
# increament()
# increament()
# increament()
# print(count)

# count = 0


# def increament():
#     global count
#     count = count + 1
#
#
# increament()
# increament()
# increament()
# increament()
# print(count)

# class Person:
# # Class Variables
# # Instance variables
# # name = "Amit" # hardcoded value
#         def __init__(self, name):
#             self.name = name
#
#         def walk(self):
#             return self.name
#
# amith = Person("amith")
# vinay = Person("vinay")
# print(amith.name)
# print(vinay.name)
# print("Who is walking with object vinay-> ", vinay.walk())

# class Person:
#     # Class Variables
#     # Instance variables
#     # name = "Amit" # hardcoded value
#     def __init__(self, name):
#         self.name = name

#     def walk(self):
#         return self.name
#
#
# amit = Person("amit")
# pramod = Person("pramod")
# print(amit.name)
# print(pramod.name)
# print("Who is walking with the object pramod -> ", pramod.walk())

# class Car:
#     def __init__(self, o_name, o_make, o_model):
#         self.name = o_name
#         self.make = o_make
#         self.model = o_model
#
#     def start_engine(self):
#         print("Starting a car with name " + self.name)
#         print("Starting a car with make " + self.make)
#         print("Starting a car with model " + self.model)
#
# lambo = Car("Lambo", "V2", "2024")
# lambo.start_engine()
#
# xuv = Car("XUV", "V6", "2023")
# xuv.start_engine()

# class VWOLoginPage:
#     def __init__(self, email_arg, password_arg):
#         self.email = email_arg
#         self.password = password_arg
#
#     def login_confirm(self):
#         if self.email == "amith@gmail.com" and self.password == "Pass@123":
#             print("Allowed to login")
#         else:
#             print("Not Allowed")
#
# email = input("Enter mail id:\n")
# password = input("Enter password:\n")
#
# vwo_obj = VWOLoginPage(email, password)
# vwo_obj.login_confirm()
#
# amith = VWOLoginPage("amith@gmail.com", "Pass@123")
# amith.login_confirm()

# class Car:
#     name = None
#     make = None
#     password = 123
#
#     def __init__(self):
#         self.password = "amith"
#
#     def change_password(self):
#         print(self.password)
#
# obj = Car()
# print(obj.password)
# obj.change_password()


