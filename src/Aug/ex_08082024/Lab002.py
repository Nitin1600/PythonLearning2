# print("Hello Amith")

with open("output.txt", "w") as file:
    print("Hello", "World", sep='!', end='\n', file=file, flush=True)