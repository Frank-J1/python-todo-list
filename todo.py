class TaskBoard:
    #Define a String : List dictionary that will hold the tasks at different stages
    def __init__(self):
        self.tasks = {
            "To Do": [],
            "In Progress": [],
            "Done": []
        }

    #Add a tasks to the dictionary list
    def add_task(self):

        #Map a number to a "task location"
        #Will be used for error checking
        num_to_category = {"1": "To Do", "2": "In Progress", "3": "Done"}

        #Asks the user where there task should be added to
        while True:
            print("\nWhere would you lile to add the task?")
            print("1) To Do")
            print("2) In Progress")
            print("3) Done")
            print("q) Cancel Task")

            #Clean user input
            choice = input("Enter 1/2/3/ or q").strip().lower()

            if choice == "q":
                print("Addition cancelled")
                return
            if choice not in num_to_category:
                print("Invalid Input, please try again!")
                continue

            category = num_to_category[choice]
            break

        #Asks the user for the name of the task to be added
        #Check if the task is longer than 50 characters and is a valid input
        while True:
            task = input("Please enter your task to add!")

            if not task:
                print("You cannot add a empty task!")
                continue
            if len(task) > 50:
                print("Your task is to long!")
                continue

            #Check if the user wants to add an already existing task
            if task in self.tasks[category]:
                ans = input("You already have this task, would you like to override/add it anyways? (y/n): ").strip().lower()

                if ans not in ("y", "yes"):
                    print("Task not added!")
                    continue
            
            self.tasks[category].append(task)
            print(f"Added '{task}' -> '{category}")

            #Ask the user if they want to add another task
            again = input("Would you like to add another task? (y/n): ").lower().strip()
            if again not in ("y", "yes"):
                break #Go back to "add task" loop if anser is yes


    #Removes a task from the dictionary list
    def remove_task(self):
        num_to_category = {"1": "To Do", "2": "In Progress", "3": "Done"}
        
        while True:
            print("Which category is the task currently in?")
            print("1) To Do")
            print("2) In Progress")
            print("3) Done")
            print("q) Cancel Remove Task")

            choice = input("Please enter 1/2/3 or q: ").strip().lower()

            if choice == 'q':
                print("Cancelled Deletion of Task")
                return
            if choice not in num_to_category:
                print("Please enter a valid option!")
                continue

            category = num_to_category[choice]
            break

        while True:

            if not self.tasks[category]:
                print(f"No tasks foudn in {category}.")
                return
            
            print(f"\nCurrent tasks in {category}: ")
            for i, t in enumerate(self.tasks[category], 1):
                print(f"{i}. {t}")

            task = input("Which task would you like to remove? ").strip()

            if not task:
                print("You must enter a task to remove!")
                continue

            if task not in self.tasks[category]:
                print("You must remove a task that is scheduled!")
                continue

            self.tasks[category].remove(task)

            again = input("Would you like to remove another task? (y/n): ").lower().strip()
            if again not in ("y", "yes"):
                break #Go back to "remove task" loop if anser is yes

            

    #Moves a task from one list in the dictionary to another
    def move_task(self):
        num_to_category = {"1": "To Do", "2": "In Progress", "3": "Done"}
        
        while True:
            print("Which category is the task currently in?")
            print("1) To Do")
            print("2) In Progress")
            print("3) Done")
            print("q) Cancel Remove Task")

            choice = input("Please enter 1/2/3 or q: ").strip().lower()

            if choice == 'q':
                print("Cancelled Deletion of Task")
                return
            if choice not in num_to_category:
                print("Please enter a valid option!")
                continue

            category = num_to_category[choice]
            break

        if not tasks_in_category:
            print(f"{category} is empty!")
            return
            
        tasks_in_category = self.tasks[category]
        for i, task in enumerate(tasks_in_category, start = 1):
            print(f"{i}) {task}")

        while True:

            selection = input("Please enter a task number (or 'q' to cancel): ").strip().lower()
            if selection == 'q':
                print("Action canceled!")
                return
            if not selection.isdigit():
                print("Please enter a number!")
                continue

            idx = int(selection) - 1

            if not (0 <= idx < len(tasks_in_category)):
                print("The number you have added is invalid (out of range!)")
                continue
            break

        while True:
            print("\n Where would you like to move the task?")
            print("1) To Do\n2) In Progress\n3)Done\nq) Cancel Move")

            chocie_to = input("Enter 1/2/3 or q: ").strip.lower()

            if choice == 'q':
                print("Action cancelled")
                return
            if choice not in num_to_category:
                print("Please enter a valid option!")
                continue

            to_category = num_to_category[chocie_to]

            if to_category == category:
                print("Source and destination are the same, Choose a different categroy!")
                continue
            break

        moved = self.tasks[category].pop(idx)
        self.tasks[to_category].append(moved)

        print(f"Moved '{moved}' from '{category}' -> '{to_category}'.")

    #Displays the tasks in the terminal
    def view_tasks(self):
        num_to_category = {"1": "To Do", "2": "In Progress", "3": "Done"}

        while True:
            print("Which List would you like to view?")
            print("1) To Do")
            print("2) In Progress")
            print("3) Done")
            print("q) Cancel Remove Task")

            choice = input ("Please enter 1/2/3 or 'q' to cancel").strip().lower()

            if choice == 'q':
                print("Action cancelled!")
                return
            if not choice.isdigit() :
                print("Please enter a valid number")
                continue

            if choice not in num_to_category:
                print("Please enter a valid option!")
                continue
            break

        category = num_to_category[choice]
        task_to_view = self.tasks[category]

        if not task_to_view:
            print(f"'{category}' is empty!")

        else:
            print(f"\nTasks in '{category}':")
            for i, task in enumerate(task_to_view, start = 1):
                print(f"{i}) {task}")


        print(task_to_view)