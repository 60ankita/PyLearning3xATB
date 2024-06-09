# Take the 2 int number from the user and we want to add them.
# We need to use the input() function.

input_1 = input("Enter a number: ")
input_2 = input("Enter another number: ")
result = input_1 + input_2
print(result)


input_1 = input("Enter a number: ")
input_2 = input("Enter another number: ")
# type conversion - str -> int -> ? int()
result = int(input_1) + int(input_2)
print(result)

#  + ->  int  sum operation
#  + -> str - concat
# int to str -> str()
# str to int -> int()

print(type(int(input_1)))