"""
(Q)Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

"""
#Method1:

# n = int(input("ENter the size of fibonacci numbers: "))
# f1 = 0
# f2 = 1
# if n <= 0:
#     print("It should be in positive numbers")
# elif n == 1:
#     print(f1)
# else:
#     #print("First two numbers of series)
#     print(f1, f2, end=" ")
#     for i in range(n):
#         sum = f1 + f2
#         print(sum, end=" ")
#         f1 = f2
#         f2 = sum

# n = int(input("Enter the size of the fibonacci series: "))
# f1 = 0
# f2 = 1
# if n <= 0:
#     print("Size of the fibonacci series should be a positive integer")
# elif n == 1:
#     print(f1)
# else:
#     #print first two numbers of the series
#     print(f1, f2, end=" ")
#     for i in range(n):
#         sum = f1 + f2
#         print(sum, end=" ")
#         f1 = f2
#         f2 = sum

#Method 2:

# f = int(input("Enter the size: "))
# a = 0
# b = 1
# fib = 0
# if f == 0:
#     print(0)
# elif f == 1:
#     print(0)
# else:
#     for i in range(0, f+2):
#         fib = a + b
#         a = b
#         b = fib
#         print(fib, end=" ")

f = int(input("Enter the number to find fibonacci of: "))
a = 0
b = 1
fib = 0
if f == 0:
    print(0)
elif f == 1:
    print(0)
else:
    for i in range(0, f+2):
        fib = a + b
        a = b
        b = fib
        print(fib, end=" ")