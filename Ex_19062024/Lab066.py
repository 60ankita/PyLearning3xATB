# # Function Scope
#
# def a():
#     a = 10
#     print(a)
#
#
# a()

# Function Scope

def my_function():
    a = 10
    local_var = 34
    print("Hello")
    print(a)

# print(a) # name 'a' is not defined
my_function()