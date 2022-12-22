import re

txt = "He is such a good man, in the sense that He always help strangers"

# replace "He" with "Qozeem"
new_txt = re.sub("He", "Qozeem", txt)

print(new_txt)