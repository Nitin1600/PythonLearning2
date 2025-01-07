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

