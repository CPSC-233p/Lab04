#Jacob Fishel
#9.19.2024
#Main file to use contact functions

import contacts

contact_dictionary = []

while True:

    print("       *** TUFFY TITAN CONTACT MAIN MENU")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list (sorted)")
    print("5. Find contact")
    print("6. Exit the program")
    
    choice = input("Enter menu choice: ")

    match choice:

        case 1:
            id = ("Enter phone number: ")
            first_name = input("Enter first name:")
            last_name = input("Enter last name:")
            added = add_contact(contact_dictionary, id, first_name, last_name)
            print("Added: " + added)

        case 2: 
            id = ("Enter phone number: ")
            first_name = input("Enter first name:")
            last_name = input("Enter last name:")
            modified = add_contact(contact_dictionary, id, first_name, last_name)
            print("Modified: " + modified)
        
        case 3:
            id = ("Enter phone number: ")
            deleted = add_contact(contact_dictionary, id, first_name, last_name)
            if deleted == 'error':
                print("Invalid phone number")
            print("Deleted: " + deleted)

        case 4:
            print("==============CONTACT LIST=================")
            print("Last Name          First Name          Phone")
            print("================== =================== =========\n")
            for key in contact_dictionary.keys():
                fullName = contact_dictionary[key]
                first_name = fullName[0]
                last_name = fullName[1]
                print(last_name + "          " + first_name + "Name          " + key)
        
        case 5:
            find = input("Enter search string: ")
            found = find_contact(contact_dictionary)
            if found == {}:
                print("============= NO CONTACT FOUND ===========")
                continue

            print("==============CONTACT LIST=================")
            print("Last Name          First Name          Phone")
            print("================== =================== =========\n")
            for key in found.keys():
                fullName = contact_dictionary[key]
                first_name = fullName[0]
                last_name = fullName[1]
                print(last_name + "          " + first_name + "Name          " + key)
        case 6:
            break

        case _:
            break


            





