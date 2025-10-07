# Text file dumping .txt
# no special formating 
# .csv file are sperated by "," use to store muliple information in excel format 
# / is for the path in linux or mac and \ is used in windows path
# use r"" to avoide \n in windows can be detected as new string so use r"" insted of just ""
# use open(file, mode) to open the file 
# file is the name of the file 
# modes
# 'r': read, 
# 'a': Append the write data, 
# 'w': open the file for writng, and if already exist it owerwrites it 
# 'x': create a file and give error if it already exist 

filepath = r"D:\redi_a25_python\text.txt"
message = "Hello!!!\n"
content = open(filepath, 'w')
content.write(message)
content.close()

message = "This is just for practicing python coding\n"
content = open(filepath, 'a')
content.write(message)

message = "Okay\n"
content.write(message)
message = "Goodbye\n!!!"
content.write(message)
content.close()

filepath = r"text.txt" #this works but file must be in the same directory as this pyhton file
content = open(filepath,'r')
print(content.readline())
print(content.readline())
print(content.readline())
print(content.read())
content.close()

print("\n")

# This is the official way of writing to open file because it don't need to close the file
# it is important becasue if the file is not closed then it wont save the changes

with open(filepath,'a') as content:
    content.write("\nHello world\n")
    content.write("Close this file nothing here\n")

content = open(filepath,'r')
print(content.read())
content.close()

# file.readlines() will return a list of all the remaining lines 

content = open(filepath,'r')
list_content = content.readlines()
print(list_content)
content.close()

# it is better to use it with for loop

content = open(filepath,'r')
for i in content.readlines():
    print(i)
content.close()


