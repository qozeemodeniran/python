# open file4.txt
f = open("file4.txt", "r")

# read the whole lines in file4.txt using the for-loop
for lines in f:
    print(lines)

# close the file
f.close()