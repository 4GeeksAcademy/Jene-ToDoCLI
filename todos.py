# Sherwood Logistics

last_id: int = 0
tasks:list[str,str|int] =[]
while True:
    print(" ")
    print(" ")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(" >>>----->   SHERWOOD Logistics   <-----<<< ")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(" ")
    print("1. Create Task")
    print("2. List Task")
    print("3. Delete Task")
    print("q. Quit")
    choice:str=input("Make your selection:")
    if choice == "1":
        print("Create new Mission - Add task")
        task_name:str=input("Enter task name: ")
        person:str=input("Enter person assigned:")
        status:str=input("Enter status of task: ")
        priority:str=input("Enter priority of task:")
        last_id += 1
        id = last_id
        tasks.append(create_task(
            task_name,person,status,priority,id
        ))
        print(f"{task_name} added to tasks.\n\n")
    elif choice == "2":
        print(" ")   
        print("Review Mission - List task")
    elif choice == "3":
        print(" ")
        print("Mission Accomplished / Aborted - Delete Task")
    elif choice == "q" or choice == "Q":
        print(" ")
        print("Unstring bows - Quit")
        quit()


