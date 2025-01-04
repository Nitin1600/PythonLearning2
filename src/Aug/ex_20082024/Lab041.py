# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula

# 1 -> User Inputs -> score or marks -> int
# 2 ->  O/p -> str -> A or B....

score = int(input("Enter the score: "))

if score >= 90 and score <=100:
    print("Grade is A")
elif score >= 80 and score <= 89:
    print("Grade is B")
elif score >= 70 and score <=79:
    print("Grade is C")
elif score >= 60 and score <= 69:
    print("Grade is D")
elif score >= 0 and score <= 59:
    print("Grade is F")
elif score < 0:
    print("Please enter marks between 0-100")
else:
    print("Superman!")