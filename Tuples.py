###########
#tuple
###########
person = ("Female", 37, "Anna")
print(person)
temp = tuple("abc")
print(temp)
print(temp[1])

#cannot chnage the tuple in run time like below
#person[0] = "male"
#this are mostly like a constant array with different data types

list_coord = [1,2,3,4,5,6,7,8]
list_tuple = []

first_tuple = (list_coord[0],list_coord[1])
list_tuple.append(first_tuple)

first_tuple = (list_coord[2],list_coord[3])
list_tuple.append(first_tuple)

first_tuple = (list_coord[4],list_coord[5])
list_tuple.append(first_tuple)

first_tuple = (list_coord[6],list_coord[7])
list_tuple.append(first_tuple)

print(list_tuple)
print(len(first_tuple))

# above operation using for loop with range
i =0 
list_tuple = []
for i in range(0,len(list_coord),2): # range will be from 0 to less then length of list and iterates with step of 2
    first_tuple = (list_coord[i],list_coord[i+1])
    list_tuple.append(first_tuple)
    print(list_tuple)
