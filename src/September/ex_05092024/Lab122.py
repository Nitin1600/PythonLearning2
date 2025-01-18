# a = 10
# class Myclass:
#
#     # public var (instance)
#     public_var = "I am PUBLIC"
#     __balance = 100
#
#     # Private variable
#     __private_var = "I am private."
#     __password = "1234"
#     # Protected variable
#     _protected_var = "I am protected."
#     b = 10
#     _c = 20
#     __d = 45
#     college = "ABC"
#     pramod =  "TTA"
#     __pramod_bank =  100000000000
#
#
#
#
# object = Myclass()
# print(object.public_var)
# print(object._protected_var)
# # print(object.__balance)
# # print(object.__private_var)
# # print(object.__password)

# class Bank:
#     def __init__(self, account_number, balance):
#         self.balance = balance
#         self.__account_number = account_number
#
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#
#     def check_balance(self):
#         print(self.balance)
#
#     def show_me_account_info(self, is_auth):
#         if is_auth == True:
#             print(self.__account_number)
#         else:
#             print("Not allowed")
#
#     def __internal_method(self):
#         print("Private Method")
#         print(self.__account_number)
#         self.show_me_account_info(True)
#
# icici = Bank(9834756234, 100)
# # icici.__init__()
# icici.deposit(100)
# icici.check_balance()
# icici.show_me_account_info(True)
# icici.deposit(100)
# icici.check_balance()
# icici._Bank__internal_method()

# class Bank:
#     def __init__(self, account_number, balance):
#         self.balance = balance
#         self.__account_number = account_number
#
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#
#     def check_balance(self):
#         print(self.balance)
#
#     def show_me_account_number(self, is_auth):
#         if is_auth == True:
#             print(self.__account_number)
#         else:
#             print("Not Allowed!")
#
#     def __internal_method(self):
#         print("Private Method")
#         print(self.__account_number)
#         self.show_me_account_number()
#
#
#
# icici = Bank(9876543210, 100)
# # icici.__init__()
# icici.deposit(100)
# icici.check_balance()
# icici.show_me_account_number(False)
# icici.deposit(100)
# icici.check_balance()
# # icici.__internal_method() - Error

# class Father:
#     key = "2BHK"
#
#     def car(self):
#         print("Father's car", "ALTO", self.key)
#
# class Son(Father):
#     key2 = "3BHK"
#
#     def home(self):
#         print("3BHK")
#
#     def truck(self):
#         print("Truck")
#
# father = Father()
# father.car()
# print(father.key)
# # father.truck()
#
# son = Son()
# son.car()

# class Father:
#     gold = "2kg"
#
#     def BHK2(self):
#         print("2BHK")
#
# class Son(Father):
#     diamond = "Diamond"
#
#     def BHK3(self):
#         print("3BHK")
#
# son = Son()
# print(son.gold)
# son.BHK2()
# son.BHK3()
#
# father = Father()
# print(father.diamond)
# father.BHK3()
# father.BHK2()

# Multilevel Inheritance

# class GrandFather:
#     gold = "2Kg"
#
#     def bhk1(self):
#         print("1BHK")
#
# class Father(GrandFather):
#     diamond = "22 karat"
#
#     def bhk2(self):
#         print("2BHK")
#
# class Son(Father):
#     btc = "1 btc"
#
#     def bhk3(self):
#         print("3BHK")
#
# gf = GrandFather()
# f = Father()
# s = Son()

# class Son:
#     gold = "1kg"
#
# class Father(Son):
#     diamond = "22karat"
#
# class GrandFather(Father):
#     btc = "1btc"
#
# gf  = GrandFather()
#
# class Father:
#     key = "ABC"
#     __password = "private"
#
#     def __show_password(self):
#         print(self.__password)
#
#     def father_money(self):
#         return 2
#
#     def home(self):
#         print("This is from father")
#
#     def show_everything(self):
#         self.__show_password()
#
# class Mother:
#
#     def mother_money(self):
#         return 5
#
#     def home(self):
#         print("This is mother's money")
#
# class Son1(Mother, Father):
#     pass
#
# class Son2(Father, Mother):
#     pass
#
# s = Son1()
# print(s.father_money())
# print(s.mother_money())
# print(s.home())
# print(s.key)
# s.show_everything()

# class A:
#     def method(self):
#         return "Method A"
#
# class B:
#     def method(self):
#         return "Method B"
#
# class C(A,B):
#     pass
#
# c = C()
# print(c.method())
# print(c.method())

# class GrandParent:
#     key = "1Kg"
#     def grandparents_method(self):
#         return "GrandParent's_method"
#
# class Parent(GrandParent):
#     def parents_method(self):
#         return "Parent's_method"
#
# class Child(Parent):
#     mac = "M4"
#     def childs_method(self):
#         return "Child's_method"
#
# c = Child()
# # print(c.childs_method())
# print(c.grandparents_method())

# import numpy as np
# # arr1 = np.array([1,2,3,4])
# # arr2 = np.flip(arr1)
# # print(arr2)
#
# arr1 = np.array([1,2,3,4])
# # arr2 = arr1[::-1]
# # print(arr2, end=",")
#
# # print(arr1[element])
# print(arr1[1])
# x=np.delete(arr1, 2)
# print(x)
# # array_name[index] = element
# arr1[2] = 5
# print(arr1)

# list1 = ["w", "a", "w", "b"]
# list2 = ["e", "", "riting", "log"]
# list3 = [x+y for x,y in zip(list1, list2)]
# print(list3)

# list1 = [1,2,3,4]
# list2 =[]
# for x in list1:
#     list2.append(x*x)
# print(list2)

# a = 'This is a String'
# li =a.split(" ")
# print(li)
# "".join(li)
# print(li)

# s = "       Hello, World!           "
# print(len(s))
# print(s.strip())

# print(s.replace("World", "Universe"))
# print(s.split(','))
#
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.isalnum())
# print(s.isalpha())

# x=10
# def func():
#     x=5
#     print(x)
# func()
# print(x)

# a=lambda x:x+10
# print(a(5))

# from math import sqrt
#
# def prime_or_not(number):
#     for i in range(2, int(sqrt(number)) + 1):
#         if number % i == 0:
#             return 0
#     return 1
#
# # prime_or_not(2)
# print(prime_or_not(98))

# def factorial(n):
#     if n==1:
#         return n
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# from functools import reduce
# a=reduce(lambda x,y:x if x<y else y)
# print(a(2,3))

# a=[i for i in range(10) if i % 2 != 0]
# print(a)

# # dict_[min(dict_.keys(), key=(lambda k: dict_[k]))]
# def mean_tuple(numbers):
#     result = [sum(x)/len(x) for x in zip(*numbers)]
#     return result

# import numpy as np
# a=np.array([[1,2], [3,4]])
# b=np.array([[5,6]])
# c=np.concatenate((a,b), axis=0)
# print(c)

# result=np.char.join(",", array)

# New_arr = np.pad[existing_arr, pad_width=1, mode='constant', constant_value=1]
# np.swapaxes(arr,0,1)

# array.argsort() [ -N: ] [: : -1]

# df["column"] = df["column"].astype(int)

# df.sort_values(by=['col1', 'col2'])

# df['column'].idmax()

# df.pct_change(periods=1)

# df.std()/df.mean()

numpy.unique(list, return_counts=True)