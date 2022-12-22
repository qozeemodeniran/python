# declare variables
amount = 20
items = 4
total = amount * items

# statement with the placeholder
statement = "Each item cost ${:.2f}, and {} items were purchased. Hence, you would be paying the total sum of ${:.2f}"

# print the values through the format method
print(statement.format(amount, items, total))