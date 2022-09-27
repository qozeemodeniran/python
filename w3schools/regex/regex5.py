import re

my_text = "Hello, my name is Qozeem Odeniran"

# check if "an" is at the beginning or ending of a word
check = re.findall(r"eem\b", my_text)
check2 = re.findall(r"ze\B", my_text)

print(check2)