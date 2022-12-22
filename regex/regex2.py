# import regular expression
import re

# define my string/sentence
my_text = "Hello world, my name is Qozeem Odeniran"

# search the string/text for set of alphabet characters
search = re.findall("[a-e]", my_text)

# sort the resulting array
search.sort()

# output the result
print(search)
