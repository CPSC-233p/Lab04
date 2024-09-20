#Jacob Fishel
#9.18.2024
#Implements the functions to manage the contact list

#`{id: ['first', 'last'], id: ['first', 'last'], id: ['first', 'last']...}`

def add_contact(contact_dictionary, id, first_name, last_name):
    if contact_dictionary[id]:
        return 'error'
    
    contact_dictionary.append({id: [first_name, last_name]})
    return {id: [first_name, last_name]}


def modify_contact(contact_dictionary, id, first_name, last_name):
    if id not in contact_dictionary:
        return 'error'
    
def delete_contact(contact_dictionary, id):
    if id not in contact_dictionary:
        return 'error'
    
    keyValuePair = contact_dictionary[id]
    contact_dictionary.pop('id')

    return keyValuePair

def sort_contacts(contact_dictionary):
    sort = lambda x: contact_dictionary[x]
    sortByFirst = contact_dictionary.sort(sort(0))
    sortByLast = contact_dictionary.sort(sort(1))

