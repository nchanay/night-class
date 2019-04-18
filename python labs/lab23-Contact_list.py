# Contact List

import csv


def load(csv):
    """
    Reads a csv file (contacts.csv) and create a dictionary of dictionaries of the contacts. And creates a variable for the header.
    """
    with open(csv) as f:
        lines = f.read().split('\n')

    contact_list = {}
    props = lines[0].split(',')
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(props, row))
        contact_list[contact['Name']] = contact

    return (contact_list, props)


def create(contact, clist):
    """
    Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
    """
    # clist[name] = clist.get(name, {'Name': name, 'Phone Number': number, 'Email': email})
    # return retrieve(name, clist)
    if clist.get(contact['Name']):
        return f"Error: {contact['Name']} already exists."

    clist[contact['Name']] = contact
    return f"Created contact for {contact['Name']}."


def retrieve(name, clist):
    """
    Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
    """
    return clist.get(name, f'Error: {name} does not exist')


def update(contact, name, clist):
    """
    Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
    """
    # clist[name][attribute] = value
    # # if clist.get(name):
    # #     clist[name].update(updated_info)
    # return retrieve(name, clist)
    if clist.get(name):
        clist[name].update(contact)
        return f'Updated contact for {name}'
    return f'Error: {name} does not exist.'


def delete(name, clist):
    """
    Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
    """
    if clist.get(name):
        del clist[name]
        return f'{name} deleted.'
    return f'Error: {name} does not exist.'


def showkeys(clist):
    """
    Show's the keys (names) of contact list
    """
    for k, v in clist.items():
        print(k)


def save(clist, props, csv):
    """
    Writes our contact list a csv file
    """
    contacts = [','.join(props)]
    for name in clist:
        contact = clist[name]
        contacts.append(','.join(contact.values()))

    with open(csv, 'w') as f:
        f.write('\n'.join(contacts))

    return f'Saving contacts as {csv}...'


# with open('contacts.csv', 'w', newline='') as f:
#     a = csv.writer(f, delimiter=',')
#     data=[['Name', 'Phone Number', 'Email'],
#           ['Jon Doe', '(503) 555-1234', 'jdoeboy@gmail.com'],
#           ['Hans Gruber', '(503) 555-2345', 'johnmcclanesucks@ymail.com'],
#           ['Snape', '(503) 555-3456', 'leviosa@hotmail.com']]
#     a.writerows(data)

# with open('contacts.csv', 'w', newline='') as f:
#     headers = ['Name', 'Phone Number', 'Email']
#     thewriter = csv.DictWriter(f, fieldnames=headers)
#
#     thewriter.writeheader()
#     thewriter.writerow({'Name': 'Jon Doe', 'Phone Number': '(503) 555-1234', 'Email': 'jdoeboy@gmail.com'})
#     thewriter.writerow({'Name': 'Hans Gruber', 'Phone Number': '(503) 555-2345', 'Email': 'johnmcclanesucks@ymail.com'})
#     thewriter.writerow({'Name': 'Snape', 'Phone Number': '(503) 555-3456', 'Email': 'leviosa@hogwarts.com'})
#     thewriter.writerow({'Name': 'Scrouge McDuck', 'Phone Number': '(503) 555-4567', 'Email': 'swimmingin$$$@yahoo.com'})
#     thewriter.writerow({'Name': 'Zordon', 'Phone Number': '(503) 555-5678', 'Email': 'gogopowerrangers@comcast.net'})
#     thewriter.writerow({'Name': 'Hawkeye', 'Phone Number': '(503) 555-6789', 'Email': 'igottabow@pointless.gov'})

# with open('contacts.csv', 'r') as f:
#     lines = csv.DictReader(f, delimiter=',')
#     contact_list = {i["Name"]: i for i in lines}

contact_list, props = load('contacts.csv')
print("Hello and welcome to my contact list!\nFirst off how about we take a look at our contacts\n"+"="*60)
showkeys(contact_list)
print("="*60 + "\nNow let's do some CRUD!")
loop = True
valid_inputs = ['c', 'create', 'r', 'retrieve', 'u', 'update', 'd', 'delete', 's', 'save', 'save and exit']
commands = """
    Commands:
    (C)reate a new contact
    (R)etrieve a contact's details
    (U)pdate a contact's information
    (D)elete a contact
    (S)ave and exit
    """
while loop:
    print('='*60)
    while True:
        print(f"Please select a command {commands}")
        user_input = input("> ").lower().strip()
        if user_input in valid_inputs:
            break
        print("Invalid input")
    print("="*60)

    if user_input.startswith('c'):
        print("To create a new contact I will need you to provide some contact detials.")
        contact = {}
        for prop in props:
            contact[prop] = input(f'{prop}: ')
        print(create(contact, contact_list))

    elif user_input.startswith('r'):
        print("To retrieve a contat's details I will need you to provide a name")
        name = input("What is the contat's name you wish to look up : ")
        print(f"Here is the contact details for {name}\n{retrieve(name, contact_list)}")

    elif user_input.startswith('u'):
        print("To update a contat's information I will need you to specify a name, and input new data. No input ='s no update.'")
        name = input("What is the name of our contact : ")
        contact = {}
        for prop in props:
            val = input(f'{prop}: ')
            if val:
                contact[prop] = val
        print(update(contact, name, contact_list))

    elif user_input.startswith('d'):
        print("To delete a contact I will need you to provide a name")
        name = input("what is the name of the contact you would like to delete : ")
        print(delete(name, contact_list))

    else:
        print(save(contact_list, props, 'contacts.csv'))
        loop = False
        print('Goodbye!')
