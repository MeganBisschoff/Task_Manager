# This program is for for a small business that 
# allows it to track, edit and report on tasks
#  assigned to each member of the team.

# ----- LIBRARIES ----- #

from datetime import date
import os

# ----- DATA LISTS ----- #
# Open and read the user.txt and tasks.txt files
# Loop through files and store all data in accessible data lists.
# Usernames are stored and accessed in 'user_names', passwords in
#   'user_passwords' and tasks in 'user_tasks'.
# Required data is indexed to appended the to relevant list.

user_tasks = []
user_names = []
user_passwords = []

with open ('tasks.txt', 'r', encoding= 'utf-8') as read_tasks:

    for tasks in read_tasks:
        tasks = tasks.strip("\n")
        user_tasks.append(tasks)

with open ('user.txt', 'r', encoding= 'utf-8') as read_users:
    
    for users in read_users:
        users = users.replace(",", "")  
        users = users.strip("\n")
        users = users.split(" ")
        
        user_names.append(users[0])
        user_passwords.append(users[1])

# ----- FUNCTIONS ----- #

def menu():
    # --- Menu --- #
    # This function displays the menu options with variations for
    # 'admin' and 'non-admin' users. 

    if login_username == 'admin':
        
        menu = input('''Select one of the following options below:
        r : Registering a user
        a : Adding a task
        va : View all tasks
        vm : View my task
        gr : Generate reports
        ds : Display statistics
        e : Exit
        \nEnter selection: ''').lower()

    elif login_username != 'admin':
        
        menu = input('''Select one of the following options below:
        a : Adding a task
        va : View all tasks
        vm : View my task
        e : Exit
        \nEnter selection: ''').lower()

    # - Menu options - #
    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()     
    elif menu == 'vm':
        view_mine()
    elif menu == 'gr':
        generate_report()
    elif menu == 'ds': 
        display_statistics()
    elif menu == 'e':
        print("\n- Exit -\n Goodbye!!!")
        exit()
    else:
        print("You have made a wrong choice. Please try again.")

def reg_user():
    # --- Register New User --- #
    # This function registers a new user and writes it to the user.txt file.
    # The registration includes the input and verification of a username, 
    #   password and password confirmatin.
    print("\n- Register New User -\n")
        
    # 'user_name_check" is used to run the while loop below.
    user_name_check = False

    # The loop checks if the username already exists to avoid duplication.
    # If validated, the 'user_name_check' changes to True.
    while user_name_check == False:
            
        # Request input of a new username.
        new_user_name = input("Please enter new user username: ")

        # Validate if/elif the username is already in the 'user_names' list.
        # Once username is checked the 'new_user_name' is appended to data list.
        if new_user_name in user_names:
            print("Username already exists. Please register user with a different username.")
        elif new_user_name not in user_names:
            user_name_check = True 
            user_names.append(new_user_name)

    # 'password_confirmation" is used to run the while loop below.
    password_confirmation = False

    # The loop validates the password and confirmed password.
    # If validated, the 'password_confirmation' changes to True. 
    while password_confirmation == False:
            
        # Request input of a new users password and confirmed password.
        new_user_password = input("Please enter new user password: ")
        new_user_password_confirm = input("Enter password again to confirm: ")
            
        # Validate if/elif the new password and confirmed password are the same.
        # If passwords are confirmed the 'new_user_password' is appended to data list.
        if (new_user_password != new_user_password_confirm):                            
            print("The passwords you entered do not match, please try again.")
        elif (new_user_password == new_user_password_confirm):                          
            password_confirmation = True     
            user_passwords.append(new_user_password)    
            print("Thank you. New username and password has been successfully registered.")

            # Update 'user_names' and 'user_passwords' list.
            user_names.append(new_user_name)
            user_passwords.append(new_user_password)

            # The registered 'new_user' is written to the user.txt file.
            new_user = (f"{new_user_name}, {new_user_password}")
            with open('user.txt', 'a', encoding= 'utf-8') as users:
                users.write("\n" + new_user)
            
def add_task():
    # --- Add New Task --- #
    # This function compiles a new task and writes it to the tasks.txt file.
    # It includes the username, title, description, due date, 
    #   assigned date and completion status.
    print("\n- Add New Task -\n")

    # Request user to input the task details.       
    assigned_to = input("Enter the username of the person whom the task is assigned to: ")
    task_title = input("Enter the title of a task: ")
    task_description = input("Enter the description of the task: ") 
    due_date = input("Enter the due date of the task, using format example 12 Dec 2012: ")
    task_complete = "No"                               
    date_assigned = date.today().strftime("%d %b %Y")          

    # The compiled 'new_task' is appended to the 'user_tasks' data list. 
    new_task = (f"{assigned_to}, {task_title}, {task_description}, {due_date}, {date_assigned}, {task_complete}")
    user_tasks.append(new_task)

    # The compiled 'new_task' is appended to the 'task.txt' file.
    with open('tasks.txt', 'a', encoding= 'utf-8') as tasks:
        tasks.write("\n" + new_task)
                       
    print("Thank you. New task has been successfully added to the file.")

def view_all():
    # --- View All Tasks --- #
    # This function allows a user to view all tasks
    #   in the 'user_tasks' data list.
    print("\n- View All Tasks -\n")

    # Loop through and split the items in 'user_tasks' list.
    for view_all_tasks in user_tasks:                                                   
        view_all_tasks = view_all_tasks.split(", ")                         

        # The corresponding items are indexed to 'view_all_tasks'.
        print(f"\n____________________________________________________"
        f"\nTask: \t\t {view_all_tasks[1]} \nAssigned to: \t {view_all_tasks[0]}"
        f"\nDate Assigned: \t {view_all_tasks[4]} \nDue Date: \t {view_all_tasks[3]}"
        f"\nTask Complete: \t {view_all_tasks[5]} \nTask Description: \n{view_all_tasks[2]}"
        "\n____________________________________________________")

def view_mine():    
    # --- View My Task --- # 
    # This function allows a user to first view, and then edit,
    #   all their tasks in the 'user_tasks' data list.
    print("\n- View My Task -\n")

    # Loop through and split the items in 'user_tasks' list.
    # Enumerate to assign and identify a 'task_num'ber for use in next step.
    for task_num, view_my_task in enumerate(user_tasks):    
        view_my_task = view_my_task.split(",")                    

        # Only the tasks for the logged-in user are displayed.
        # 'view_my_task' is indexed to get the data for the 'login_username'.
        if login_username == view_my_task[0]:

            # The corresponding items are indexed to 'view_my_task'.
            print(f"Task Data For: {login_username}"
            f"\n____________________________________________________"
            f"\nTask Number: \t  {task_num}"         
            f"\nTask: \t\t {view_my_task[1]} \nAssigned to: \t {view_my_task[0]}"
            f"\nDate Assigned: \t {view_my_task[4]} \nDue Date: \t {view_my_task[3]}"
            f"\nTask Complete: \t {view_my_task[5]} \nTask Description: \n{view_my_task[2]}"
            "\n____________________________________________________\n")

    # - Task Action or Return - # 
    # Request user input and then,
    #   index input to retrieve the 'selected_task' from 'user_tasks' lists.    
    user_selection = int(input("Enter the 'Task Number' to mark and edit, or '-1' to return to the main menu: "))
    selected_task = user_tasks[user_selection] 
    
    if user_selection == -1:
        menu()
    elif user_selection != -1:
         
        # - Task Action - #
        # Request user input to take action on 'selected_task'. 
        task_action = input("\nEnter 'E' to edit the task or 'M' to mark the task as complete: ").lower()

        # - 'M'ark Task - #
        # This section marks a task completion status as "Yes".
        if task_action == 'm':

            # Split 'selected_task' to access and index listed items.
            # Once display is complete, the split task items are joined again 
            #   to be updated in 'user_tasks' list and tasks file.
            selected_task = selected_task.split(", ") 

            # 'Task Complete' status is indexed and changed to "No". 
            if selected_task[5] == "No":
                selected_task[5] = "Yes"

                # The corresponding items are indexed to display 'selected_task' data.                     
                print(f"\nThe task has been successfully edited and updated:"
                f"\n____________________________________________________"
                f"\nTask Number: \t  {user_selection}"         
                f"\nTask: \t\t {selected_task[1]} \nAssigned to: \t {selected_task[0]}"
                f"\nDate Assigned: \t {selected_task[4]} \nDue Date: \t {selected_task[3]}"
                f"\nTask Complete: \t {selected_task[5]} \nTask Description: \n{selected_task[2]}"
                "\n____________________________________________________\n")

                selected_task = (", ").join(selected_task)

            # Update 'user_tasks' list.
            index = 0
            for index in range(len(user_tasks)):
                if index == user_selection:
                    user_tasks[index] = selected_task
                    index += 1

            # Update 'tasks.txt' file.
            with open ('tasks.txt', 'w+', encoding= 'utf-8') as read_tasks:
                for lines in user_tasks:
                    read_tasks.write(lines + "\n")

        # - 'E'dit Task - #
        # This section allows the tasks username or due date to be edited.
        elif task_action == 'e':

            # Split 'selected_task' to access and index listed items.
            # Once display is complete, the split task items are joined again 
            #   to be updated in 'user_tasks' list and tasks file.
            selected_task = selected_task.split(", ") 

            # The tasks can only be edited if the 'Task Complete' status is "No".
            if selected_task[5] == "No":

                # Request user input to edit the 'selected_task'.   
                task_action = input("\nEnter 'U' to edit the username or 'D' to edit the due date: ").lower()

                # - Edit 'U'sername - #
                if task_action == "u":

                    # Request user input for editing.
                    # 'Assigned to' username is indexed and changed to user input.
                    edit_username = input("\nChange the username to: ")
                    selected_task[0] = edit_username

                    # The corresponding items are indexed to display 'selected_task' data.
                    print(f"\nThe task has been successfully edited and updated:"
                    f"\n____________________________________________________" 
                    f"\nTask Number: \t  {user_selection}"         
                    f"\nTask: \t\t {selected_task[1]} \nAssigned to: \t {selected_task[0]}"
                    f"\nDate Assigned: \t {selected_task[4]} \nDue Date: \t {selected_task[3]}"
                    f"\nTask Complete: \t {selected_task[5]} \nTask Description: \n{selected_task[2]}"
                    "\n____________________________________________________\n")

                    selected_task = (", ").join(selected_task)

                    # Update 'user_tasks' list.
                    index = 0
                    for index in range(len(user_tasks)):
                        if index == user_selection:
                            user_tasks[index] = selected_task
                            index += 1

                    # Update tasks.txt' file.
                    with open ('tasks.txt', 'w+', encoding= 'utf-8') as read_tasks:
                        for lines in user_tasks:
                            read_tasks.write(lines + "\n")

                # - Edit 'D'ate - #
                elif task_action == "d":

                    # Request user input for editing.
                    # 'Due date' is indexed and changed to user input.
                    edit_date = input("\nEdit due date to, using format example 12 Dec 2012: ")
                    selected_task[3] = edit_date

                    # The corresponding items are indexed to display 'selected_task' data.
                    print(f"\nThe task has been successfully edited and updated:"
                    f"\n____________________________________________________" 
                    f"\nTask Number: \t  {user_selection}"         
                    f"\nTask: \t\t {selected_task[1]} \nAssigned to: \t {selected_task[0]}"
                    f"\nDate Assigned: \t {selected_task[4]} \nDue Date: \t {selected_task[3]}"
                    f"\nTask Complete: \t {selected_task[5]} \nTask Description: \n{selected_task[2]}"
                    "\n____________________________________________________\n")

                    selected_task = (", ").join(selected_task)

                    # Update 'user_tasks' list.
                    index = 0
                    for index in range(len(user_tasks)):
                        if index == user_selection:
                            user_tasks[index] = selected_task
                            index += 1

                    # Update 'tasks.txt' file.
                    with open ('tasks.txt', 'w+', encoding= 'utf-8') as read_tasks:
                        for lines in user_tasks:
                            read_tasks.write(lines + "\n")

            else:
                print(f"\nTask {user_selection} is already complete and cannot be edited.")

def generate_report():
    # --- Generate Report --- # 
    # This function compiles data and generates User and Task reports.
    # A 'user_overview.txt' file is written to output the user report.
    # A 'task_overview.txt' file is written to output the task report.
    print("\n- Generate Report -\n")

    task_overview()
    user_overview()

def task_overview():
    # --- Task Overview --- #

    # - Total tasks - #
    total_tasks = len(user_tasks)

    # - Total complete and incomplete tasks - #    
    total_comp_tasks = 0
    total_incomp_tasks = 0

    # Loop through and split 'user_tasks'
    #   to get 'Completion status' at index[5]
    # Add count to corresponding 'total_comp_tasks' 
    #   and 'total_incomp_tasks' variables.

    for task in user_tasks:
        task = task.split(", ") 

        if task[5] == "Yes":
            total_comp_tasks += 1
        if task[5] == "No":
            total_incomp_tasks += 1

    # - Total incomplete and overdue tasks - #
    today = date.today().strftime("%d %b %Y")
    total_incomp_overdue_tasks = 0
    
    # Loop through and split 'user_tasks'
    #   to get 'Completion status' at index[5] and 'Due date" at index[3]
    # Add username and count (key:value) to 'total_incomp_overdue_tasks' dict.

    for task in user_tasks:
        task = task.split(", ") 

        if task[5] == "No" and task[3] > today:     
            total_incomp_overdue_tasks += 1

    # - Percentage of incomplete tasks - #
    pct_incomp_tasks = round((total_incomp_tasks/total_tasks) * 100, 2)

    # - Percentage of overdue tasks - #
    pct_overdue_tasks = round((total_incomp_overdue_tasks/total_tasks) * 100, 2)

    # - Task report template - #
    task_report = (f"Task Report:"
    f"\n____________________________________________________"
    f"\nTotal tasks: \t\t\t\t {total_tasks} \nTotal completed tasks: \t\t\t {total_comp_tasks}"
    f"\nTotal incpomplete tasks: \t\t {total_incomp_tasks}"
    f"\nTotal incomplete and overdue task: \t {total_incomp_overdue_tasks}"
    f"\nPercentage of incomplete tasks: \t {pct_incomp_tasks}"
    f"\nPercentage of overdue tasks: \t\t {pct_overdue_tasks}"
    "\n____________________________________________________\n")

    # Display report and write to 'task_overview.txt' file.
    print(task_report)
    with open ('task_overview.txt', 'w+') as task_overview:
        task_overview.write(task_report)

def user_overview():
    # --- User Overview --- #

    # - Total users - #
    total_users = len(user_names)

    # - Total tasks - #
    total_tasks = len(user_tasks)

    # - Total tasks assigned per user - #          
    total_user_tasks = {}   

    # Loop through and split 'user_tasks'
    #   to get 'Username' at index[0]
    # Add username and count (key:value) to 'total_user_tasks' dict.

    for users in user_tasks:
        users = users.split(", ")

        if users[0] in total_user_tasks:
            total_user_tasks[users[0]] += 1
        else:
            total_user_tasks[users[0]] = 1

    # - Percentage of total tasks assigned to user - #
    # Iterate through 'total_user_tasks' key:value pairs to calculate percentage.

    pct_user_total_tasks = {}
    for key, value in total_user_tasks.items():             
        pct_user_total_tasks[key] = round((total_user_tasks[key]/total_tasks) * 100, 2)

    # - Percentage of completed tasks assigned to user - # 
    user_comp_tasks = {}

    # Loop through and split 'user_tasks'
    #   to get 'Completion status' at index[5] and 'Username' at index[0]
    # Nested if/elifs cross-reference both conditions and
    #   add username and count (key:value) to 'user_comp_tasks' dict.
    for users in user_tasks:
        users = users.split(", ")

        if users[5] == "Yes":
            if users[0] in user_comp_tasks:
                user_comp_tasks[users[0]] += 1
            else:
                user_comp_tasks[users[0]] = 1
        elif users[5] == "No":
            if users[0] in user_comp_tasks:
                user_comp_tasks[users[0]] += 0
            else:
                user_comp_tasks[users[0]] = 0

    # Iterate through 'user_comp_tasks' key:value pairs to calculate percentage.
    pct_user_comp_tasks = {}
    for key, value in user_comp_tasks.items():           
        pct_user_comp_tasks[key] = round((user_comp_tasks[key]/total_user_tasks[key]) * 100, 2)

    # - Percentage of incompleted tasks assigned to user - #
    user_incomp_tasks = {}

    # Loop through and split 'user_tasks'
    #   to get 'Completion status' at index[5] and 'Username' at index[0]
    # Nested if/elifs cross-reference both conditions and
    #   add username and count (key:value) to 'user_incomp_tasks' dict.
    for users in user_tasks:
        users = users.split(", ")

        if users[5] == "No":
            if users[0] in user_incomp_tasks:
                user_incomp_tasks[users[0]] += 1
            else:
                user_incomp_tasks[users[0]] = 1
        elif users[5] == "Yes":
            if users[0] in user_incomp_tasks:
                user_incomp_tasks[users[0]] += 0
            else:
                user_incomp_tasks[users[0]] = 0

    # Iterate through 'user_incomp_tasks' key:value pairs to calculate percentage.
    pct_user_incomp_tasks = {}
    for key, value in user_incomp_tasks.items():           
        pct_user_incomp_tasks[key] = round((user_incomp_tasks[key]/total_user_tasks[key]) * 100, 2)

    # - Percentage of incompleted and overdue tasks assigned to user - #
    today = date.today().strftime("%d %b %Y")
    user_incomp_overdue_tasks = {}

    # Loop through and split 'user_tasks' to get 'Username' at index[0]
    #   'Completion status' at index[5] and 'Due date" at index[3].
    # Add username and count (key:value) to 'user_incomp_overdue_tasks' dict.
    for users in user_tasks:
        users = users.split(", ")

        if users[5] == "No" and users[3] > today:
            if users[0] in user_incomp_overdue_tasks:
                user_incomp_overdue_tasks[users[0]] += 1
            else:
                user_incomp_overdue_tasks[users[0]] = 1
        elif users[5] == "Yes" and users[3] > today:
            if users[0] in user_incomp_overdue_tasks:
                user_incomp_overdue_tasks[users[0]] += 0
            else:
                user_incomp_overdue_tasks[users[0]] = 0

    # Iterate through 'user_incomp_overdue_tasks' key:value pairs to calculate percentage.
    pct_user_incomp_overdue_tasks = {}
    for key, value in user_incomp_overdue_tasks.items():           
        pct_user_incomp_overdue_tasks[key] = round((user_incomp_overdue_tasks[key]/total_user_tasks[key]) * 100, 2)

    # - User report template - #
    user_report = (f"User Report:"
    f"\n____________________________________________________"
    f"\nTotal users: \t\t\t\t {total_users} \nTotal tasks: \t\t\t\t {total_tasks}"
    f"\nTotal tasks assigned per user: \n {total_user_tasks}" 
    f"\nPercentage of total tasks assigned to user: \n {pct_user_total_tasks}"
    f"\nPercentage of completed tasks assigned to user: \n {pct_user_comp_tasks}"
    f"\nPercentage of incompleted tasks assigned to user: \n {pct_user_incomp_tasks}"
    f"\nPercentage of incompleted and overdue tasks assigned to user: \n {pct_user_incomp_overdue_tasks}"
    "\n____________________________________________________")

    # Display 'user_report' and write to 'user_overview.txt' file.
    print(user_report)
    with open ('user_overview.txt', 'w+') as user_overview:
        user_overview.write(user_report)

def display_statistics():
    # --- Display Statistics --- # 
     # This function displays the number of total tasks and total users.
    print("\n- Display Statistics -\n")

    # Check if file exists using 'isfile' function.
    # If not, first 'generate_report'.
    file_exists = ""

    if os.path.isfile('user_overview.txt'):
        file_exists = True
    else:
        generate_report()
        file_exists = True

    # If 'file_exists', 
    # Read and print indexed lines from the 'user_overview' file.
    if file_exists == True:

        with open ('user_overview.txt', 'r') as read_report:
            stats = read_report.readlines()
            user_stats = stats[2]
            task_stats = stats[3]

            print(f"\nTask and User Statistics:"
            f"\n____________________________________________________\n"
            f"{user_stats}"
            f"{task_stats}"
            f"____________________________________________________")

# ----- LOG IN ----- # 
# This section is displayed first and prompts the user
#   to log in to access the Task Manager program.

# 'logged_in' is used to control the while loops below.
logged_in = False

# While 'logged_in' status is equal to False,
#   the user must enter username & password to be validated.
# Once validated, the while loop changes to True. 
while logged_in == False:
    print("\n- Please Log In To The Task Manager -\n")
    
    # Request user to input username and password.
    login_username = input("Enter your username: ")
    login_password = input("Enter your password: ")
    
    # Check if 'login_username' elif 'login_password' are in lists,
    #    and index it to use in validation checks below.
    if login_username in user_names:
        search_index = user_names.index(login_username)
    elif login_password in user_passwords:
        search_index = user_passwords.index(login_password)

    # Validate if both the 'login_username' and 'login_password' exist in the data lists.       
    if (login_username == user_names[search_index]) and (login_password == user_passwords[search_index]):
        print("Username and password are correct. You are successfully logged in.")
        logged_in = True
    elif (login_username != user_names[search_index]) and (login_password == user_passwords[search_index]):
        print("Username incorrect, please try again.")
    elif (login_username == user_names[search_index]) and (login_password != user_passwords[search_index]):
        print("Password incorrect, please try again.")
    elif (login_username not in user_names) and (login_password not in user_passwords):
        print("Username and password are incorrect, please try again.")

# While 'logged_in' status is equal to True,
#   the user is presented with the menu() options.
while logged_in == True:
    print("\n- Task Manager -\n")

    menu()
