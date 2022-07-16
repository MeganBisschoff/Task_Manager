# Task Manager

A Python program that manages tasks and the users assigned to each task.

## Description

This program is for for a small business that allows it to track, edit and report on tasks assigned to each member of the team.

Once logged in, a menu is presented to the 'admin' while a limited menu is presented to any other 'user'.

From the user menu, all users are able to:

* Add a new task given the input of the assigned user, task title, task description, due date, completion status and date assigned.
* View all tasks in the database.
* View tasks assigned to them and then either:
    * Mark the task as complete or,
    * Change who the task is assigned to or the due date of the task.

From the admin menu, an admin has extended permissions to:

* Register and validate a new user given the input of a username and password.
* Generate a user and task report in a CSV file.
* Display user and task statistics.

Each menu option calls the corresponding function for action. Any time a task or user is edited the details are updated in the following CSV files.

The program works with two input files:

* A user.txt file that stores the username and password of each team member, per line.
* A tasks.txt file that stores a list of all the tasks that the team is working on, per line, which includes:
  * The username of the person to whom the task is assigned.
  * The title of the task.
  * A description of the task.
  * The date that the task was assigned to the user.
  * The due date for the task.
  * Either a ‘Yes’ or ‘No’ value specifying if the task has been completed.

The program generates two output files:

* A user_overview.txt file that displays a report of the team members statistics, per line, which includes:
  * Total number of registered users.
  * Total number of tasks that have been generated and tracked.
  * Total tasks assigned per user.
  * Percentage of total tasks assigned per user.
  * Percentage of completed tasks assigned per user.
  * Percentage of incompleted tasks assigned per user.
  * Percentage of incompleted and overdue tasks assigned per user.
* A tasks_overview.txt file that displays a report of the tasks statistics, per line, which includes:
  * Total number of tasks that have been generated and tracked.
  * Total number of completed tasks.
  * Total number of incomplete tasks.
  * Total number of incomplete and overdue task.
  * Percentage of incomplete tasks.
  * Percentage of overdue tasks.

## Functionality summary:

* User login
* Register a new user
* Add a new task
* View all tasks
* View and edit a users tasks
* Generate user and task reports
* View user and task statistics

## Programming principles

This program employs the programming concepts of conditional logic, external databases, lists, dictionaries, loops, functions and string handling. Furthermore it employs fundamental programming functions that include enumerate, .item(), indexing and date formating.

## Dependencies

from datetime import date
import os

## Running the program

Run the task_manager.py file in any Python IDE.
View the tasks.txt, user.txt, tasks_overview.txt and user_overview.txt files in any text editing program, such as Notepad++.

## Code preview

```python

# ----- LOG IN ----- #

# This section is displayed first and prompts the user
# to log in to access the Task Manager program
# 'logged_in' is used to control the while loops below

logged_in = False

# While 'logged_in' status is equal to False
# the user must enter username & password to be validated
# Once validated, the while loop changes to True

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

# While 'logged_in' status is equal to True
# the user is presented with the menu() options
while logged_in == True:
    print("\n- Task Manager -\n")

    menu()
```

## Program preview

```
- Please Log In To The Task Manager -

Enter your username: admin
Enter your password: adm1n
Username and password are correct. You are successfully logged in.

- Task Manager -

Select one of the following options below:
        r : Registering a user
        a : Adding a task
        va : View all tasks
        vm : View my task
        gr : Generate reports
        ds : Display statistics
        e : Exit
```

&nbsp;
***  
_I long to accomplish a great and noble task, but it is my chief duty to accomplish small tasks as if they were great and noble._ \~ Helen Keller
***
&nbsp;

## Author

Megan Bisschoff

Project submitted for Software Engineering learnership Level 1 Task 23 at [HyperionDev](https://www.hyperiondev.com/)

[View](https://www.hyperiondev.com/portfolio/86596/) submission results and code review.
