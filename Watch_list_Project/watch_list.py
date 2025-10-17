import local_data_editing
import Export_data

def main():
    # user_choice = input()
    print("Loading previous data....")
    local_data = Export_data.load()
    if local_data != None:
        print("Loading successful....")
    else:
        print("Issue while loading file not found....")
        local_data = {}
    
    while True:
        print()
        print("What would you like to do?")
        print("1. Add a show")
        print("2. List my watchlist")
        print("3. Mark a show as watched")
        print("4. View watched shows")
        print("5. Export watched shows to CSV")
        print("6. Save and Exit")
        print("7. Exit")

        user_choice = input(f"Enter here: ")

        if user_choice == "1":
            local_data = local_data_editing.add_show(local_data)
        elif user_choice == "2":
            # print(local_data)
            local_data_editing.list_watch_list(local_data)
        elif user_choice == "3":
            local_data = local_data_editing.mark_show_watched(local_data)
        elif user_choice == "4":
            local_data_editing.list_watched_list(local_data)
        elif user_choice == "5":
            Export_data.export_CSV(local_data)
        elif user_choice == "6":
            Export_data.save(local_data)
            break
        elif user_choice == "7":
            break
        else:
            print("you enter outside of the choice try again")
        
if __name__ == "__main__":
    print("Running")
    main()

