import re

# define text
txt = "The item is worth 24 dollars."

# search for all digits characters
search = re.findall("\d", txt)

print(search)