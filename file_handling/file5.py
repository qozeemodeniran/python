# open file5.txt with a parameter to allow appending more contents
f = open("file5.txt", "a")

# append some content to file5.txt using write() method
f.write("\nI am now appending new contents.")

# close the file
f.close()

# open the file after appending some contents to it
f = open("file5.txt", "r")

# print the content of the file using the read() method
print(f.read())