import os

# checking if file exist before deletion in order to avoid getting error
if os.path.exists("file7.txt"):
    os.remove("file7.txt")
    print("File file7.txt successfully deleted.")
else:
    print("File does not exist")