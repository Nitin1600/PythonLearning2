# public_area = "PB"
#
# def home():
#     private_area = "PT"
#     print(public_area)
#     print(private_area)
#
# def strange():
#     print(public_area)
#
# print(public_area)
# home()
# print(public_area)
# strange()

# public_toilet = "PB"

# local variables have more preference as comapre to public variables



# def home():
#     private_toilet = "PT"
#     print(private_toilet)
#     public_toilet = "LPB"
#     print(public_toilet)
#
#
# home()
#
#
# def strange():
#     print(public_toilet)
#     # print(private_toilet)
#
#
# print(public_toilet)
# # print(private_toilet)
# strange()

# def outer_function():
#     var1 = 30
#
#     def inner_function1():
#         print(var1)
#
#     def inner_function2():
#         print(var1)
#
#     inner_function1()
#     inner_function2()
#
# outer_function()

# my_shopping_list = ["bread", "milk", "butter"]
# print(my_shopping_list[0])
# print(len(my_shopping_list))
#
# def bring_more_food(my_list):
#     more_item = input("Enter items: ")
#     my_list.append(more_item)
#     my_list.remove(more_item)
#     my_list.insert(0, more_item)
#     return my_list

# l = bring_more_food(my_shopping_list)
# print(l)

# bring_more_food(my_list)

# # ✅ Understanding Decorators in Python
#
# def add_extra_security(func):
#     def wrapper():
#         print("1.Before the function is called")
#         print("2.Add helmet, golves, knee_guard, dash_cam")
#         drive_bike
#         func()
#         print("3.After the function is called")
#         print("4.Secure driving")
#     return wrapper()
#
# @my_decorator
# def drive_bike():
#     print("I am driving")

# @add_extra_security
# def drive_scooty():
#     print("Normal Function")

# def add_extra_security(func):
#     # two parts
#     # wrapper & call
#     def wrapper():
#         print("1.Before the function is called.")
#         print("2.Add Helmet, Dashcash, gloves, knee guards")
#         # drive_bike()
#         func()
#         print("3.After the function is called.")
#         print("4.Secure Driving")
#
#     return wrapper()
#
#
# # definition
# # @my_decorator
# # def drive_bike():
# #     print("I am driving")
#
# @add_extra_security
# def drive_scooty():
#     print("Normal Function")

# ✅ Understanding Decorators in Python

# def UI_Tc(custom_func):
#     def wrapper():
#         print("1.Before running UI Tc")
#         print("2.Starting the browser")
#         custom_func()
#         print("3.Ending the running UI Tc")
#         print("4.Quitting the browser")
#     return wrapper()
#
# @UI_Tc
# def test_UI():
#     print("I will start the TC")

# def start_Tc():
#     print("1.Before running UI Tc")
#     print("2.Starting the browser")
#
# def stop_Tc():
#     print("3.Ending the running UI Tc")
#     print("4.Quitting the browser")
#
# def test_UI():
#     print("I will test UI")
#
# start_Tc()
# test_UI()
# stop_Tc()

# import time
#
# def time_decorator(func):
#     def wrapper():
#         start_time = time.time()
#         print(start_time)
#         func()
#         end_time = time.time()
#         print(end_time)
#         print(f"Time taken by this function is {end_time - start_time}")
#     return wrapper()
#
# @time_decorator
# def test_UI1():
#     print("Add a function, time taken by this function1")
#     time.sleep(2)
#
# @time_decorator
# def test_UI2():
#     print("Add a function, time taken by the function2")
#     time.sleep(5)

# @staticmethod
# @classmethod
# @property
# @functools.wraps
# These we will use them int the OOPs

# def decorator1(func):
#     def wrapper():
#         print("Decorator 1")
#         func()
#
#     return wrapper
#
# def decorator2(func):
#     def wrapper():
#         print("Decorator2")
#         func()
#
#     return wrapper
#
# @decorator1
# @decorator2
# def say_hello():
#     print("Hello")
#
# say_hello()

# def decorator1(func):
#     def wrapper():
#         print("Decorator 1")
#         func()
#
#     return wrapper
#
#
# def decorator2(func):
#     def wrapper():
#         print("Decorator 2")
#         func()
#
#     return wrapper
#
#
# @decorator1
# @decorator2
# def say_hello():
#     print("Hello!")
#
#
# say_hello()

# # ✅ Type Conversions
# a = "10"
# print(type(a))
# a = int(a)
# print(a)
# print(type(a))
#
# print(float("3.14"))
# # int(), str(), float(), bool(), list(), tuple(),set(), dict(), complex()

# lambda expression
# A lambda is an anonymous function that returns some form of data.

# def triple_me(num):
#     return num ** 3
#
# l = triple_me(3)
# print(l)
#
# o = lambda num: num ** 3
# print(o(10))

# lambda expression
# A lambda is an anonymous function that returns some form of data.

# def add_10(n):
#     return n + 10
#
# o = add_10(100)
# print(o)
#
# oo = lambda n: n + 10
# print(oo(1000))

# def mul(a,b):
#     return a * b
#
# l = lambda a,b: a * b
# print(l(3,4))

# def add(a,b,c):
#     return a + b + c
#
# op = lambda a,b,c: a + b + c
# print(op(4,5,6))

# def check_odd_or_even(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# check_odd_or_even(9)

# l = lambda num:"Even" if num % 2 == 0 else "Odd"
# print(l(6))

# import math
#
# def pow(num):
#     return math.pow(num, 2)
#
# op1 = pow(10)
# print(op1)

# op2 = lambda : math.pow(int(input("Enter the number:\n")),2)
# print(op2())

#__init__.py

# create dir - normal folder - python doesn't serach the files here or code here.


# python is very, foler with file __int__.py - python will search the code here
# __init__.py -> dir -> module (where python will search better)

from src.Aug.ex_27082024.normal_directory.Lab091 import sum_1
from src.Aug.ex_27082024.python_package.Lab092 import sum_2

op1 = sum_1(3,4)
print(op1)

op2 = sum_2(4,5)
print(op2)