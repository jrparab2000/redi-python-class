import access_server

# local_data = {}

def add_show(local_data):
    title = input("Enter Title (to go back just press enter): ")
    if title != '\n':
        data = access_server.print_show_data(title)
    else:
        return local_data
    
    if data != None:
        local_data.update({len(local_data)+1:data})
        return local_data
    else:
        return local_data
    

def list_watch_list(local_data):
    # count = 0
    for key, value in local_data.items():
        print_data(key, value)
    
def mark_show_watched(local_data):
    unwatched = list_unwatched_list(local_data)
    try:
        numb = int(input("Enter number: "))
    except:
        print("please enter vaild number")
        return local_data
    
    if numb > len(unwatched):
        print("Please enter number from given list")
        return
    try:
        review = int(input("Give review out of 5: "))
    except:
        print("please enter vaild number")
        return local_data
    
    if (review > 5 and review < 1):
        print("Please enter review between 1 to 5")
        return
    # print(local_data)
    local_data[str(numb)]['Watched'] = True
    local_data[str(numb)]['Review'] = review
    return local_data

def list_watched_list(local_data):
    # count = 0
    for key, value in local_data.items():
        if value['Watched']:
            # count += 1
            print_data(key, value)

def list_unwatched_list(local_data):
    unwatched = []
    # count = 0
    for key, value in local_data.items():
        if value['Watched'] == False:
            # count += 1
            print_data(key, value)
            unwatched.append(value["Title"])
    
    return unwatched

def print_data(count,value):
    print(f"-------------------{count}----------------------")
    print(f"Title: {value['Title']}")
    print(f"Genres: {', '.join(value['Genres'])}")
    print(f"Official Rating: {value['Rating']}")
    print(f"Summary: {value['Summary']}")
    if value['Watched']:
        print(f"Watched: Yes, done watching")
        print(f"Review: {value['Review']}/5")
    else:
        print(f"Watched: No, not watched")
    print(f"------------------------------------------")
    print("\n")