# Python
# Attributes / Properties / Data members
# Behaviour / Methods / members functions

# Attributes - name, id, phoneNo, gender, color_eyes, city, location, address.
# By Which you recognize


# Behaviour - walk, talk, write, sing, dance, watch, listen, sleep, cry, simile
# You can do something.

# class Person:
#     # Attributes
#     id = None
#     name = None
#     age = None
#     email = None
#     height = None
#     gender = None
#     phone_no = None
#     address = None
#
#     # Behaviour
#     def talk(self):  # NRNG  # self - this , self will be first argument in every behaviour.
#         print("I can talk")
#
#     def sleep(self, name):  # Arg with No Return
#         print("I am a Method!!")
#         print("Sleep", name)
#
#     def sleep2(self, name):  # Arg with Return
#         print("I am a Method!!")
#         return None
#
#     def walk(self):
#         print("I am walking")
#
#     def walk_return(self):  # No Arg with Return
#         return "I am walking"
#
#
# # Create an Object of the Class
# # ObjectRef = ClassName() -> Object
# tushar = Person()
# tushar.name = "tushar"
# print(tushar.name)
# tushar.talk()
#
#
# rajyalakshmi = Person()
# rajyalakshmi.name = "rajyalakshmi"
# print(rajyalakshmi.name)
# rajyalakshmi.talk()

# class Dog:
#
#     name = None
#     colour = None
#     age = None
#     breed = None
#
#     def sleep(self):
#         print("sleeping")
#
#     def bark(self):
#         print("barking")
#
#     def eat(self, food):
#         print("Food")
#
# dog1 = Dog()
# print(dog1.name)
# dog1.name = "Chow"
# print(dog1.name)
# dog1.sleep()
#
# dog2 = Dog()
# print(dog2.name)
# dog2.name = "Mow"
# print(dog2.name)
#
# dog3 = dog1

# class Dog:
#
#       name = None
#       colour = None
#       age = None
#       breed = None
#
#       def __init__(self,name,age):
#           print("Called, Object is created")
#           self.name = name
#           self.age = age
#
#       def sleep(self):
#           local_variable = 10
#           print("Sleeping")
#           print("Who is sleeping -> ", self.name, self.age)
#           return None
#
# dog1 = Dog("Chow", 10)
# print(dog1.name)
# dog1.age
# #print(dog1.colour)
# dog1.sleep()
#
# print("-----------------------")
#
# dog2 = Dog("Mow", 20)
# print(dog2.name)
# dog2.age
# #print(dog2.colour)
# dog2.sleep()

class Dog:
    name = None # Instance VARIABLE
    age = None
   # color = "Black" - Hardcoded - not generic to all - blueprint?

    def __init__(self, name, age):
        print("Called, Object is created")
        self.name = name
        self.age = age


    def sleep(self):
        local_variable = 10
        print("Sleeping")
        print("Who is sleeping -> ", self.name, self.age)
        return None


dog1 = Dog("chow", 10)
print(dog1.name)
dog1.sleep()
# print(dog1.color)
print(id(dog1))

dog2 = Dog("mow", 20)
print(dog2.name)
dog2.sleep()
# print(dog2.color)
print(id(dog2))


# print(name)
