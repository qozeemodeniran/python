# open file6.txt with the "w" parameter
f = open("file6.txt", "w")

# overwrite the content using write() method
f.write("I am overriding the content of file6.txt")

# close file6.txt
f.close()

# open the file after overwriting it
f = open("file6.txt", "r")

# display the new contents of file6.txt using read() method
print(f.read())