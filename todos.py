# Sherwood Logistics

from functions import create_task
last_id: int = 0
tasks:dict[int, dict[str, str | int]] ={}
while True:
    print("\n")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(" >>>----->   SHERWOOD Logistics   <-----<<< ")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n1. Create Task")
    print("2. List Task")
    print("3. Delete Task")
    print("q. Quit")
    choice:str=input("\nPick a number:")
    if choice == "1":
        print("\nCreate new Mission (Add task)")
        task_name:str=input("\nEnter task name: ")
        person:str=input("Enter person assigned:")
        priority:str=input("Enter priority of task:")
        last_id += 1
        task_id = last_id
        tasks[id] = create_task(
            task_name,person,priority,id
        )
        print(f"\n Task Name :{task_name} is now added to tasks.\n")
    elif choice == "2":   
        print("Review Mission (List task details)")
        lookup_id:int = input("Enter task ID: ")

        if not lookup_id :
            for task in tasks.values():
                print(f"{task['id']}:{task['task_name']} - {task['person']}")
            continue

        if int(lookup_id) not in tasks.keys():
            print(f"Task {lookup_id} not found")
            continue

        task = tasks[int(lookup_id)]
        print(f"{task['id']}:{task['task_name']} - {task['person']}")


    elif choice == "3":
        print("Mission Accomplished / Aborted (Delete Task)")
        
        lookup_id:int = input("Enter task ID to delete: ")
        if int(lookup_id) not in tasks.keys():
            print(f"Task {lookup_id} not found")
            continue 
        if input("Are you sure y/n ?").lower() == "y" :
            del tasks[int(lookup_id)]

    elif choice == "q" or choice == "Q":
        print(" ")
        print("Unstring bows (Quit) ")
        quit()


