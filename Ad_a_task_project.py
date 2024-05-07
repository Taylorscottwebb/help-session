# Project Requirements


# User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
# ```
# Welcome to the To-Do List App!
#     Menu:
#     1. Add a task
#     2. View tasks
#     3. Mark a task as complete
#     4. Delete a task
#     5. Quit

#     ```
# To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task
# Viewing the list of tasks with from Incomplete and Complete tasks.
# Marking a task as complete.
# Deleting a task.
# Quitting the application.
# User Interaction:
# Allow users to interact with the application by selecting menu options using input().
# Implement input validation to handle unexpected user input gracefully.
# Error Handling:
# Implement error handling using try, except, else, and finally blocks to handle potential issues.
# Code Organization:
# Organize your code into functions to promote modularity and readability.
# Use meaningful function names with appropriate comments and doc strings for clarity.
# Testing and Debugging:
# Thoroughly test your application to identify and fix any bugs.
# Consider edge cases, such as empty task lists or incorrect user input.
# Documentation:
# Include a README file that explains how to run the application and provides a brief overview of its features.
# Optional Features (Bonus):
# If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.
# GitHub Repository:
# Create a GitHub repository for your project.
# Commit your code to the repository regularly.
# Include a link to your GitHub repository in your project documentation.






# Submission


# Submit your project, including all source code files and the README, to your instructor or designated platform.






# Project Tips


# Start by designing a simple user interface and plan the program's structure.
# Test your code frequently as you build each feature to ensure everything works as expected.
# Collaborate with fellow learners and seek help when needed. Remember, learning is a communal effort!






# By completing this project, you'll gain practical experience in Python programming and have a useful To-Do List Application to help you stay organized in your own life.



# Happy coding! 📋🐍


#example

# def add_item(cart):
#     item = input("What would you like to add to your cart? ").lower() #lowercases the string
#     if item not in cart:
#         cart.append(item)
#     else:
#         print(f"{item} is already in your cart!")

# # cart holds our place for shopping_cart which we use as an argument in the while loop below
# def remove_item(cart):
#     item = input("Which item would you like to remove from your cart?").lower()
#     # cart.remove(item)
#     try:
#         cart.remove(item)
#     except ValueError:
#         print(f"{item} is not in your cart, you can't remove something that doesn't exist!")

# # cart holds our place for shopping_cart which we use as an argument in the while loop below
# # bag holds the place of the bag list which we will use as an argument in the while loop below
# def bag_item(cart, bag):
#     # take an item from our cart, if it exists
#     # and put it in our bag
#     # remove our item from one list and add it to the other list
#     # mark as "purchased"
#     item = input("Which item would you like to bag?").lower()
#     try:
#         # remove from shopping_cart
#         cart.remove(item)
#         # adds to bag (at the end of the list)
#         bag.append(item)
#     except ValueError:
#         print("That item is not in your cart...")

# def view_items(cart, bag):
#     response = input("Would you like to check your cart or your bag?").lower()
#     if response == "cart":
#         print("Here are your items!")
#         for item in cart:
#             print(item)
#     elif response == "bag":
#         print("Here are your purchased items: ")
#         for item in bag:
#             print(item)
#     else:
#         print("please enter a valid response!")             





# driver code that will call the functions based on the response variable thats holding the user input
# we're using cart and bag as parameters to be consistent with the above functions parameter naming conventions
# when we call the run function, we'll take shopping_cart and bagged_items as arguments
# cart and bag parameters will become the arguments in the functions within the run function
# def run(cart,bag):
#     while True:
#         response = input("What would you like to do? add/remove/purchase/view/quit").lower()
#         if response == "add":
#             # using the shopping_cart list as an argument to fulfill the position of the cart parameter
#             add_item(cart)
#             print(cart)
#         elif response == "remove":
#             remove_item(cart)
#             print(cart)

#         elif response == "purchase":
#             bag_item(cart, bag)
#             print("Your purchased items: ")
#             for item in bag:
#                 print(item)
#         elif response == "view":
#             view_items(cart, bag)

#         elif response == "quit":
#             for item in cart:
#                 print(item)
#             for purchased_item in bag:
#                 print(purchased_item)
#             break
#         else:
#             print("Please enter a valid response")


# # calling the run function with shopping_cart and bagged_items arguments
# run(shopping_cart, bagged_items)



def add_task(notes):
        tasks = input("what tasks would you like to add to your notes?").lower()
        if tasks not in notes:
            notes.append(tasks)
        else:
            print(f"{tasks} is already in your notes!!!")
# This is defining my add to function and is holding our tasks in our notes for our argument in the while loop.

def remove_task(notes):
     tasks = input("what tasks would you like to remove from your notes?").lower()

     try:notes.remove(tasks)
    
     except ValueError:
      print(f"{tasks}is not in your notes, you should add it!!")
#this is also holding a place in our while argument and is also making a exception that the user could of possibly come across.
 


     
