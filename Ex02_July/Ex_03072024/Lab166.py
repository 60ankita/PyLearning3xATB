try:
    with open("TextData.txt", "r") as file:
        content = file.readlines()
        print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    file.close()