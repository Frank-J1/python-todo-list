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

            choice = input("Please enter 1/2/3 or q").strip().lower()

            if choice == 'q':
                print("Cancelled Deletion of Task")
                break
            if choice not in num_to_category:
                print("Please enter a valid option!")
                continue

            category = num_to_category[choice]
            break

        while True:
            



    #Moves a task from one list in the dictionary to another
    def move_task(self):
        pass

    #Displays the tasks in the terminal
    def view_tasks(self):
        pass