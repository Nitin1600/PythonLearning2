# Match Statement
# Switch in Java
# match the op and execute
# Python > 3.10

# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block

# Write a program to ask the user which browser he want to run automation

browser_name = input("Enter the name of the browser:\n")
# browser_name = browser_name.lower()

match browser_name:

    case "safari":
        if browser_name == "safari":
            print("Hello  hello")
        print("Execute safari code")
    case "chrome":
        print("Execute chrome code")
    case "firefox":
        print("Execute firefox code")
    case "mozilla":
        print("Execute mozilla code")
    case _:
        print("No browsers")