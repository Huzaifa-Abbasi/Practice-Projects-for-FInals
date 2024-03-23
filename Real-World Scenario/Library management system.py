'''Library Management System: Create a program for a library to manage its books and users. It 
should allow adding new books with details like title, author, ISBN, and availability. The program 
should also register new users, track borrowed and returned books, and display available books 
based on various criteria like title, author, or genre.'''

library = {"book":[]}
data = {"student":[]}


def add():
    title = input("Enter the name of the book: ")
    author = input("Enter the name of author: ")
    isbn = int(input("Enter the ISBN: "))
    if title not in library:
        library["book"].append({"title": title, "author": author, "ISBN": isbn})
    else:
        print("Book is Already Available ")

def register():
    name = input("Enter The name of student: ")
    if name not in data:
        data["student"].append(name)

def student_regular():
    student_data = input("Enter the Student status: ")
    if student_data == "regular":
        user_input = input("Enter do you want to borrow return, or add the book: ")
        if user_input == "return":
            name1 = input("Enter the name of book: ")
            library["book"].append(name1)
            print("return accepted")

        elif user_input == "borrow":
            name2 = input("Enter the name of book: ")
            library["book"].pop(name2)
            print("Borrowed: ")


while True:
    user2 = input("sr regular student,/r new student,/ a to add new book: ")
    if user2 == "a":
        add()
        print(library)
    elif user2 == "sr":
        student_regular()
    elif user2 == "r":
        register()
        print(data)
    else:
        user2 == "q"
        break


print(library)