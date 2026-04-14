Data = []

def show_menu():
    print('\n -------TO DO List -------')
    print("WeLCOME To he List")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def Add_Task():
    Task = input("Enter The Task : ")
    Data.append({"Task":Task, "Done":False})
    print(f"Task : '{Task}' added successfully!")
    return

def View_Task():
    if not Data:
        print("No Task Yet!")
        return
    print("\n Your Tasks : ")
    for index, Task in enumerate(Data, start=1):
        status = "✔️" if Task ["Done"] else "❌"
        print(f"{index}. {Task['Task']}  {status}")

def Mark_Task():
    View_Task()
    if not Data:
        return
    try:
        index = int(input("Enter A Number To Mark Done : ")) -1
        if 0 <= index < len(Data):
            Data[index]["Done"]= True
            print("Marked as Done!")
        else:
            print("Invalid Number")
    except ValueError:
        print("Enter A Valid Value")

def Remove_Task():
    View_Task()
    if not Data:
        return
    try:
        index = int(input("Enter A Number To Remove Task : ")) -1
        if 0 <= index < len(Data):
            remove = Data.pop(index)
            print(f"Task : '{remove['Task']}' Deleted!")
        else:
            print("Invalid Number")
    except ValueError:
        print("Enter A Valid Value")

while True:
    show_menu()
    try:
        Choice = int(input("Enter Choice ( 1 - 5 ) : "))
    except ValueError:
        print("Please Enter A Valid Number.")
        continue
    except KeyboardInterrupt:
        print("\n\n Program interrupted by user. Exiting...")
        break
    
    if Choice == 1:
        Add_Task()
    elif Choice == 2:
        View_Task()
    elif Choice == 3:
        Mark_Task()
    elif Choice == 4:
        Remove_Task()
    elif Choice == 5:
        print("Program Exit")
        print("BYE...!")
        break
    else:
        print("Invalid Choice. Try Again..")
