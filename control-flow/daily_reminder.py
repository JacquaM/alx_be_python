# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Determine the base reminder message
if priority == "high":
    reminder = f"Reminder: '{task}' is a high priority task"
elif priority == "medium":
    reminder = f"Reminder: '{task}' is a medium priority task"
elif priority == "low":
    reminder = f"Note: '{task}' is a low priority task"
else:
    reminder = f"'{task}' has an unknown priority level"

# Add time-bound note
if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"
    elif priority == "low":
        reminder += ". It might be better to finish it soon, but not urgent."
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += "."

print(reminder)

