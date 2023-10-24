import sys

height = None
width = None
Third_dim = None
depth = None

height = int(input("Input height: "))
width = int(input("Input width: "))
Third_dim = input("Do you have a Depth? Y/N ")
if Third_dim == "Y" or Third_dim == "y":
    depth = int(input("Input Depth: "))
    print(f"Area is {height * width}, Volume is {height * width * depth}")
else:
    print(f"Area is {height * width}")

sys.exit(0)
