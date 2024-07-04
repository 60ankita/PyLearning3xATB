# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "naman"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

# or

x = "malayalam"

w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes")
else:
    print("No")