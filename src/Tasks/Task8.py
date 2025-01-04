"""
(Q)Triangle Classifier:
>Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.

"""

a = float(input("Enter first side of triangle: "))
b = float(input("Enter second side of triangle: "))
c = float(input("Enter third side of triangle: "))

if a == b and a == c and b == c:
    print("Equilateral")
elif a == b != c or a == c != b or b == c != a
    print("isoscles")
else:
    print("scalene")

