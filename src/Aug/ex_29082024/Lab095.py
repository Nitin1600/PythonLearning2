# squares = [1, 4, 9, 16, 25]
# print(squares.pop())
# print(squares)

# squares = [1, 4, 9, 16, 25]
# print(squares.pop())
# print(squares)

# shopping_list_wife = ["bread", "butter", "paneer"]
# shopping_list_wife[2] = "milk"
# print(shopping_list_wife)

# squares = [1, 4, 9, 16, 25]
# # List is Mutable in nature
# # mutable - change -
#
# squares[3] = 64
# print(squares)  # [1, 4, 9, 64, 25]
#
# # Tuple - Collection of Items
# my_tuple = (1, 4, 9, 16, 25)
# # my_tuple[3] = 64 # Immutable in nature
# print(my_tuple)  # 'tuple' object does not support item assignment
#
# shopping_list_wife = ["bread", "butter", "paneer"]
# shopping_list_wife[2] = "milk"
# print(shopping_list_wife)
#
# # Real world project
# # thetestingacademy.com, sdet.live
# my_tuple = ("a.com", "t.live")
# my_api_list = list(my_tuple) # conversion
# print(my_api_list)
# my_api_list = tuple(my_api_list) # conversion
# print(my_api_list)
#
#
# # Real case, where we Tuples
# API_URLSs = ("https://live/python0x", "https://qa.com", "https://udemy.com")
# print(API_URLSs[0])
# print(API_URLSs[1])

# t = tuple()
# print(t)
#
# # Conversion List to Tuple
# t1 = tuple(["pramod","amit","manisha"])
# print(t1)
#
# t2 = list(t1)
# print(t2)

# hero1 = ("Batman", "Bruce Wayne")
# hero2 = ("Wonder Woman", "Diana Prince")
# new_tuple = (hero1,hero2)
# print(new_tuple)
# print(new_tuple[0]) # ("Batman", "Bruce Wayne")
# print(new_tuple[0][0]) # "Batman"
# print(new_tuple[1][1]) # "Batman"

# a, b, c = (10,11,12)
# print(a)
# print(b)
# print(c)

# Search in Tuple
# cities = ("London", "Paris", "Los Angeles", "Tokyo")
# print("Paris" in cities)
# print("New_delhi" in cities)

# t = (12,34,56)
# # t.append(89)
# # print(t)
# my_list = list(t)
# my_list.append(89)
# print(my_list)
# t1 = tuple(my_list)
# print(t1)

# t = (12, 34, 56)
# my_tuple = t + (4,)
# print(my_tuple)
#
#
# ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
# print(ENV_API_URLS)

# SET
# Collection of Unique
# {} - parenthesis
# list_of_unique_items = {1, 2, 3, 4, 4, 5, 5}
# print(list_of_unique_items)
#
# list1 = [45.2, 33, 33, 45, 21]
# set1 = set(list1)
# print(set1)

# t = ("emy", "for", "emy")
# print(t)
# print(set(t))

# set1 = {1,2,3,7,88,8,8,9,9,9,9}
# set2 = {4,5,6,7,8,88,9,0,7,9}
# my_set = set1.union(set2)
# my_set2 = set1.intersection((set2))
# print(my_set)
# print(my_set2)
# my_set3 = set2.difference(set1)
# my_set4 = set1.difference(set2)
# print(my_set3)
# print(my_set4)

# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 3, 8}
# subset1 = set2.issubset(set1)
# subset2 = set1.issubset(set2)
# print(subset1)
# print(subset2)

# set1 = set(["emy", "For", "emy"])
# print(len(set1))
#
# for i in set1:
#     print(i)
#
# set1.add("Amith")
# set1.add("Amith")

# name = "Amith"
# print(name.upper())

# Dict
# Key and Value
# name -> "Pramod"

# student_infor = {
#     "Name": "Amith",
#     #"Age" :65
#     "Age": "67",
#     "Address": "KA"
# }
#
# print(student_infor)
# print(student_infor["Name"])
# print(student_infor["Age"])
# print(student_infor["Address"])
#
# student_infor["Age"] = 100
# print(student_infor)
#
# student_infor2 = dict(name="Akash", Age=44, address="GA")
# print(student_infor2)

# Student_info1 = {
#     "Name": "Bacchan",
#     "Age": "42",
#     "Address": {
#         "Home": "ND",
#         "Office": "KA"
#     }
# }
#
# Student_info2 = {
#     "Name": "Chennbasu",
#     "Age": "38",
#     "Address": {
#         "Home": "OD",
#         "Office": "AP"
#     }
# }
#
# Students_infor_list = [Student_info1, Student_info2]
# print(Students_infor_list)

l = [1,2,3]
# l.add(4)
l.append(4)
print(l)