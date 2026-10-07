file = open("input.txt", "r")
lines = file.readlines()
file.close()
#count lines
print("Number of lines:", len(lines))

#Extract first two lines
first_two_lines = lines[:2]

#Write into a new file
output = open("output.txt", "w")

for line in first_two_lines:
    output.write(line) 

output.close()

print("First two lines written to output.txt")                