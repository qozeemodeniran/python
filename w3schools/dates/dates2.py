import datetime

date = datetime.datetime.now()
print(date.year)
print(date.strftime("%A"))

full_date = datetime.datetime.now()
month = full_date.strftime("%B")
day_of_the_week = full_date.strftime("%A")
year = full_date.year
print(month)
print(day_of_the_week)

print(full_date.strftime(("%x")))
