file = open("read_file.txt", "r")
f = file.readlines()

# checking through all the lines
newList = []
for line in f:
    if line[-1] == "\n":
        newList.append(line[:-1])
    else:
        newList.append(line)


# or can be done in more simple way using build in "strip"  method:

# newList = []
# for line in f:
#   newList.append(line.strip())

print(newList)