# x = True
# y = False
# print(x^y)

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# count = 0
#
# while True:
#     count += 1
#
#     print(f"This will print atleast once. Count={count}")
#
#     if count >= 5:
#         break

# for num in range(2,10):
#     if num % 2 == 0:
#         print("Found an even number: ", num)
#         continue
#     print("Found an odd number: ", num)

parameter = "Amitha"

match parameter:
    case "Amith":
        print("Hi")
    case "AmITh":
        print("2")
    case _:
        print("Default")