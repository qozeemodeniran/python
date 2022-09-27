import re

txt = "Holla, what are you up to today?"

# check if "H" is at the beginning of a string
x = re.search(r"\bH\w+", txt)

# output the start and end position of the match
print(x.span())

# output the string passed into the re function
print(x.string)

# output the string where a match was found
print(x.group())