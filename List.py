import time

print("WHAT TO DO?")

# List of what i need to do.
Task = ["Clean the house","Water the plants","Play clash of clans"]

def Edit():
    print('EDIT TASK?')
    time.sleep(0.2)
    print('VIEW TASK [0]')
    time.sleep(0.2)
    print('Add Task [1]')
    time.sleep(0.2)
    print('Remove/Done Task [2]')
    time.sleep(0.2)
    print('Replace Task [3]')
    time.sleep(0.2)
    print('Clear All [4]')
    time.sleep(0.2)

while True:
    print('Checking...')
    time.sleep(3)
    print(Task,"Current Task")
    time.sleep(2)
    Edit()

    ChooseOpt = input("Choose Option (0-4): ").capitalize()

    def view_task():
        print(Task)
        print('Keep up the good work!')

    def add_task():
        New_Task = input("What task to add?: ").capitalize()
        Task.append(New_Task)
        print('Task Added.')

    def remove_task():
        Remove_Task = input('What task to remove?: ').capitalize()
        if Remove_Task in Task:
            Task.remove(Remove_Task)
            print('Task Removed.')
        else:
            print("Task didn't exist.")

    def replace_task():
        Old_Task = input('What task to replace?: ').capitalize()
        if Old_Task in Task:
            Old2_task = input("What task to add?: ")
            New2_Task = Task.index(Old_Task)
            Task[New2_Task] = Old2_task
            print('Task Replace.')
        else:
            print('No existing task has been found.')

    def clear_all():
        Task.clear()

    if ChooseOpt == '0':
        view_task()
    elif ChooseOpt == '1':
        add_task()
        print(Task, "Updated Task")

    elif ChooseOpt == '2':
        remove_task()
        print(Task)

    elif ChooseOpt == '3':
        replace_task()
        print(Task)

    elif ChooseOpt == '4':
        clear_all()
    else:
        print("Invalid Input, Try Again")

# Return