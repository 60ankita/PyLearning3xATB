def allow_to_attend_python_class(name):
    match name:
        case "Ankita":
            print("Hi Ankita, you can attend the class")
        case "Ankit":
            print("Hi Ankit, you can attend the class")
        case "Ankesh":
            print("Hi Ankesh, you can attend the class")
        case _:
            print("Sorry, you can't attend the class")


allow_to_attend_python_class("Anki")