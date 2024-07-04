def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "Ankita"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))

# or

def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]


s = "Sharma"

print("The original string is : ", end="")
print(s)

print("The reversed string(using recursion) is : ", end="")
print(reverse(s))

# or

# Python code to reverse a string
# using reversed()

# Function to reverse a string
def reverse(string):
	string = "".join(reversed(string))
	return string

s = "eat"

print("The original string is : ", end="")
print(s)

print("The reversed string(using reversed) is : ", end="")
print(reverse(s))
