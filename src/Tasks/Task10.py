"""
(Q)Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

"""

# num = int(input("Enter number: \n"))
#
# fact = 1
# i = num
# while i >=1 :
#     fact = i * fact
#     i = i - 1
# print(f"Factorial of {num} is {fact}")

num = int(input("Enter the number: "))
res = 1
if num == 0:
    print(1)
else:
    for i in range(1, num+1):
        res = res * i
print(f"Factorial of {num} is {res}")
