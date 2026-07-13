# Sherwood Logistics

from functions import add_one_task
from functions import print_list
from functions import delete_task
from functions import save_todos
from functions import load_todos

tasks:dict[int, dict[str, str | int]] = load_todos()
task_id: int = max(tasks.keys()) if tasks else 0

while True:
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(" >>>----->   SHERWOOD Logistics   <-----<<< ")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n1. Create Task")
    print("2. List Task")
    print("3. Delete Task")
    print("4. Quit")
    choice:str = input("\nPick a number, my Lord! :")

    if choice == "1":
        print("\nCreate new Mission (Add task)")
        task_name:str=input("\nEnter task name: ")
        person:str=input("Enter person assigned: ")
        priority:str=input("Enter priority of task: ")
        task_id += 1 
        tasks[task_id] = add_one_task(
            task_name,person,priority,task_id
        )
        save_todos(tasks)
        print(f"\nTask : '{task_name}' is now added to the list. God speed, my Lord !\n")
    
    elif choice == "2":   
        print("\nReview Mission (List of task with details)")
        
        list_id:str = input("Enter task ID (or press 0 to view all) : ")
        if not list_id.isdigit():
            print("Please enter a 'number' for ID.")
            continue
        else:
            task_found = print_list(int(list_id),tasks)
            continue

    elif choice == "3":
        print("\nMission Accomplished or Aborted (Delete Task)")
        
        delete_id:str = input("Enter task ID to delete: ")
        if not delete_id.isdigit():
            print("My Lord, Please enter a 'number' for ID.")
            continue
        else :
            confirm_delete = delete_task(int(delete_id),tasks) 
            if confirm_delete == "DELETED":
                save_todos(tasks)
            continue

    elif choice.lower() == "q" or choice == "4":
        print("\nLet's unstring bows and retreat !\n")
        quit()

    elif not choice.isdigit():
        print("\nMy Lord, Please enter a 'number' !")
        continue