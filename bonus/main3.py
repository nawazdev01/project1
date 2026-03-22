while True:
    user_action = input("type of todos add,show,edit,complete,exit: ")
    user_action = user_action.lower()
    user_action.strip(" ")

    match user_action:

        case "add":
            todo = input("Enter a todo:") +'\n'
            with open("todos3.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos3.txt", "w") as file:
                file.writelines(todos)


        case "show":
            with open("todos3.txt", "r") as file:
                todos = file.readlines()

            for i,j in enumerate(todos):
                print(f"{i+1}-{j.strip("\n")}")

        case "edit":
            number = int(input("Enter the todo number: "))
            number = number - 1
            with open("todos3.txt", "r") as file:
                todos = file.readlines()

            todos[number] = input("enter the new todo: ") + '\n'
            with open("todos3.txt", "w") as file:
                todos = file.writelines(todos)

        case "complete":
            number  = int(input("enter the completed todo number: "))
            number = number - 1
            with open("todos3.txt", "r") as file:
                todos = file.readlines()
                todos.pop(number)
            with open("todos3.txt", "w") as file:
                file.writelines(todos)

        case "exit":
            break


