# Function to create Task
def add_one_task(task_name:str,person:str,priority:str,id:int):
    return {
        "id" : id,
        "task_name" :task_name,
        "person" : person,
        "priority" : priority
    }

#Function to list tasks
def print_list(list_id:int,tasks:dict):    
    if list_id == 0 :
        if not tasks:
            print("There is no tasks in the list")
        else:
            print("\nHere is the list of tasks for reference")
            for task in tasks.values():
                print(f"Task ID {task['id']}: '{task['task_name']}' is assigned to '{task['person']}' and has '{task['priority']}' priority")
        return True
    elif list_id not in tasks.keys():
        print(f"\nTask with ID '{list_id}' is not found")
        return False
    else :
        task = tasks[list_id]
        print(f"\nTask {task['id']}: '{task['task_name']}' is assigned to '{task['person']}' and has '{task['priority']}' priority ")
        return True

#Function to delete a task   
def delete_task(delete_id:int,tasks:dict):
    if delete_id not in tasks.keys():
        print(f"\nTask with ID '{delete_id}' is not found")
        return False 
    else:
        confirm_delete:str = input("Are you certain to delete this task, y/n ?")
        if confirm_delete.lower() == "y" :
            del tasks[delete_id]
            print(f"\nThe task with ID '{delete_id}' is deleted !")
            return True
        elif confirm_delete.lower() == "n":
            print("\nThe task remains untouched !")
            return True
        else :
            print("\nThe task remains untouched !")
            print("Please type 'y' or 'n' to delete !")
            return False