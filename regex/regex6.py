import re

my_string = "one two three four five"

# split at each whitespace
my_split = re.split("\s", my_string)

# spit at the first whitespace occurrence
my_split1 = re.split("\s", my_string, 1)

print(my_split1)