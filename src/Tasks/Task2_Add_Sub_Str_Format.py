"""

Take two numbers and fetch

-Add,Div,Mul,Pow,Sub,Pow,Max.
-Format output in string format

"""

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter thr num2: "))

max_num = max(num1, num2)
pow = num1**num2
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
modulus = num1 % num2
andd = num1 // num2

print("Maximum_number is: ", f"{max_num}")
print("Power is: ", f"{pow}")
print("Sum is: ", f"{sum}")
print("Sub is: ", f"{sub}")
print("Mul is: ", f"{mul}")
print("Div is: ", f"{div}")
print(f"{modulus}")
print(f"{andd}")