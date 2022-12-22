import re
my_string = "My name is Qozeem"

check = re.search("^My.*Qozeem$", my_string)

if check:
    print("There's a match for your check")
else:
    print("Sorry, no match for your check")