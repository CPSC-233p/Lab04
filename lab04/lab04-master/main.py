#Jacob Fishel
#9.19.2024
#Main file to use contact functions

import contacts

contact_dictionary = {}

while True:

    print("       *** TUFFY TITAN CONTACT MAIN MENU")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list (sorted)")
    print("5. Find contact")
    print("6. Exit the program")
    
    choice = int(input("Enter menu choice: "))

    match choice:

        case 1:
            id = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            added = contacts.add_contact(contact_dictionary, id, first_name, last_name)
            if added == 'error':
                print(added)
            else:
                print("Added: " + str(added) + "\n")

        case 2: 
            id = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            modified = contacts.modify_contact(contact_dictionary, id, first_name, last_name)
            if modified == 'error':
                print(modified)
            else:
                print("Modified: " + str(modified))
        
        case 3:
            id = input("Enter phone number: ")
            deleted = contacts.delete_contact(contact_dictionary, id)
            if deleted == 'error':
                print("Invalid phone number")
            else:
                print("Deleted: " + str(deleted))

        case 4:
            print("==============CONTACT LIST=================")
            print("Last Name          First Name          Phone")
            print("================== =================== =========\n")
            for key in contact_dictionary.keys():
                fullName = contact_dictionary[key]
                first_name = fullName[0]
                last_name = fullName[1]
                print(str(last_name) + "             " + str(first_name) + "               " + str(key))
        
        case 5:
            find = input("Enter search string: ")
            found = contacts.find_contact(contact_dictionary, find)
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
                print(str(last_name) + "             " + str(first_name) + "               " + str(key))
        case 6:
            break

        case _:
            break


            


#c = {7145551111: ['Alpha', 'Jobs'], 7145552222: ['Steve', 'Jobs'], 5625553333: ['Bill', 'Gates']} 


