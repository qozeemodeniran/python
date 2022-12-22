def counter(mylist, x):
    count = 0
    for item in mylist:
        if(item == x):
            count += 1
    return count

mylist = []
n = int(input("Enter number of elements: "))
for i in range(n):
    item = int(input())
    mylist.append(item)

x = int(input("Enter the number whose count you want to find in the list: "))
y = counter(mylist, x)

print(x, y)