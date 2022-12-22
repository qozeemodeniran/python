# variable declaration
first = 1
second = 2
third = 3

# statement with indexed placeholder
statement = "The first {0}, the second {1}, and the third {2}"

# run the values through the format method
print(statement.format(first, second, third))