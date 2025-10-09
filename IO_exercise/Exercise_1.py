# write two lines to the file 
# with help of user get the input and write it to file
filepath = r"D:\redi_a25_python\IO_exercise\exercise1.txt"

f = open(filepath,'w')
message = input("write 1st line to file: ")
message += "\n"
f.write(message)

message = input("write 2nd line to file: ")
message += "\n"
f.write(message)

f.close()
