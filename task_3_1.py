tasks=[]
done=[]

def menu():
    print("\nLIGHTNING MCQUEEN'S TO-DO LIST\nGotta get ready for the big race! Here's what's on deck:")
    print("\n1.Add a task.")
    print("2.View my to-do list.")
    print("3.Mark a task as done.")
    print("4.Remove a task.")
    print("5.Quit.")

def addTask():
    task= input("Enter a task: ")
    tasks.append(task)              #adds the task to list of tasks then marks it as false(not done)
    done.append(False)
    print("Task added successfully.")

def viewList():
    if len(tasks) == 0:
        print("No tasks available.")
        return
    for i in range (len(tasks)):        #prints tasks clearly showing whats pending and whats done
        if done[i]:
            print(i + 1, ".", tasks[i], "(Done)")
        else:
            print(i + 1, ".", tasks[i], "(Pending)")

def markDone():
    if len(tasks) == 0:
        print("No tasks available.")
        return
    viewList()
    number=int(input("Enter task number: "))
    if number >= 1 and number <= len(tasks):    #check if number belong to the list of tasks
        done[number - 1] = True
        print("Task marked as done.")
    else:
        print("Sorry, invalid number.")

def removeTask():
    if len(tasks) == 0:
        print("No tasks available.")
        return
    viewList()
    number=int(input("Enter task number: "))
    if number >= 1 and number <= len(tasks):
        tasks.pop(number - 1)               #remove task from the list
        print("Task removed.")
    else:
        print("Sorry,invalid number.")


while True:
    menu()
    choice = input("\nChoose an option: ")

    if choice == "1":
        addTask()
    elif choice == "2":
        viewList()
    elif choice == "3":
        markDone()
    elif choice == "4":
        removeTask()
    elif choice == "5":
        print("Goodbye!")
        break

