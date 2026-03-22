import functions
import time
now = time.strftime("%b-%d-%Y, %H:%M:%S")
print("It is",now)

while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()
    


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos("todos.txt")
        todos.append(todo +"\n")

        functions.write_todos("todos.txt",todos)


    elif user_action.startswith("show"):



        todos = functions.get_todos("todos.txt")

        for index, item in enumerate(todos):

            row = f"{index+1}-{item.strip("\n")}"
            print(row)

    elif user_action.startswith("edit"):

        try:


            number = int(user_action[5:])
            number = number-1

            todos = functions.get_todos("todos.txt")

            new_todos= input("Enter new todo: ")
            todos[number] = new_todos + "\n"

            functions.write_todos("todos.txt",todos)

        except ValueError:
            print("Your command is not valid")
            continue



    elif  user_action.startswith("complete"):

        try:

            number = int(user_action[9:])
            todos = functions.get_todos("todos.txt")
            todos.pop(number-1)
            functions.write_todos("todos.txt",todos)

        except IndexError:

            print("type correct number")

            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("invalid command")


print("bye")