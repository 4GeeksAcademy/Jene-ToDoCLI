def create_tasks(task_name:str,person:str,status:str,priority:str,id:int):
    return {
        "id" : id,
        "task_name" :task_name,
        "person" : person,
        "status" : status,
        "priority" : priority

    }