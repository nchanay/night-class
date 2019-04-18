#  contact list with OOP

class ContactList:
    """
    Contact list with class objects
    """
    def __init__(self, csv=None, props=None):
        if csv is None:
            self.props = props
            self.contacts = {}
        else:
            self.load(csv)


    def load(self, csv):
        """
        reads csv file and parses it into a dictionary of dictionaries
        """
        with open(csv) as f:
            lines = f.read().split('\n')

        contact_list = {}
        props = lines[0].split(',')
        for i in range(1, len(lines)):
            row = lines[i].split(',')
            contact = dict(zip(props, row))
            contact_list[contact['name']] = contact

        self.contacts = contact_list
        self.props = props


    def save(self, csv):
        contacts = [','.join(self.props)]
        for name in self.contacts:
            contact = self.contacts[name]
            contacts.append(','.join(contact.values()))

        with open(csv, 'w')as f:
            f.write('\n'.join(contacts))

        return f'your file has saved'

if __name__ == '__main__':
    contacts = ContactList('contacts.csv')
    print(contacts.contacts)
    print(contacts.props)
