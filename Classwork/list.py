###########
#list
###########
shopping_list = ["apple","grape","milk","eggs", "cheese"]
print(shopping_list)

#remove and add elemets to list
shopping_list.append("bananas")
shopping_list.insert(1,"bread")
shopping_list.remove("apple") #removes the only 1st element of the apple not all
print(shopping_list)

#list are not unique or it can have same elemets
shopping_list.append("bananas")
print(shopping_list)

#to find the intex of the item
print(shopping_list.index("milk"))
print(shopping_list[0])
#print(shopping_list.index("apple")) #not present in the list this throw an error
print(shopping_list[-1]) #will return last element

#finding lenth of the list
print(len(shopping_list))

#list manipulation
shopping_list.reverse()
print(shopping_list)
shopping_list.sort()
print(shopping_list)
print(shopping_list[1:2])

###########
#example
###########
# Alice goes to the store with a bag containing a pen.
bag = ["pen"]

# Alice buys a notebook and puts it in her bag.
bag.append("notebook")

# Alice buys a laptop and puts it in her bag.
bag.append("Laptop")

# Alice buys a pencil and puts it in her bag.
bag.append("pencil")

# On the way home, Alice meets a friend and gives them the pen.
bag.remove("pen")

# But Alice then hesitate if she has enough room in her bag for another item. She checks.
length = len(bag)
print(length)

# Alice find the number of items in her bag, and wants to remember if she has a laptop in her bag.
print(bag.index("Laptop"))
print(bag.count("Laptop")) #return the count of the item if not prsent then count = 0 

if "Laptop" in bag:
    print("yes")
else:
    print("no")
# When Alice gets home, she takes all the items out of her bag and shows them to her family.
print(bag)