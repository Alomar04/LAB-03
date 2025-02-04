tasks_input = input("Enter the tasks and separate them by commas: ")
tasks = tasks_input.split(",")  
team_members = int(input("Enter the number of team members: "))
max_input = input("Enter max tasks per member (leave it blank if not specified): ")


max_tasks = None
if max_input:
    max_tasks = int(max_input)


error_message = ""
if not tasks or team_members <= 0:
    error_message = "Invalid input. Provide valid tasks and team members."
elif max_tasks:  
    required = (len(tasks) + max_tasks - 1) // max_tasks  
    if required > team_members:
        error_message = f"Not enough team members. You need at least {required}."


if error_message:
    print(error_message)
else:
    
    assignments = {}
    for m in range(team_members):
        assignments[f"Member {m+1}"] = []
    
    
    current_member = 0
    for task in tasks:
        
        assignments[f"Member {current_member+1}"].append(task)
        current_member = (current_member + 1) % team_members
    
    print("\nTask Distribution:")
    for member, tasks_list in assignments.items():
        print(f"{member}: {', '.join(tasks_list)}")