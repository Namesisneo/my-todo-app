FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    # automatically closes file
    """Reads a text file and return list of
    to-do items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


# learn about split function and many more
def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do list in text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


#  __name__ is hidden function by python
#  print(__name__)
if __name__ == "__main__":
    #  if name is equal to main in this file
    print("Hello")
    print(get_todos())
