# LAB_FILES_IO


## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"


# Bonus
## Modify the project to be able to the following instead of  writing the to do items line by line (hint: use the json module):
- each to-do item should be saved with the following attributes:
- - title
  - date & time
  - done (default is false)

- User can display his to do list items as follows:
  ```
  1- Go to Gym - 2023-08-05 08:00:00 - DONE
  2- Visit Grandma - 2023-08-08 21:00:00 - NOT DONE
  ```
  - User can mark a specific Task as Done.
  - User can search in his tasks using the title.
