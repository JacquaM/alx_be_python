import sys

def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    if sys.version_info >= (3, 10):
        # match-case in string to avoid syntax error on 3.8
        code = f'''
match "{priority}":
    case "high":
        reminder = "a high priority task"
    case "medium":
        reminder = "a medium priority task"
    case "low":
        reminder = "a low priority task"
    case _:
        reminder = "a task with unknown priority"
'''
        local_vars = {}
        exec(code, {}, local_vars)
        reminder = local_vars.get("reminder", "a task with unknown priority")
    else:
        # fallback for Python 3.8
        if priority == "high":
            reminder = "a high priority task"
        elif priority == "medium":
            reminder = "a medium priority task"
        elif priority == "low":
            reminder = "a low priority task"
        else:
            reminder = "a task with unknown priority"

    # Use if statement to adjust for time-bound
    if time_bound == "yes":
        print(f"Reminder: '{task}' is {reminder} that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is {reminder}. Consider completing it when you have free time.")

if __name__ == "__main__":
    daily_reminder()

