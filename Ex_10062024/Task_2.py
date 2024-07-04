# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
import math
num = int(input("Enter a number: "))
sq = math.pow(num, 2)
print("Square of", num, "is", sq)
cube = math.pow(num, 3)
print("Cube of", num, "is", cube)

# OR
print("Square of", num, "is", num ** 2, "and Cube is", num ** 3)
# OR
print(f"Square of {num} is {num ** 2} and Cube is {num ** 3}")


# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(num1, "is greater than", num2)
else:
    print(num1, "is less than", num2)
    if num1 == num2:
        print(num1, "is equal to", num2)
    else:
        print(num1, "is not equal to", num2)

# OR

print("num1 is greater then num2" if num1 > num2 else "num1 is less than num2" if num1 < num2 else "num1 is equal to num2" if num1 == num2 else "num1 is not equal to num2" if num1 != num2 else "Invalid input")