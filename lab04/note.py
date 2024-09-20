# #Notes to use for lab

# ''''''

# s = 's;k;dhkljgl;'
# if "dh" in s:
#     print(124)
# else:
#     print(456)

# ''''''

# li = [123, 456, 765, 863, 329856]

# search_number = 863

# # for value in li:

# #     if search_number == value:
# #         print('Found')
# #     else:
# #         print("Not Found")

# #or

# if search_number in li:
#     print('Found')

# ''''''

c = {
    '1234' : ["First", "Last"],
    '5678' : ["Sam", "Altman"],
    '8976' : ["Jacob", "Jobs"],
    '0891' : ["Jacob", "Last"]
}

# list = [0th index, 1 index]

# c.sort() cant sort a dictionary, there is no order

li_temp = []

for key, values in c.items():
    # print(key, values)
    li_temp.append([key, values[0], values[1]])

print("Before", li_temp)

li_temp.sort(key= lambda x: [x[2], x[1]])

#sorting by first, then last, so if two last
#names are the same, it will sort the one with
#the first name that comes first, then sort all
#the first names, then sort the one with the last
# name after
#if there is repeated last names, they will be
#sorted by first name
print("After: ", li_temp)

new_contacts = {}
for values in li_temp:

    new_contacts[values[0]] = [values[1], values[2]]

print(new_contacts)

''''''

#find_contacts
# Define a function named `find_contact` to meet the following requirements:
#           1. Take a contact dictionary as a positional parameter.
#           1. Take a `find` as a keyword parameter.
#           2. Create an empty dictionary.
#           3. If find is a numeric value and contained as a key in the dictionary, add the key:value pair to the created dictionary.
#           4. Loop through all the key:value pairs and if the find substring is contained in either the first name or last name, add the key:value pair to the created dictionary.
#           5. Sort the created dictionary in ascending order by last name, and then by first name, ignoring case.
#           6. Return the created dictionary. 


# find_contact(contacts_dictionary, find = input("Enter the search string")) #function call

def find_contact(contacts_dictionary, find):
    search_dict = {}

    #if find is an int and find is in contacts_dictoinary.keys():
    search_dict[find] = contacts_dictionary[find]

    for key, value in contacts.items():
        if find in value[1] or find in value [2]:
            serach_dict[key] = contacts[key]

            #or

            search_dict[key] = contacts[key]


# find = input("enter search string")
# find_contact(contacts_dictionary, find)