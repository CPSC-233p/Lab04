#Jacob Fishel
#9.18.2024
#Implements the functions to manage the contact list

#`{id: ['first', 'last'], id: ['first', 'last'], id: ['first', 'last']...}`

def add_contact(contact_dictionary, id, first_name, last_name):
    #adds a new contact to the dictionary and returns the key value pair

    id = int(id)
    new_contact = [first_name, last_name]

    if id in contact_dictionary:
        return 'error'
    
    contact_dictionary[id] = [first_name, last_name]

    return {id: [first_name, last_name]}


def modify_contact(contact_dictionary, id, first_name, last_name):
    #modifies a contact to the new id, first and last name

    id = int(id)
    if id not in contact_dictionary:
        return 'error'
    
    else:
        contact_dictionary[id] = [first_name, last_name]

    return {id: [first_name, last_name]}
    

def delete_contact(contact_dictionary, id):
    #Deletes a specified contact from the dictionary

    id = int(id)

    if id not in contact_dictionary:
        return 'error'
    
    else:
        keyValuePair = contact_dictionary[id]
        del contact_dictionary[id]
        return keyValuePair


def sort_contacts(contact_dictionary):
    #sorts contacts by last name, then by first ignoring case
    return contact_dictionary.sort(key=lambda x: [x[1], x[0]])


def find_contact(contact_dictionary, find): 
    #locates find in the contact dictionary

    temp = []

    if find.isnumeric() and find in contact_dictionary:
        key = int(find)
        value = contact_dictionary[find]
        # temp[key] = value
        temp.append({key: value})

    for keys in contact_dictionary.keys():
        value = contact_dictionary[keys]

        if value[0] == find or value[1] == find:
            temp[key] = value

    temp = temp.sort(key=lambda x: [x[1], x[0]])

    return temp









